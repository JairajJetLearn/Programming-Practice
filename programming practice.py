#Create a program to ask for the marks of 5 subjects (for example- English, Math, Science, Computer Science, and Arts).
#Calculate and print the total marks and average(mean) of the marks.
#If the mean is between 80 and 100, print the remarks as excellent.
#If the mean is between 60 and 80, print the remarks as very good.
#If the mean is between 40 and 60, print the remarks as good.
#If the mean is less than 40, print the remarks as can do better.

English = int(input("What was your english mark?"))
Maths = int(input("What was your english mark?"))
Physics = int(input("What was your english mark?"))
Chemistry = int(input("What was your english mark?"))
Biology = int(input("What was your english mark?"))

total = English + Maths + Physics + Chemistry + Biology
mean = total/5

if 80 <= mean <= 100:
    print("The marks are excellent")
elif 60 <= mean <= 79:
    print("The marks are very good")
elif 40 <= mean <= 59:
    print("The marks are good")
elif 39 >= mean:
    print("The marks can do better")

#Write a program to check whether the entered year is a leap year.

#A year is a leap year if either of the following conditions are satisfied:
#The year is multiple of 400.
#The year is a multiple of 4 and not a multiple of 100.

year = int(input("Enter a year:"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("That year is a leap year")
else:
    print("That year is not a leap year")

#Create a project to ask the user his name and print it 6 times using for loop.

name = input("Whats your name")

for i in range(6):
    print(name)

#Q. Create a project to print all the numbers from 0 to 10 using for loop.
#Q. Create a project to print all the numbers from 7 to 15 using for loop.
#Q. Create a project to print all the even numbers from 6 to 20 using for loop.
#Q. Create a project to print all the odd numbers from 7 to 15 using for loop.
#Q. Create a project to print ten multiples of 3 using for loop.
#Q. Create a project to print twelve multiples of 8 using for loop.
#Q. Create a project to print all the numbers from 10 to 1 using for loop.

for i in range(11):
    print(i)

for a in range(7,16):
    print(a)

for b in range(6,21,2):
    print(b)

for c in range(7,16,2):
    print(c)

for d in range(1,11):
    print(d*3)

for e in range(1,13):
    print(e*8)

for f in range(10,0,-1):
    print(f)

#Q. Create a project to ask the user his name and print it 6 times using while loop.
#Q. Create a project to print all the numbers from 0 to 10 using while loop.
#Q. Create a project to print all the numbers from 7 to 15 using while loop.
#Q. Create a project to print all the even numbers from 6 to 20 using while loop.
#Q. Create a project to print all the odd numbers from 7 to 15 using while loop.
#Q. Create a project to print ten multiples of 3 using while loop.
#Q. Create a project to print twelve multiples of 8 using while loop.
#Q. Create a project to print all the numbers from 10 to 1 using while loop.

name = input("Enter your name")
count = 0

while count < 6:
    print(name)
    count = count + 1

a = 0
while a < 11:
    print(a)
    a = a + 1

b = 7
while b < 16:
    print(b)
    b = b + 1

c = 1
while c < 12:
    print(c*3)
    c = c + 1

d = 1
while d < 13:
    print(d*8)
    d = d + 1

e = 10
while e > 0.9:
    print(e)
    e = e - 1

f = 6
while f < 22:
    print(f)
    f = f + 2

for i in range(5):
    for j in range(3):
        print(i,j)

for g in range(2,11,2):
    for k in range(1,5):
        print(g+k)

counter1 = 2
counter2 = 1

while counter1 < 12:
    while counter2 < 5:
        print(counter1 + counter2)
        counter2 = counter2 + 1
    counter1 = counter1 + 2
    counter2 = 1


