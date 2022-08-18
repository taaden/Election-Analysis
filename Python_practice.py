from optparse import Values


print("Hello World")

# if Statement
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] =="Denver":
    print(counties[1])
if counties[0] != "Jefferson":
   print(counties[2])


# if -else Statments
temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# nested if-else Statement
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# If-elif-else Statements
# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

# membership Operation

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# Combining Membership and Logical operation
# if And
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

# if OR

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is  not in the list of counties.")

#  A condition controlled loop also called while loop
x = 0
while x <= 5:
    print(x)
    x = x + 1


count= 7
while count < 1:
    print("Hello World")

# for loop  iterate through lists and Tuples
counties =[ "Arapahoe","Denver","Jefferson"]

for county in counties:
    print(county)

# for loop in python built in function range()
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

# same output as above whwn using range()
for num in range(5):
    print(num)

# Using f loop in range() for counties
#counties = ["Arapahoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])

# for loop iterate through a dictionary
counties_dict = {"Arapahoe":422820,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)

# Get the Keys of Dictionary
for county in counties_dict.keys():
    print(county)

# the values of a Dictionary
for voters in counties_dict.values():
    print(voters)

# using Dictionary_name[key] to get values
for county in counties_dict:
    print(counties_dict[county])

# using get() to get values
for county in counties_dict:
    print(counties_dict.get(county))

# Get the Key-Value Pairs of a Dictionary using item()
#for key, value in dictionary_name.items():
#    print(key, value)
for county, voters in counties_dict.items():
    print(county, voters)
    print(county  + " county has "+ str(voters)+" registered voters.")

# Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

# using range() in voting data
for i in range(len(voting_data)):

      print(voting_data[i]['county'])

# Get the Values from a List of Dictionaries using nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# would print both key and values
for county_dict in voting_data:

     for key, value in county_dict.items():

         print(value)

# would print the registered voters
for county_dict in voting_data:

     print(county_dict['registered_voters'])

# would print the each the county_dictionary
for county_dict in voting_data:  

     print(county_dict.values())

# to print the county name from each dictionary
for county_dict in voting_data:
    print(county_dict['county'])






 