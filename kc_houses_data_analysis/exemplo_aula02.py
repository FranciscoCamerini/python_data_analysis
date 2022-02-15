import plotly.express as px
import pandas as pd
data = pd.read_csv('data_sets/kc_house_data.csv')



#1. Create a new column called: “house_age”

data['house_age'] = 'house'
data['date'] = pd.to_datetime(data['date'])

#	- If the value of column “date” is greater than 2014-01-01 => “new_house”
data.loc[data['date'] > '2014-01-01', 'house_age'] = "new_house"

#	- If the value of column “date” is less than 2014-01-01 => “old_house”
data.loc[data['date'] < '2014-01-01', 'house_age'] = "old_house"


#2. Create a new column called: “dormitory_type”

data['dormitory_type'] = "dormitory_type"

#	- If the value of column “bedrooms” is equal to 1 => ‘studio’

data.loc[data['bedrooms'] == 1, 'dormitory_type'] = "studio"

#	- If the value of column “bedrooms” is equal to 2 => ‘apartment’

data.loc[data['bedrooms'] == 2, 'dormitory_type'] = "apartment"

#	- If the value of column “bedrooms” is greater than 2 => ‘house’

data.loc[data['bedrooms'] > 2, 'dormitory_type'] = "house"


#3. Create a new column called: “condition_type”

data['condition_type'] = ""

#	- If the value of column “condition” is less than 2 => ‘bad’

data.loc[data['condition'] <= 2, 'condition_type'] = "bad"

#	- If the value of column “condition” is equal to 3 or 4 => ‘regular’

data.loc[(data['condition'] == 3) | (data['condition'] == 4), 'condition_type'] = "regular"


#	- If the value of column “condition” is equal to 5 => ‘good’

data.loc[data['condition'] == 5, 'condition_type'] = "good"


#4. Change the type of column “condition” to STRING

data['condition'] = data['condition'].astype(str)
data['condition_type'] = data['condition_type'].astype(str)

#5.Delete columns: “sqft_living15” and “sqft_lot15”

data = data.drop(['sqft_living15', 'sqft_lot15'], axis=1)

#6. Change the type of column “yr_built” to DATE

data['yr_built'] = pd.to_datetime(data['yr_built'])

#7. Change the type of column “yr_renovated” to DATE

data['yr_renovated'] = pd.to_datetime(data['yr_renovated'])

#8. When was the oldest house built

print(data[['yr_built']].sort_values('yr_built', ascending=True).min())

#R: 1900

#9. Whats the oldest renovation date

print(data[['yr_renovated']].sort_values('yr_renovated', ascending=True).min())
#R: 1934

#10. How many houses have 2 floors?

print(data[data['floors'] == 2].shape[0])
#R: 8241

#11. How many houses have the condition “regular”?

print(data[data['condition_type'] == "regular"].shape[0])

# R: 19710

#12. How many houses have the condition “bad” and have “waterfront”?

print(data[(data['condition_type'] == "bad") & (data['waterfront'] == 1)].shape[0])

# R: 2 houses

#13. How many houses have the condition “good” and “new_house”

print(data[(data['condition_type'] == "good") & (data['house_age'] == "new_house")].shape[0])

# R: 1701 imóveis

#14. Whats the value of the most expensive "studio"

print(data.loc[data['dormitory_type'] == "studio", 'price'].max())

# R: 1.247.000

#15. How many "apartment" houses where renovated in 2015

print(data[(data['dormitory_type'] == "apartment") & (data['yr_renovated'] == 2015)].shape[0])

# R: 0

#16. Whats the max number of bedrooms for a "house"

print(data['bedrooms'].max())

# R: 33

#17. How many "new_house" where registered in 2014

print(data[(data['house_age'] == "new_house") & (data['yr_renovated'] == 2014)].shape[0])

# R: 91

#18. Select columns: “id”, “date”, “price”, “floors”, “zipcode” by each method:

	#18.1 – By column name
print(data[['id', 'date', 'price', 'floors', 'zipcode']])
	#18.2 – By indexes
print(data.iloc[:,0:3])
print(data.iloc[:,8])
print(data.iloc[:,16])
	#18.3 – By indexes and colum names

data18 = data.loc[0:10, ['id', 'date', 'price', 'floors', 'zipcode']]

	#18.4 – Boolean

cols = [True, True, True, False, False, False, False,True, False, False, False, False, False, False, False, False, True, False, False, False, False, False]
print(data.loc[:, cols])

#19. Save a .csv archive with the columns from exercise 18

data18.to_csv('data_sets/exercicio19_aula02.csv', index=False)

#20. Change the colour of the map from "fuchsia" to dark green

data_mapa = data[['id', 'lat', 'long', 'price']]
mapa = px.scatter_mapbox( data_mapa, lat='lat', lon='long', hover_name='id' , hover_data=['price'], color_discrete_sequence = ['darkgreen'], zoom=3)

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout( height=600, margin={'r':0, 't':0, 'l':0, 'b':0})


