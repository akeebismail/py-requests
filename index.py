#!/usr/bin/env python3
a = 12.3
age = 12
# print('my age is ' + str(age) + ' years')
# print("My age is {0} years".format(age))

print("There are {0} days in {1}, {2}, {3}, {5}, {6} and {7} ".format(31, "Jan", "March", "May", "July", "August",
                                                                      "October", "December"))
for i in range(1, 12):
    print("No {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    print("Hello loop")
print("loop end ")

guess = int(input('guess a number'))
date = int(input('your birth date is :'))

if guess >= 20 and date >= 2:
    print("you can't be born in the future. ode exit")
elif guess >=20 and date <= 10:
    print("you are to old for this. thanks ")
    