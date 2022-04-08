import pandas as pd
import plotly.express as px

data = pd.read_csv('data_set/HousingPrices-Amsterdam-August-2021.csv')
print(data.columns)

data = data.drop(['Unnamed: 0'],axis=1)

num = data.shape[0]

print(f'Número de casas a venda = {num} ')

mean = int(round(data['Price'].mean(), 0))

print(f'Com um preço médio de {mean} euros')

x = int(input('Digite um número de quartos: '))

data_x = data[data['Room'] == x]
num_x = data_x.shape[0]
mean_x = int(round(data_x['Price'].mean()))

print(f'Existem {num_x} casas com {x} quartos, com um preço médio de {mean_x} euros')

data_map = data_x[['Address', 'Lat', 'Lon', 'Price', 'Room', 'Area']]
map = px.scatter_mapbox( data_map, lat='Lat', lon='Lon',\
                        hover_name='Address' , hover_data=['Price', 'Room', 'Area'],\
                        color_discrete_sequence = ['fuchsia'], zoom=10)

map.update_layout(mapbox_style='open-street-map')
map.update_layout( height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
map.show()
