#Exercise 1
#Create a list named students containing some student names (strings).
#Print out the second student's name.
#Print out the last student's name.

students = ['Vieng', 'Yue', 'Jennifer', 'Nicole', 'KeiLee', 'Katharyn']
print(students[1])
print(students[-1]) # neg. integer to index from the end of a list


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".

foods = 'Pizza', 'Pasta', 'Hamburgers', 'Salads', 'Ramen', 'Soup'
#print(type(foods))
for food in foods:
    print(f'{food} is a good food')


# Exercise 3
# Using a for loop, print just the last two food strings from foods.

#range() returns the sequence of the given number between the given range
#range(start,stop) takes two arguments where the series of num. will begin and end


for f in range(-2, 0):
    print(foods[f])


# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"


home_town = {
    'city': 'Atlanta',
    'state': 'GA',
    'population': '6,000,000'
}

print(f"I was born in {home_town['city']}, {home_town['state']} - popluation of {home_town['population']}") 
#I kept getting a syntax error for the first home_town bracket, but I changed my single quotations to double and it got rid of the error??? Not sure why or how that happened


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000

for key, val in home_town.items():
    print(f'{key} = {val}')


# Exercise 6
# Create an empty list named cohort.

# Using a for loop, add one dictionary to the cohort list for each student name. Each dictionary should have this shape:

#  {
#    'student': 'Tina',
#    'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.

cohort = []

for idx in range(len(students)):
    cohort.append({
        'students': students[idx],
        'fav_food': foods[idx]
    })

for student in cohort:
    print(student)


# Exercise 7
# Using the list of students and list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_students printing out each string.


#list comprehension [<expression> for <item> in <list>] 'I want <expression> for each <item> in <list>'
awesome_students = [f'{student} is awesome!' for student in students]

for item in enumerate(awesome_students):
    print(item) 


# Exercise 8
# Using the tuple foods and list comprehension within a for loop, print each food string that contains the letter a.


for food in (foods):
    if 'a' in food:
        print(food)

