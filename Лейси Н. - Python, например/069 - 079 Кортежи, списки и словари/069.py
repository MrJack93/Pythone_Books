
country = ('Moldova', 'Russia', 'Ukraine', 'France', 'Italy', 'Romania')
print(country)
country_input = str.title(input('Enter the name of one of these countries: '))
country_index = country.index(country_input)
print(f'Index tuple: {country_index}')
