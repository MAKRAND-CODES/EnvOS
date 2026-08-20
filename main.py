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
"""
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


#### PYTHON TUPLES 
## A tuple is ordered like a list , but it is immmutable

## 1.Creating a tuple 

##In List we basically do as follows : cities = ["BHopal","Indore","Delhi","Mumbai"]
cities = ("Bhopal","Indore","Delhi","Mumbai")
city = ("Bhopal",145,42.2)
'''print(cities)
print(city)
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])
print(city[0])
print(city[1])
print(city[2])
'''
city_data = ("Bhopal",145,38.5)
#city_data[1]=150
print(city_data[0])
print(city_data[-1])
print(city_data[1])
print(len(city_data))

###### TUPLE UNPACKING 
state,aqi,temperature = city_data
print(state)
print(aqi)
print(temperature)
print(type("Bhopal"))
print(type("Bhopal",))

#### Creating a Set 
#### Use curly braces

pollutants = {"PM2.5","PM10","NO2","CO","CO2","PM10"}
print(pollutants)

### ADDING ELEMENTS 
''' sets have : add()
'''

pollutants.add("NaS")
print(pollutants)
pollutants.remove("CO")
print(pollutants)

##### Now set operations
'''temp = {25,30,35,40,42}
time  = {"morning,afternoon,evening,midnight"}
temp1 ={34,38,45,50,30}
weather = temp | time
print(weather)
common = temp & temp1
print(common)
only_temp = temp - temp1
print(only_temp)'''

record = ["Bhopal",145,32.5,68]

###### Python Dictionaries
record = {
    "city":"Bhopal",
    "aqi":145,
    "temperature":32.5,
    "humidity":68
}
'''
dictionary = {
    "key":value,
    "key":value
}
'''

"""
"""
Accessing values :
environment[0]
print(environment["city"])
print(environment["aqi"])
output : 145 
List -> access by Index
Dictionary -> access by key

### Adding a new field 

environment["wind_speed"] = 12.5
now print(environment)

--->So Dictionary are Mutable 
--->environment["temperature"] = 33.2
Now print(environment["temperature"])
output -> 33.2
### Removing a field:
-> del environment["humidity"]
now humidity is removed.
Here we can also use the pop :
humidity = environment.pop("humidity")

### Checking a weather a key exists 

## If "aqi" in environment:
    print("AQI is available")

output :  AQI is available.

## get()
->Its an important Python dictionary method.
Suppose we have :

environment = {
    "city":"Bhopal",
    "aqi" : 145
}
And here  If we do -> print(environment["temperature"])
##Here we will get the raises a KeyError because the key doesn't exist.
So instead we do print(environment.get("temperature",0)) , output 0
Now here when we do print(environment.keys())
so this will Getting all keys : 
so here conceptually :
->city 
->aqi
->temperature
->humidity

Now to get all the values :

->print(environment.values())
will give all the values.

for key, value in environment.items():
print(key,":",value)

Output would be:
{
city : Bhopal
aqi : 145
temperature : 32.5
humidity : 68
}

## Nested dictionaries 

environment = {
    "location":{
        "city":"Bhopal",
        "state":"Madhya Pradesh"
    },
    "measurements": {
        "aqi":145,
        "temperatures":32.5,
        "humidity":68
    }
}

// environment 
    |
    |---location
    |   |---city
    |   |---state
    |---measurements
        |----aqi
        |---temperature
        |---humidity
Now to access the city : 
print(environment["location"]["city"])
print(environment["measurements"]["aqi"])
print(environment["location"]["city"])

//List -> Ordered Collection
//Tuple -> Fixed ordered Collection
//Set   -> Unique Collection
//Dictionary -> Key -> value mapping
"""
"""
record = {
    "city" : "Jabalpur",
    "aqi" : 198,
    "temperature" : 34.99,
    "humidity" : 30
}
print(record["city"])
print(record["aqi"])
print(record["temperature"])
print(record["humidity"])

## Python Conditions --- if , elif , else
"""
"""
Python syntax: 
if condition:
    #code

example :

aqi = 175 

if aqi > 150:
    print("Air quality is unhealthy")

Output : Air quality is unhealthy
Python uses indentation 
There are no { } braces
"""
##Also the indentation is part of Python's syntax

