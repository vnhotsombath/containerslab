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