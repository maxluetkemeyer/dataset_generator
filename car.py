class Car:
    def __init__(self, model, make, year, number_seats, weight_in_kg, price_in_euro, fuel_level_in_percent):
        self.model: str = model
        self.make: str = make
        self.year: int = year
        self.number_seats: int = number_seats
        self.weight_in_kg: int = weight_in_kg
        self.price_in_euro: int = price_in_euro
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
        self.ambient_light_level_in_lux: float = ambient_light_level_in_lux  # look at whatsapp
        self.current_timestamp = 0  # seconds

    def step(self, car: Car, next_acceleration: float):
        self.current_timestamp += 1
        car.acceleration = next_acceleration

        # update speed
        car.speed = int(next_acceleration + car.speed)

    

