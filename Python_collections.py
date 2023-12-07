# Script:                       ops301d10-challenge 07
# Author:                       Bryanna Fox
# Date of latest revision:      12/04/2023
# Purpose:                      Collections

# Assign a list of ten string elements to a variable
Princesses = ['Belle', 'Tiana', 'Arial', 'Mulan', 'Cinderella', 'Merida', 'Jasmine', 'Pocahontas', 'Moana', 'Elsa']

# Print the fourth element of the list
print("Fourth Element:", Princesses[3])

# Print the sixth through tenth element of the list
print("Sixth to Tenth Elements:", Princesses[5:10])

# Change the value of the seventh element to "onion"
Princesses[6] = "onion"

# Print the updated list
print("Updated List:", Princesses)

# Strech Goals

# Using methods on the list
Princesses.append('Snow White')  # append(): Adds another princess to the end of the list
print("After append:", Princesses)

Princesses.clear()  # clear(): Removes all elements from the list
print("After clear:", Princesses)

Princesses = ['Belle', 'Tiana', 'Arial', 'Mulan', 'Cinderella', 'Merida', 'Jasmine', 'Pocahontas', 'Moana', 'Elsa']
list_copy = Princesses.copy()  # copy(): Creates a shallow copy of the list
print("Copied List:", list_copy)

count_Belle = Princesses.count('Belle')  # count(): Counts occurrences of Belle shows up
print("Count of 'Belle':", count_Belle)

Princesses.extend(['Sleaping Beauty', 'Anna'])  # extend(): Adds elements from another iterable (list) to the end of the list
print("After extend:", Princesses)

index_Cinderella = Princesses.index('Cinderella')  # index(): Returns the index of the first occurrence of "cherry"
print("Index of 'Cinderella':", index_Cinderella)

Princesses.insert(2, 'Mulan')  # insert(): Inserts Mulan at index 2
print("After insert:", Princesses)

popped_element = Princesses.pop()  # pop(): Removes and returns the last element
print("Popped Element:", popped_element)

Princesses.remove('Elsa')  # remove(): Removes the first occurrence of Elsa
print("After remove:", Princesses)

Princesses.reverse()  # reverse(): Reverses the order of elements in the list
print("After reverse:", Princesses)

Princesses.sort()  # sort(): Sorts the elements in ascending order
print("After sort:", Princesses)

# Creating a tuple
my_tuple = ('Tiana', 'Arial', 'Mulan')

# Creating a set
my_set = {'Merida', 'Jasmine', 'Pocahontas'}

# Creating a dictionary
my_dict = {'Princess1':'Pocahontas', 'Princesses2':'Moana', 'Princesses3':'Elsa'}

# Print the results
print("\nTuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)

