from car import Car


# Sample cars
audi_a7 = Car(model="A7", make="Audi", year=2020, number_seats=5, weight_in_kg=1645, price_in_euro=72400, fuel_level_in_percent=0.7)
bmw_3_series = Car(model="3 Series", make="BMW", year=2021, number_seats=5, weight_in_kg=1570, price_in_euro=50200, fuel_level_in_percent=0.8)
mercedes_e_class = Car(model="E-Class", make="Mercedes-Benz", year=2019, number_seats=5, weight_in_kg=1780, price_in_euro=64500, fuel_level_in_percent=0.6)
ford_mustang = Car(model="Mustang", make="Ford", year=2022, number_seats=4, weight_in_kg=1685, price_in_euro=56500, fuel_level_in_percent=0.7)
toyota_camry = Car(model="Camry", make="Toyota", year=2020, number_seats=5, weight_in_kg=1525, price_in_euro=38900, fuel_level_in_percent=0.9)
volkswagen_golf = Car(model="Golf", make="Volkswagen", year=2021, number_seats=5, weight_in_kg=1265, price_in_euro=27800, fuel_level_in_percent=0.8)
tesla_model_s = Car(model="Model S", make="Tesla", year=2022, number_seats=5, weight_in_kg=2100, price_in_euro=79900, fuel_level_in_percent=0.85)
honda_civic = Car(model="Civic", make="Honda", year=2019, number_seats=5, weight_in_kg=1295, price_in_euro=25500, fuel_level_in_percent=0.75)
jaguar_f_type = Car(model="F-Type", make="Jaguar", year=2023, number_seats=2, weight_in_kg=1665, price_in_euro=81200, fuel_level_in_percent=0.7)
# Append cars to a list
car_list = [audi_a7, bmw_3_series, mercedes_e_class, ford_mustang, toyota_camry, volkswagen_golf, tesla_model_s, honda_civic, jaguar_f_type]


def get_cars(number: int):
    
    return car_list[:number]

