#Lide of cities with their carbon footprints in tons CO2 per month 
cities = [
    {"name" : "City A", "carbon_footprint" : 500},
    {"name" : "City B", "carbon_footprint" : 350},
    {"name" : "City C", "carbon_footprint" : 600},
    {"name" : "City D", "carbon_footprint" : 200},
]

#lambda function to filter cities below the threshold of 400 tons CO2
threshold = 400
filtered_cities = list(filter(lambda city: city["carbon_footprint"] < threshold, cities))
print("Cities with Carbon Footprint below 400 tons CO2 : ")
for city in filtered_cities:
    print(city["name"])


#addtion of two number using lambda function 

sum = lambda x, y : x + y 
#lambda function is a one line function that takes two arguments x and y and returns their sum
print("Sum of 5 and 10 is : ", sum(5, 10))

square = lambda a : a * a #also using a ** 2 like this 
print(f"Square of the number 5 is {square(5)}")

evenOdd = lambda num : "Even" if num % 2 == 0 else "Odd"
inp = int(input("Enter the number : "))
print(evenOdd(inp))

distances = [40, 55, 30, 70] # km per day
emission_factor = 0.21 #petrol car 

#find out emission using lambda function 
#emission = emission factor * distances 

emissions = list(map(lambda x : x * emission_factor, distances))
print(emissions) #List of emissions value 

#Identify households exceeding 300 units.

units = [210, 320, 280, 410, 260]

households = list(filter(lambda x : x > 300, units)) #filter is another high order function like to analyse the value 
print(households)

# households = list(map(lambda x : x > 300, units)) #filter is another high order function like to analyse the value 
# print(households) it will return the list of true and false value for each element in the list

#compute efficiency  = output / max_output

generation = [120, 150, 180, 200]

max_value = max(generation)

efficiency = list(map(lambda x : x / max_value, generation))

print(efficiency)

cities = [
    {"City" : "Delhi", "AQI": 320},
    {"City" : "Mumbai", "AQI": 185},
    {"City" : "Pune", "AQI": 140},
]

#sorted cities based on AQI
sorted_cities = sorted(cities, key = lambda x : x["AQI"], reverse = False) # reverse false is for descending to ascending
print(sorted_cities)