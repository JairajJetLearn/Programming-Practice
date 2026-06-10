import random

#Create a program to ask for the marks of 5 subjects (for example English, Math, Science, Computer Science, and Arts).
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

#Write a Python program that asks each person in the group how much they are
#paying towards the meal and works out when the bill is fully paid. Each person can
#pay a different amount.

#The program should:
#get the user to enter the total amount of the bill
#get a person to enter how much they are paying towards the bill
#subtract the amount entered from the bill
#if the amount left to pay is more than 0, output how much is left to pay and repeat until the amount left to pay is 0 or less
#if the amount left to pay is 0, then output the message Bill paid
#if the amount left to pay is less than 0, then output the message Tip is and the difference between the amount left to pay and 0


total = float(input("What's the total bill"))

while total > 0:
    amount = float(input("How much are you paying to the bill"))
    total = total - amount
    print(total)
    if total == 0:
        print("Bill paid")
    elif total < 0:
        print("Tip is", -total)

#One ride in Fun Kingdom has a minimum height of 135 cm to ride alone or 115cm to ride with an adult.

#Write a Python program that:
#asks the user to input the height of the rider, in centimetres
#if needed, asks if they are riding with an adult
#outputs whether or not they are allowed to ride
#repeats this process until 8 people have been allowed to ride.
counter = 0

while counter < 9:
    height = int(input("Height in cm:"))
    if height < 136:
        adult = input("Are you riding with an adult")
        if adult == "yes" or adult == "Yes":
            print("You can ride")
            counter = counter + 1
        else:
            print("You can't ride")
    elif height > 135:
        print("You can ride")
        counter = counter + 1

Q. Write a program to take ten numbers as input from the user and add it to a list. Calculate and print the sum of all the numbers in the list.
Q. Write a Python program to check if a list is empty or not.
Q. Write a Python program to print the odd numbers from a list of numbers.


list = []
for i in range(10):
    num = int(input())
    list.append(num)

#print(sum(list))

sum = 0

for num in list:
    print(num)
    sum = sum + num

print(sum)

# 5 teams

teams = []
scores = []

for i in range(5):
    teamName = input("team name:")
    score = int(input("score:"))
    teams.append(teamName)
    scores.append(score)

print(teams)
print(scores)

winnerTeam = teams[0]
highScore = scores[0]

totalscore = 0
for score in scores:
    totalscore += score
print(totalscore)

for i in range(len(scores)):
    if scores[i] > highScore:
        highScore = scores[i]
        winnerTeam = teams[i]

print("Winner team is", winnerTeam)
print("highScore is", highScore)

if len(list) == 0:
    print("list is empty")

lis = [2,3,4,5,6,7,8,9]

for i in lis:
    if i % 2 != 0:
        print(i)

Create a two-dimensional array scores of 3 players score in 4 rounds and retrieve a few values using indexing.

score = [[12,14,15,13], [14,13,19,12], [19,11,15,17]]

print(score[2][3])
print(score[1][2])

for row in score:
    for item in row:
        print(item)
    # for j in score[0]:
    #     print[i][j]

for i in range(len(score)):
    for j in range(len(score[0])):
        print(score[i][j])

largest = score[0][0]
smallest = score[0][0]

for i in range(len(score)):
    for j in range(len(score[0])):
        if score[i][j] > largest:
            largest = score[i][j]
        elif score [i][j] < smallest:
            smallest = score[i][j]

print(largest,smallest)

numbers = []
total = 0

for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)

for number in numbers:
    total = total + number

print("Sum =", total)

list = []

if len(list) == 0:
    print("The list is empty")
else:
    print("The list is not empty")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number % 2 != 0:
        print(number)









#prompt the user to enter how many tickets they would like and take this value as input
#output "tickets booked" and reduce the value stored in tickets if there are enough tickets available
#output "not enough tickets" if there are not enough tickets available
#repeat the steps until there are no tickets left

tickets = 500
tickets_booked = 0
while tickets > 0:
    num_tickets = int(input("HOw many tickets would you like"))
    tickets_booked = tickets_booked + num_tickets
    print("Tickets booked: ", tickets_booked)
    tickets = tickets - tickets_booked
    if tickets_booked > 500:
        print("Not enough tickets")




tiles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]

for i in range (46):
    if tiles[i + 1] == tiles[i] + 1 and tiles[i + 2] == tiles[i + 1] + 1 and tiles[i + 3] == tiles[i + 2] + 1 and tiles[i + 4] == tiles[i + 3] + 1:
        print("valid run")
    else:
        print("invalid run")

def get_day(day):
    if day == 0:
        return("Monday")
    elif day == 1:
        return("Tuesday")
    elif day == 2:
        return("Wednesday")
    elif day == 3:
        return("Thursday")
    elif day == 4:
        return("Friday")
    else:
        return("Invalid input")

DOW = get_day(6)

print(DOW)

#Create a project using random module that generates strong password.

#The password should be 8 characters long with 3 digits,  3 letters and 2 special characters.

alphabet = "abcdefghijklmnopqrstuvwxyz"
digits = "1234567890"
sc = "!£$%&*@?"

a = random.choice(alphabet)
b = random.choice(alphabet)
c = random.choice(alphabet)
d = random.choice(digits)
e = random.choice(digits)
f = random.choice(digits)
g = random.choice(sc)
h = random.choice(sc)

password = a + b + c + d + e + f + g + h
print(password)

#Create a rock, paper, scissors game. The player picks one of the three objects and the computer randomly picks one of the three objects. Then these rules are applied to see who has won that round:
#Paper wraps (beats) Rock
#Scissors cut (beat) Paper
#Rock blunts (beats) Scissors
#Repeat it to have 3 rounds.
#Add score to the game.
#Declare the final winner.

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

for i in range(3):
    player = input("Choose rock, paper or scissors")
    computer = random.choice(choices)

    print("The computer chose:", computer)

    if computer == player:
        print("Its a draw")
    elif computer == "rock" and player == "scissors":
        print("Computer wins this round")
        computer_score += 1
    elif computer == "rock" and player == "paper":
        print("You won this round")
        player_score += 1
    elif computer == "scissors" and player == "rock":
        print("You won this round")
        player_score += 1
    elif computer == "scissors" and player == "paper":
        print("Computer wins this round")
        computer_score += 1
    elif computer == "paper" and player == "rock":
        print("Computer wins this round")
        computer_score += 1
    elif computer == "paper" and player == "scissors":
        print("You won this round")
        player_score += 1
    else:
        print("Invalid Choice")

    print("Player:", player_score)
    print("Computer:", computer_score)

print("Final Scores:")
print("Player:", player_score)
print("Computer:", computer_score)

if computer_score > player_score:
    print("The Computer wins!")
elif player_score > computer_score:
    print("You win!")
else:
    print("It's a draw")

#Define the area of a square

def area(x,y):
    return(x*y)

square = area(5,5)
print(square)

#Define the area of a circle

pi = 3.141529

def circle(x):
    return(x**2*pi)

area_circle = circle(7)
print(area_circle)










