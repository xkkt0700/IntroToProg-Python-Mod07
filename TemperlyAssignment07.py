# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Working with Pickling and Structured Error Handling
# ChangeLog (Who,When,What):
# Kristin Temperly, 3/1/22 created code to complete assignment 07
# GitHub URL:
# ---------------------------------------------------------------------------- #


import pickle

# ask user to quantify how much data they will be entering
number_of_groceries = int(input('Enter the total number of grocery items on your list: '))
data = []

# input data/input groceries
for grocery in range(number_of_groceries):
    lstGroceries = input('Enter grocery item '+str(grocery)+' : ')
    data.append(lstGroceries)

# open a file where you want to store the binary data
objFile = open('grocery.dat', 'wb')

# dump groceries to the file
pickle.dump(data, objFile)

# close the file
objFile.close()

# print pickled data to test that it worked
print('\nthis is what your pickled data looks like:')
print(open("grocery.dat", "rb").read())
# ---------------------------------------------------------------------------- #
# Now do the reverse, and open the pickled data file
objFile = open('grocery.dat', 'rb')

# load data from the file
lstGroceries = pickle.load(objFile)

# close the file
objFile.close()

print('\n....and here is your data that was pickled, but has now been de-serialized: ')
cnt = 0
for lstGroceries in data:
    print('The grocery item in position', cnt, 'is: ', lstGroceries)
    cnt += 1
