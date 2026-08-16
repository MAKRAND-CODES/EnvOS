"""print("Welcome to EnvOS")
print("Environmental Operating System")

import numpy as np;

numbers = np.array([10,20,30,40])

print(numbers)
print(numbers.mean())

city="Indore"
aqi=145
temperature=32.5
humidity=68
wind_speed = 12.5

print(city)
print(aqi)
print(temperature)
print(humidity)
print(type(city))
print(type(aqi))
print(type(temperature))
print(type(humidity))
print(wind_speed)
"""

#city1 = "Indore"
#city2 = "Bhopal"

#print(city1)
#print(city2)

state = "Bhopal"
city = "Indore"

print(city)
print(state)

print(city + "     " + state)
print(len(city)) #length using len function

print(city[0])
print(city[1])
print(city[2])
print(city[3])
print(city[4])
print(city[-1])

#String methods

'''  city = "Bhopal"
aqi = 140
temperature = 35
print(f"{city} has an AQI of {aqi} and temperature of {temperature}C")   '''

'''print(city.upper())
print(city.capitalize())
print(city.strip())'''

#Python Lists 
cities = ["Bhopal","Indore","Delhi","Mumbai"]
print(cities)
print(cities[3])
print(cities[2])
print(cities[-1])
# Lists can contain Numbers
# AND Also negative indices work here too 
aqi_values = [120,130,150,170]
print(aqi_values)
print(aqi_values[0])
print(aqi_values[1])
print(aqi_values[2])
print(aqi_values[3])
#Adding data -- append()
aqi_values.append(190)
print(aqi_values)
#Removing data
aqi_values.remove(190)
print(aqi_values)

#Here we can use pop too because it generally deletes the last element

#Length of a Lists
print(len(aqi_values))

#To check whether something exists in a list so for that we can use the in operator.
state=["MadhyaPradesh","Uttarakhand","HimachalPradesh","Gurugram","Rajasthan"]
print("Uttarpradesh" in state)
print("MadhyaPradesh" in state)

#NESTED LISTS

envirnomental_data = [
    ["Bhopal",140,35],
    ["Indore",120,45],
    ["Delhi",190,42]
]
print(envirnomental_data[0][1])
print(envirnomental_data[2][2])
