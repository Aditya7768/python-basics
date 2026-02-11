
import keyword

#checking the number of keyword in keyword library
print(len(keyword.kwlist)) #there are 35 keywords in python

#Identifier is aname which is given to the variable 
#some rules of the variable 
#1) Identifier cannot start with number 
#2) Identifier cannot contain sprcial symbols 
#3) only _ is allowed as special char 
#4) cannot be same as keyword 

#Single line statement 
p1 = 10 + 20
print(p1)

#multiple line statement

p2 = 20 + 30\
 + 40 + 50 +\
 +70 + 80
print(p2)


p = 10
if p == 10:
    print("p is 10")


'''
DeocString - Documentation String used to provide information about your objects, functions, classes, or modules.
 It is a string literal that appears right after the definition of a function, method, class, or module. 
 Docstrings are used to describe what the object does, its parameters, return values, and any other relevant 
 information. 
'''
def addition_of_number():
    '''This is addition function written using docstring'''
    "This is addition function written using string literal"
    return 10 + 20
print(addition_of_number()) #this will print the result of the function
print(addition_of_number.__doc__) #this will print the docstring of the function
temp = 30
print(id(temp)) #this will return the memory address of the variable temp
print(hex(id(temp))) #this will return the memory address of the variable temp in hexadecimal format

p = 20
q = 20 
r = 40

print(id(p)) #this will return the memory address of the variable p
print(id(q)) #this will return the memory address of the variable q 
print(id(r)) #this will return the memory address of the variable r

r = "Madhur"
s = "Madhur"
t = "Shubham"

print(id(r), id(s), id(t)) #this will return the memory address of the variable r

#Data types 

intVar = 10 #integer data type
floatVar = 10.5 #float data type    
strVar = "Hello World" #string data type
boolVar = True #boolean data type

import sys
val1 = 10 # Integer data type 
print(val1)
print(type(val1)) #this will return the data type of the variable val1
print(sys.getsizeof(val1)) #this will return the size of the variable val1 in bytes
print(val1, "is Ineger?", isinstance(val1, int)) #this will return True if val1 is an instance of int data type

#String concatenation 

s1 = "Green"
s2 = "AI"
s3 = s1 + " " + s2 #this will concatenate the two strings with a space in between
print(s3)

#Environmenta calucation on the data 

daily_units = 11.5
family_members = 4
water_per_person = 135

annual_units = daily_units * 365
annual_water = family_members * water_per_person * 365

print("Annual Electircity units : ", annual_units)
print("Annual water Usage in liters : ", annual_water)

solar_kw = 5.2
wind_kw = 3.8
hydro_kw = 2.0

total_capacity = solar_kw + wind_kw + hydro_kw
print("Total Renewable Capacity(kW) : ", total_capacity)


daily_distance = 42
emission_factor = 0.21

annual_emission = daily_distance * emission_factor * 365
print("Anuual CO2 Emssion in kg : ", annual_emission)

#AQI based health advisory

aqi = int(input(("\nEnter the AQI : ")))

if aqi >= 300:
    print("Emergency : Stay Indoors")
elif aqi >= 200:
    print("Very Unhealthy")
elif aqi >= 100:
    print("Moderate")
else:
    print("Good Air Quality")

#Electricity Slab 

units = int(input("Enter units : "))

if units <= 200:
    bill = units * 4
elif units <= 400:
    bill = (200 * 4) + (units - 200) * 6
else:
    bill = (200 * 4) + (200 * 6) + (units - 400) * 8
print("Bill Amount is : ", bill)

soil_moisture = int(input("Enter the Soil moisture(%) : "))
rain_expected = False 

if soil_moisture < 30 and not rain_expected:
    print("Start Irrigation")
else:
    print("No Irrigation needed")

#Monthly Energy Trend.

units = [210, 230, 260, 300, 340, 380]
for month, value in enumerate(units, 1):
    print(f"Month = {month}, Units = {value}")

#Peak Energy Detection

units = [180, 220, 260, 310, 290]

peak = max(units)
day = units.index(peak) + 1 #adding 1 to get the day number starting from 1 instead of 0

print(f"Peak Energy Consumption: {peak} units on Day {day}")

#Calculating Total Rainfall
# rainfall = [12, 0, 5, 18, 22, 9]
# total_rainfall = sum(rainfall)
# print(f"Total Rainfall: {total_rainfall} mm")

print("Total Rainfall: ", sum([12, 0, 5, 18, 22, 9]), "mm")

height = 50

for year in range(1, 11):
    height += 12
    print(f"Year {year}: Height = {height} cm")

report = "Delhi AQI=320 Status=Emergency"
parts = report.split()
print("City:", parts[0])
print("AQI:", parts[1].split("=")[1])

text = "Reduce plastic waste to protect environment"
words = text.lower()
print(words)

if "plastic" in words:
    print("Plastic is mentioned in the text.")

data = "       Clean Energy Report"
print(data.strip()) #this will remove the leading and trailing whitespace from the string data

unitss = [210, 230, 260, 300]
avg = sum(unitss) / len(unitss)
print("Average:", avg)

aqii = [90, 140, 210, 180, 95]
unsafe = []

#Find out unhealthy days add to list

for aq in aqii:
    if aq >= 150:
        unsafe.append(aq)
print(unsafe)