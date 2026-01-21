#Q. Write a program to take input for 2 numbers and print their sum.
#Q. Write a program to take input for 2 numbers and print their difference.

num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
print(num1 + num2)

#Write a program to take input for the length and the height of a rectangle.Calculate and print the perimeter and area of the rectangle.

length = int(input("Enter the length of the rectangle"))
width = int(input("Enter the width of the rectangle"))

perimeter = (length*2) + (width*2)
area = length*width

print(perimeter, area)

#Q. Ask the user to enter their first name and last name.
#Construct the full name and display it
#Fetch and display the initials 
#Find the length of the name
#Generate a username in lowercase by joining the first 3 letters of the first name and the first letter of the last name

fname = input("Enter your first name")
lname = input("Enter your last name")
fullname = fname + " " + lname
print(fullname)

initial1 = fname[0]
initial2 = lname[0]
print(initial1 + initial2)

username = fname[0:3] + lname[0]
print(username)

name_length = len(fname) + len(lname)
print(name_length)

#Q.Create a program to ask for the marks of 3 subjects (for example- English, Math, Science, Computer Science, and Arts).
#Calculate and print the total marks and average(mean) of the marks.


Emarks = float(input("What marks did you get in English?"))
Mmarks = float(input("What marks did you get in Maths?"))
Smarks = float(input("What marks did you get in Science?"))

total = Emarks + Mmarks + Smarks
average = total/3
print(average)
