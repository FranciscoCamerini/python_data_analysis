import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data_set/HousingPrices-Amsterdam-August-2021.csv')
print(data.columns)

data = data.drop(['Unnamed: 0'],axis=1)

num = data.shape[0]

print(f'Número de casas a venda = {num} ')

mean = int(round(data['Price'].mean(), 0))

print(f'Com um preço médio de {mean} euros')


data_map = data[['Address', 'Lat', 'Lon', 'Price', 'Room', 'Area']]
map = px.scatter_mapbox(data_map, lat='Lat', lon='Lon',\
                        hover_name='Address' , hover_data=['Price', 'Room', 'Area'],\
                        color_discrete_sequence = ['blue'], zoom=10)

map.update_layout(mapbox_style='open-street-map')
map.update_layout( height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
map.show()

plt.rcParams['figure.figsize'] = (10,8)
sns.set_theme(style="darkgrid")

sns.relplot(x="Area", y="Price", hue="Room", data=data)
plt.show()

x = int(input('Digite um número de quartos:'))

data_x = data[data['Room'] == x]
num_x = data_x.shape[0]

if num_x == 1:
    mean_x = int(round(data['Price'].max(), 0))
else:
    mean_x = int(round(data_x['Price'].mean(), 0))
    
mean_x = list(str(mean_x))

if len(mean_x) > 6:
    new_num = f'{mean_x[0]}.{mean_x[1]} milhões'
else:
    new_num = f'{mean_x[0]}{mean_x[1]}{mean_x[2]} mil'

print(f'Existem {num_x} casa(s) com {x} quarto(s), com um preço médio de {new_num} euros')

data_map = data_x[['Address', 'Lat', 'Lon', 'Price', 'Room', 'Area']]
map_x = px.scatter_mapbox( data_map, lat='Lat', lon='Lon',\
                        hover_name='Address' , hover_data=['Price', 'Room', 'Area'],\
                        color_discrete_sequence = ['fuchsia'], zoom=10)

map_x.update_layout(mapbox_style='open-street-map')
map_x.update_layout( height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
map_x.show()

plt.rcParams['figure.figsize'] = (10,8)
sns.set_theme(style="darkgrid")

sns.relplot(x="Area", y="Price", hue="Room", data=data_x)
plt.show()
