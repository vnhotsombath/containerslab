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
