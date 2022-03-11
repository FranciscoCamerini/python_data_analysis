#
# this program gives you the id number and price of the cheapest and most expensive house
# from a real estate agency's (king county, USA) database taken from kaggle.com
# according to a specific number of bedrooms
# and bathrooms set by the user
#
import pandas as pd

data = pd.read_csv('data_sets/kc_house_data.csv')

print('Preencha os atributos da casa ')
print('')

bedrooms = int(input('Numero de quartos: '))
while bedrooms <= 0:
    print('Numero inválido, digite novamente')
    bedrooms = int(input('Numero de quartos: '))

print('')

bathrooms = int(input('Numero de banheiros: '))
while bathrooms <= 0:
    print('Numero inválido, digite novamente')
    bathrooms = int(input('Numero de banheiros: '))


df = data[(data['bedrooms'] == bedrooms) & (data['bathrooms'] == bathrooms)]

# mostrar a id e preço da casa com menor valor e maior valor

print('\nConsiderando-se estes parâmetros')

print('\nCasa com menor valor')

cheap = (df.sort_values('price', ascending=True)['id'])
first = cheap.first_valid_index()

print(f'Numero de ID = {cheap[first]}')

cheap = (df.sort_values('price', ascending=True)['price'])
first = cheap.first_valid_index()

print(f'Valor = {cheap[first]}')
print('')

expensive = (df.sort_values('price', ascending=False)['id'])
first = expensive.first_valid_index()

print('\nCasa com maior valor')
print(f'Numero de ID = {expensive[first]}')

expensive = (df.sort_values('price', ascending=False)['price'])
first = expensive.first_valid_index()

print(f'Valor = {expensive[first]}')
print('')
