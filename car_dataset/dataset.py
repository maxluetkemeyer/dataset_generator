import pandas as pd
import random
from car import Car, Environment
from car_list import get_car


def generate_dataset(
    number_of_rows: int, number_of_custom_outliers: int, number_of_custom_nulls: int, use_time_inaccuracy: bool, chance_of_drive_end: float
) -> pd.DataFrame:
    output_df = pd.DataFrame()
    # generate car
    car: Car = generate_car()
    env: Environment = generate_env()
    # while not enough rows
    for i in range(number_of_rows):
        # has ride ended?
        if False:  # TODO:
            # generate car
            car = generate_car()
            env = generate_env()

        # get row and add
        # env.getrow TODO:
        row: pd.DataFrame = create_row(car=car, env=env)
        output_df: pd.DataFrame = pd.concat([output_df, row])

        env.step(car=car, next_acceleration=0.5)

    # manipulate data
    # apply outliers and nulls

    # use time inaccuracy

    return output_df


def generate_car() -> Car:
    car: Car = get_car()

    car.year = random.randint(1990, 2024)

    price: int = car.price_in_euro
    for i in range(2024 - car.year):
        change_of_value = random.randint(-700, 100)
        price += change_of_value
    car.price_in_euro = price

    car.fuel_level_in_percent = random.random()

    return car


def generate_env() -> Environment:
    # TODO:
    return Environment(ambient_light_level_in_lux=10_000)


def create_row(car: Car, env: Environment) -> pd.DataFrame:
    row = pd.DataFrame(
        [
            {
                "model": car.model,
                "make": car.make,
                "year": car.year,
                "number_seats": car.number_seats,
                "weight_in_kg": car.weight_in_kg,
                "price_in_euro": car.price_in_euro,
                "fuel_level_in_percent": car.fuel_level_in_percent,
                "ambient_light_level_in_lux": env.ambient_light_level_in_lux,
                "speed": car.speed,
                "acceleration": car.acceleration,
            }
        ]
    )

    return row