##now if+else->
"""
aqi = 90

if aqi>200:
    print("Very Unhealthy")
elif aqi>150:
    print("Unhealthy")
elif aqi > 100:
    print("Moderate")
else:
    print("Good")

"""
"""
Here also order matters , 
Now we have comparison operators :
like -> 
== equal to 
!= not equal to 
> greater than
< less than
>= greater than or equal to 
<= less than or equal to
"""
"""
## Here we have = -> means assignment and == means comparison 
## Example of Comparison Operator is below :
'''a = 10
if ( 10 == 10):
    print("true")
else :
    print("false")'''
"""

"""
Here we have Logical Operators too:
Python uses : 
->and 
->or 
->not """
"""
## Example 
aqi = 145
temperature = 32 
## AND 
if aqi > 100 and temperature > 30:
    print("High pollution and high temperature")
##Here Both conditions must be true.

# OR 

if aqi > 150 or temperature > 40:
    print("Environment warning")

# not 
is_raining = False
if not is_raining:
    print("No rainfall detected")

# not reverse the Boolean value 
# true -> false
# false -> true

# nested if 
# Python uses indentation to define code blocks   

## Python for loop 
## for item in collection:
##    code

cities = ["Bhopal","Indore","Delhi","Mumbai"]

for city in cities:
    print(city)

## For loop with range 
# range()

for i in range(4):
    print(i)
### Start and stop 
range(start , stop)
for i in range(1,4):
    print(i)

##Now we have step too , along with start,stop,step 
# range(start , stop , step )
for i in range(0,4,1):
    print(i)

'''
while condition:
    #code 
Example: 
count = 1

while count <= 5:
    print(count)
    count += 1

output would be : 
1
2
3
4
5
------> Similarly we have break and continue , where break is stop the statement
at the particular point where the condition is applied ,
While the continue statement skips the current line and continues from the remaining line ther.
"""
## NOW WE HAVE FUNCTIONS IN PYTHON 
## CREATING THE FIRST FUNCTION IN PYTHON !! 
def greet():
    print("Hello world")

greet()

def show_platform_entry():
    print("=====================================")
    print("======WELCOME TO EnvOS======")
    print("=====================================")
    print("An Ai driven urban intelligence platform")

show_platform_entry()

##Npw introducing the parameters with functions 
def show_platform_info(name):
    print("=================================")
    print("                EnvOS Platform")
    print(f"Welcome,{name}!")
    print("An AI Driven Urban Intelligence Platform")
    print()

show_platform_info("Makrand")

## Here name is a parameter,and when we call the show_platform_info("Makrand")
##Here the value gets passed into the name.

## Now we have Return Values :
## here we have example below as, 
def get_platform_name():
    return "EnvOS"

platform = get_platform_name()
print(platform)

'''
Here the main difference beween the return and normal print like 
return EnvOS and print("EnvOS) is that print displays only the given value
while the return,Sends a Value to the caller function and here the caller is 
platform = get_platform_name() which returns the same EnvOS.
'''
from envos_platform import show_platform_info,get_platform_name

show_platform_info("Makrand")

platform = get_platform_name()

print("Platform name:",platform)

## FILE HANDLING IN PYTH0N 
## Here we have files to exchange(import / export) the data, between the files that is suppose i have two files
## environment.csv and environment.json no i want to store t he information between the two file then we will use Python file Handling
## Create files
##      |
## Open files
##      |
## Read files 
##      |
## Write files
##      |
## close files
#Use \n escape character for new line

file = open("notes.txt","w")
file.write("EnvOS environmental intelligence platform\n")
file.write("Learning , Practicing , Reading all the way")
file.close()

## Reading the file 
file = open("notes.txt","r")
content = file.read()
print(content)
file.close()

## Here we have,content=file.read() which stores the content that is read by the file.
## The files gives the data->Python stores in it.
## Another method i can use is : 
with open("notes.txt","r") as file:
    content = file.read()
print(content)
##Here by using with open we didnt write the file.close()
##Because it is automatically closed,once the file has been read.

with open("environment.txt","w") as file:
    file.write("City: Indore\n")
    file.write("Temperature: 32.5 C\n")
    file.write("Humidity: 61%\n")
    file.write("PM2.5:82\n")

with open("environment.txt","r") as file:
    data = file.read();
print(data)

##CSV Handling in Python 
import csv
with open("environment.csv","r")as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
## Now suppose we want the average temperature
'''total = total + row[1]
row[1] is a string, we need to convert float(row[1])'''



total_temperature = 0
count = 0

with open("environment.csv","r")as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        temperature=float(row[temperature])

        total_temperature += temperature
        count += 1
    average_temperature = total_temperature / count
    print("Average_temperature:",average_temperature)
