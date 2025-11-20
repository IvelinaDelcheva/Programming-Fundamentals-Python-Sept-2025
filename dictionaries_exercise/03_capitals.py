country_names = input().split(', ')
capital_cities = input().split(', ') 

countries_capitals = {country_names[index] : capital_cities[index] for index in range(len(country_names))}
# countries_capitals = dict(zip(country_names, capital_cities))

for country, capital in countries_capitals.items():
    print(f'{country} -> {capital}')

