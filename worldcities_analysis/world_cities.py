import pandas as pd
import plotly.express as px

data = pd.read_csv('data_sets/worldcities.csv')

print()

# How many cities are in this dataset

num = data.shape[0]  # ----> 41.001 cities
print(f'CITIES = {num}')


# How many different countries are on the dataset

countries = list(data.groupby('country'))

print(f'COUNTRIES = {len(countries)}')  # ----> 237
print()


# How many cities are on the Southern/Northern hemisphere

print('CITIES PER HEMISPHERE: ')
south = data[data['lat'] < 0]  # ----> South = 5502
north = data[data['lat'] > 0]  # ----> North = 35499

print(f'S = {south.shape[0]}\nN = {north.shape[0]}')
print()

# How many cities are on the Eastern/Western hemisphere

east = data[data['lng'] > 0]  # ----> East = 21917
west = data[data['lng'] <= 0]  # ----> West = 19084

print(f'E = {east.shape[0]}\nW = {west.shape[0]}')
print()


# Average number of inhabitants considering all cities
print()
print()
population_mean = data['population'].mean()  # ----> 111.761,45

print(f'AVERAGE POPULATION TOTAL  = {round(population_mean, 2)}')
print()

# Average number of inhabitants, per Hemisphere


def population_mean(hemisphere):
    return round(hemisphere['population'].mean(), 2)


print(f'AVERAGE POPULATION WEST  =   {population_mean(west)}')
print(f'AVERAGE POPULATION EAST  =  {population_mean(east)}')
print()
print(f'AVERAGE POPULATION NORTH  = {population_mean(north)}')
print(f'AVERAGE POPULATION SOUTH  =  {population_mean(south)}')
print()
print()

# Cities with biggest and lowest population per Hemisphere

print()


def lowest(hemisphere):
    first = hemisphere.sort_values('population', ascending=True).first_valid_index()
    return f'-> {hemisphere["city"][first]}, POPULATION = {hemisphere["population"][first]}'


def biggest(hemisphere):
    first = hemisphere.sort_values('population', ascending=False).first_valid_index()
    return f'-> {hemisphere["city"][first]}, POPULATION = {hemisphere["population"][first]}'


print('CITIES WITH THE LOWEST AND BIGGEST POPULATION PER HEMISPHERE')
print()

print(f'LOWEST EAST {lowest(east)}')  # Nordvik 0.0
print(f'BIGGEST EAST {biggest(east)}')  # Tokyo 37.977.000
print()

print(f'LOWEST WEST {lowest(west)}')  # Timmiarmiut 10
print(f'BIGGEST WEST {biggest(west)}')  # São Paulo 22.046.000
print()

print(f'LOWEST NORTH {lowest(north)}')  # Nordvik 0.0
print(f'BIGGEST NORTH {biggest(north)}')  # Tokyo 37.977.000
print()

print(f'LOWEST SOUTH {lowest(south)}')   # Soldado Bartra = 10
print(f'BIGGEST SOUTH {biggest(south)}')  # Jakarta = 34.540.000
print()


# How many brazilian cities

brazil = data[data['country'] == 'Brazil']
num_brazil = brazil.shape[0]
print(f'BRAZILIAN CITIES = {num_brazil}')  # --> 3371 brazilian cities


# Average population of brazilian cities

print(f'AVERAGE BRAZILIAN CITY POPULATION = {population_mean(brazil)}')  # --> 58.900
print()

# 5 most and least populated brazilian cities

least_brazil = brazil.sort_values('population', ascending=False)['city'].tail()
print('5 LEAST POPULATED BRAZILIAN CITIES')

a = 5
for city in least_brazil:
    print(f'\t {a} - {city}')
    a -= 1

print()


most_brazil = brazil.sort_values('population', ascending=True)['city'].tail()
print('5 MOST POPULATED BRAZILIAN CITIES')

a = 5
for city in most_brazil:
    print(f'\t {a} - {city}')
    a -= 1

print()

# Plot a map showing the location of the 200 most populated cities


data_mapa = data.sort_values('population', ascending=False)[0:200]

mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='lng', hover_name='city',
                         hover_data=['population'], color_discrete_sequence=['fuchsia'], zoom=3)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})


# Plot a map showing the location of the 100 most populated Brazilian cities


data_mapa_brazil = brazil.sort_values('population', ascending=False)[0:100]

mapa_br = px.scatter_mapbox(data_mapa_brazil, lat='lat', lon='lng', hover_name='city',
                         hover_data=['population'], color_discrete_sequence=['blue'], zoom=3)

mapa_br.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
      ])
mapa_br.update_layout(height=600, margin={'r': 0, 't': 0, 'l': 0, 'b': 0})


# Create a function that receives a country and considers
# all cities with 1 million + inhabitants and returns the percentage
# of those cities located in that specific country

set = data[data['population'] > 10**6]


def metro(country):
    per = round(len(set[set["country"] == country]) * 100 / len(set), 2)
    return f'{per}%'


print('WORLD METROPOLES: ')

print(f'\t{metro("Brazil")} are in Brazil')  # ----> 2.49% of metropoles are located in Brazil
print(f'\t{metro("China")} are in China')  # ----> 44.26% of metropoles are located in China
print(f'\t{metro("India")} are in India')  # ----> 6.78% in India
print(f'\t{metro("United States")} are in the USA')  # ----> 6.92% in the United States


# Percentage of metropoles per Hemisphere

def metro_hem(hemisphere):
    set2 = hemisphere[hemisphere['population'] > 10 ** 6]
    per = round(len(set2) * 100 / len(set), 2)
    return f'{per}%'


print()
print(f'\t{metro_hem(east)} are in the East')  # ----> 81.05%
print(f'\t{metro_hem(west)} are in the West')  # ----> 18.95%
print()
print(f'\t{metro_hem(north)} are in the North')  # ----> 90.73%
print(f'\t{metro_hem(south)} are in the South')  # ----> 9.27%
