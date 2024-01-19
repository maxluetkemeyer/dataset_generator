import random

TARGET_TIRE_PRESSURE = 2.5

class Car:

    def __init__(self, model, make, year, number_seats, weight_in_kg, price_in_euro, fuel_level_in_percent):
        self.model: str = model
        self.make: str = make
        self.year: int = year
        self.number_seats: int = number_seats
        self.weight_in_kg: int = weight_in_kg
        self.price_in_euro: float = price_in_euro

        self.fuel_level_in_percent: float = fuel_level_in_percent  # 0 - 1
        self.speed: int = 0
        self.acceleration: float = 0

        self.cruise_control: bool = False
        self.cruise_control_speed: int | None = None

        self.engine_temperature: float = 20
        self.engine_rpm: int = 0
        self.engine_oil_pressure: float = 2
        self.tire_pressure: float = 2.5


class Environment:
    def __init__(self, ambient_light_level_in_lux):
        self.ambient_light_level_in_lux: int = ambient_light_level_in_lux
        self.current_timestamp = 0  # seconds
        self.ended = False

    def step(self, car: Car, next_acceleration: float):

        if self.ended is True:
            raise Exception("The drive has already ended")

        self.current_timestamp += 1

        # Compute ambient light level change 
        # Domain: N [0, 10000]
        # Always: -= 100 * random.random()
        self.ambient_light_level_in_lux -= int(100 * random.random())

        # Probability of the drive ending is 1 if ambient light level is below 300
        # And 0.01 otherwise
        if self.ambient_light_level_in_lux < 300:
            self.ended = True

        # We have a 2% chance that the driver changes the state of the cruise control (de-)activates it
        if random.random() < 0.02:
            car.cruise_control = not car.cruise_control

        # The tire pressure has a 2% chance of decreasing
        # The value of the change is between 0 and 0.2 (uniform distribution)
        # If the tire pressure is below 1.5, the tire pressure will be updated
        # to the target tire pressure (2.5)
        if random.random() < 0.02:
            tire_pressure_change = random.uniform(0, 0.2)
            car.tire_pressure = max(1.5, car.tire_pressure - tire_pressure_change)
        if car.tire_pressure < 1.5:
            car.tire_pressure = TARGET_TIRE_PRESSURE

        if car.cruise_control:
            # If cruise control is active, the cars speed is unchanged
            # And the cruise control speed is set to the current speed
            car.acceleration = 0
            car.cruise_control_speed = car.speed
        else:
            # If cruise control is not active, the cars speed is changed
            # And the cruise control speed is set to None
            car.acceleration = next_acceleration
            car.speed = int(next_acceleration * (car.tire_pressure/TARGET_TIRE_PRESSURE) + car.speed)
            car.cruise_control_speed = None

        # Compute the engine temperature change
        # Domain: [85, 115]
        # Normal distribution (mean: 100, standard deviation: 5)
        # Correlation with acceleration: 0.7
        engine_temparature_change = random.normalvariate(100, 5) * 0.7 * car.acceleration
        car.engine_temperature = max(85, min(115, car.engine_temperature + engine_temparature_change))

        # Compute the engine rpm
        # Domain: [0, 6000]
        # Normal distribution (mean: 4000, standard deviation: 500)
        # Correlation with acceleration: 0.9
        engine_rpm_change = random.normalvariate(4000, 500) * 0.9 * car.acceleration
        car.engine_rpm = max(0, min(6000, car.engine_rpm + int(engine_rpm_change)))

        # Compute the oil pressure change
        # Domain: [0, 200]
        # Normal distribution (mean: 100, standard deviation: 7)
        # Correlation with engine rpm: 0.8
        engine_oil_pressure_change = random.normalvariate(100, 7) * 0.8 * car.engine_rpm
        car.engine_oil_pressure = max(0, min(200, car.engine_oil_pressure + engine_oil_pressure_change))

        # Compute the fuel level change
        # Always: -=0.005
        # If the car is accelerating: -=0.01
        # If the car is braking: +=0.01
        fuel_level_change = -0.005
        if car.acceleration > 0:
            fuel_level_change -= 0.01
        elif car.acceleration < 0:
            fuel_level_change += 0.01

        # The probability of the fuel level being refilled is 1 - fuel_level_in_percent^2
        # This means that the fuel level is refilled more often if the fuel level is low
        if random.random() < 1 - car.fuel_level_in_percent ** 2:
            fuel_level_change += 1

        car.fuel_level_in_percent = max(0, min(1, car.fuel_level_in_percent + fuel_level_change))
