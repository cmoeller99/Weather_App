from geopy.geocoders import Nominatim
'''
Object to output the city 
'''
def cityfunc(query):
	geolocator = Nominatim(user_agent="Your_Name")
	location = geolocator.geocode(query, exactly_one=False)
	i =0
	if len(location)==1:
		city_choice = 0
		return((location, city_choice))
	else:
		for item in location:
			print (str(i) +' :' + str(item))
			i=i+1
		city_choice = input('Which City would you like?')
	try: 
		city_choice = int(city_choice)
		if  city_choice > i:
			print('Option doesnt exist, please choose a City: ')
			return(cityfunc(query))
	except: 
		print('Error: please select a City')
		return(cityfunc(query))
	return((location, city_choice))

'''
1) ask for a city
'''
query = input("please enter in the name of the City:")
user_input = cityfunc(query)
location = user_input[0]
city_choice = user_input[1]

'''
2) convert the city/ country into the long/ lattitude
'''

correct_city = location[city_choice]

latitude,longitude =((correct_city.latitude, correct_city.longitude))

'''
3) Pulling the Raw Data from the Weather API (JSON)
'''
import requests
import json

url = "https://api.weather.gov/points/%s,%s"%(latitude,longitude)
r = requests.get(url)
data = json.loads(r.content.decode())

url2 =data['properties']['forecast']
r2 = requests.get(url2)
data2 = json.loads(r2.content.decode())

time =data2['properties']['periods'][1]['name']
temp =data2['properties']['periods'][1]['temperature']

print(str(correct_city) +': ' + "{} it will be {} degrees Fahrenheit".format(time, temp))




	



