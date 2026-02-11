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


