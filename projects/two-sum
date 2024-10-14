# step one: it's given an array of integers randomly, we can define the size, so, i think i'll put the maximum of, idk, maybe 5 numbers it's good enough.
# ask for a number. it also cannot be a big one, so we probably will have to deal with it by just putting a limit.
# check if the sum of two numbers inside the array its equal to the number asked.
# return the position of the two numbers in the array that meet the requirement.


# so to generate a random array, we can use either random module or numpy

import random

array = [random.randint(1,10) for _ in range (5)]  #that array wil have 5 numbers, all sorted from 1 to 10.
print(array)

# ask for a number from 2 to 20, since those are the limits possible.
flag = False

while flag == False:
    while True:
        try:
            requested_number = int(input("Please enter a number from 2 to 20. "))
            if 2 <= requested_number <= 20:
                print(f"valid number: {requested_number}")
                break
            else:
                print("it must be between 2 and 20")
        
        except ValueError:
            print("please enter an integer number")

    # iterate through the array with two arrays

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == requested_number:
                print(f"Number position in array: [{i},{j}]")
                flag = True

    if not flag:
        print(f"There's no sum of two numbers in this array that meets to requested number of {requested_number}")