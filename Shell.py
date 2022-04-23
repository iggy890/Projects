"""
t = "h"
if t == "t":
    print("The t value has a value of t")
elif t == "g":
    print("The t value has a value of g")
elif t == "g":
    print("The t value has a value of g")
elif t == "h":
    print("The t value has a value of g")
else:
    print("")

q = int(input("Enter a number"))
if q == 1:
    print("Monday")
elif q == 2:
    print("Tuesday")
elif q == 3:
    print("Wednesday")
elif q == 4:
    print("Thursday")
elif q == 5:
    print("Friday")
elif q == 6:
    print("Saturday")
elif q == 7:
    print("Sunday")
else:
    print("Number out of 1-7")

q = int(input("Enter a number"))
if q % 2 == 0:
    print("Even number")
else:
    print("Odd number")

q2 = int(input("Enter a 3-Digit Number: "))
if q2 >= 100:
    if q2 % 3 == 0:
        print("Divisible by 3")
    else:
        print("Not Divisble by 3")
q3 = int(input("Enter a number: "))
q4 = int(input("Enter a number: "))
q5 = int(input("Enter a number: "))
if not q3 == q4 and not q3 == q5:
    print("Integers are unique.")
else:
    print("Integers are not unique.")
    
days = int(input("How many days will you be at the hotel: "))
daycost = 75
dayfoodcost = int(input("Daily food cost: "))
activitycost = int(input("How much will the activities cost: "))
totalcost = (dayfoodcost+activitycost+daycost)*days
print("Total cost: {}$".format(totalcost))

height = int(input("Please enter your height (only numbers)"))
weight = int(input("Please enter your weight (only numbers)"))
bmi = weight / (height ** 2)
print("Your BMI is: {}.".format(bmi))

q = input("Enter a 2-digit or 3-digit number")

if q >= 10 and q <= 99:
    print("2-digit number")
elif q >= 100 and q <= 999:
    print("3-digit number")
else:
    print("Out of range.")

num = int(input("Enter a number: "))
num1 = int(input("Enter a number: "))

if num % 7 == 0 and num1 % 7 == 0:
    print("Both multiples of 7")
else:
    print("Not multiples of 7")

num = int(input("Enter a number: "))

if num >= 100 and num <= 999:
    if num % 3 == 0:
        print("3-digit number divisible by 3")
    else:
        print("3-digit")
else:
    print("Not 3-digit")
    
cre = int(input("How many credits do you have: "))

if cre >= 120:
    print("You have enough credits to graduate!")
else:
    print("You don't have enough credits to graduate. :(")

price=int(input("Enter price: "))

if price >= 2000:
    print(price/5)
elif price >= 2001 and price <= 5000:
    print(price/25)
elif price >= 5001 and price <= 10000:
    print(price/35)
elif price > 10000:
    print(price/50)
else:
    print(price)

marks = int(input("Enter you marks: "))

if marks >= 90 and marks <= 100:
    print("You got an A!")
elif marks >= 70 and marks <= 89:
    print("You got a B!")
elif marks >= 50 and marks <= 69:
    print("You got a C.")
elif marks > 30 and marks <= 49:
    print("You got a D.")
elif marks <= 30:
    print("You got an F :(")
else:
    print("Invalid value: {}(out of range)".format(marks))

price=int(input("Enter price: "))

if price <= 2000:
    dsc = 5
elif price >= 2001 and price <= 5000:
    dsc = 25
elif price >= 5001 and price <= 10000:
    dsc = 35
elif price > 10000:
    dsc = 50
final = price-(price*(dsc/100))
print("You will pay {} pounds".format())

energy = int(input("Enter how much energy you use: "))
if energy <= 100:
    cost = 2
elif energy > 100 and energy <= 200:
    cost = 1.8
elif energy > 200:
    cost = 1.5

print("You will pay: {} pounds in energy bills".format(price))

days = int(input("How many days have you taken your book out of the library? "))

if days >= 5:
    cost = 40
elif days >= 6 and days <= 10:
    cost = 65
elif days > 10:
    cost = 80
    
final = days*cost/100
print("You will have to pay: {} pound(s)".format(final))

num = int(input("Enter a number: "))

if num >= 10000 and num <= 99999:
    print("Number is 5-digit")
    divided=num//100
    print("Middle digit is: {}.".format(divided%10))
else:
    print("Number is not 5-digit :(")

num0 = int(input("Enter a number:"))
if num0 >= 1000 and num0 < 10000:
    print("4-digit Number.")
    firstdigit = num0//1000
    lst = num0//10*10
    lst2 = num0
    lastdigit = lst2 - lst
    print("Sum of first and last digits {}.".format(firstdigit+lastdigit))
else:
    print("Not a 4-digit number.")
num1 = int(input("Enter another number: "))
if num1 >= 100 and num1 < 1000:
    firstdigit = num1//100
    lst = num1//10*10
    lst2 = num1
    lastdigit = lst2 - lst
    su = firstdigit+lastdigit
    if su % 2 == 0:
        print("Sum of first and last digits is even.")
    else:
        print("Sum is not even.")
else:
    print("Number is not 3-digit")

waterconsumed = int(input("How many gallons of water do you use? "))

if waterconsumed <= 45:
    tax = 1
elif waterconsumed > 45 and waterconsumed <= 75:
    tax = 475
elif waterconsumed > 75 and  waterconsumed <= 125:
    tax = 750
elif waterconsumed > 125 and waterconsumed <= 125:
    tax = 1125
elif waterconsumed > 200 and waterconsumed <= 350:
    tax = 1650
else:
    tax = 2000

print("You have to pay {} in water taxes.".format(waterconsumed/100*tax))

import os
def getdirs(directory):
    sub_folders = {}
    for dir, files, sub_dirs in os.walk(str(directory)):
        sub_folders[str(dir)] = str(files)
    return sub_folders
results = getdirs()
print(results)
q = input("search dirs")
values = []
def searchdict(search,lib)
    values = []
    showtext = ""
    found = False
    for value in lib.values():
        low = value.lower()
        if q.find(value):
            if not value in values:
                values.append(value)
                found=True
        if q.find(low):
            if not value in values:
                values.append(value)
                found=True
      if not found:
          return ()
print(values)

age = int(input("What's your age? "))                                                                              
print("That's cool.")

itemsinstock = ["BrickStock","AppleStock","PlaneStock"]
order = input("What are you going to buy? ")
if order in itemsinstock:
    num = int(input("How many are you going to buy? "))
    if 100-num < 0:
        itemsinstock.remove(order)
        print("Sorry, we only have 100 {}' in store we will dispatch and deliver you all the ones avaliable and will deliver the rest when {} is in stock.".format(order,order))
    else:
        print("Dispatching order... {} left...".format(100-num))
else:
    print("Sorry we dont seem to have {}.".format(order))

answer = "Moscow"
ans = input("What is the capital of Russia? ")
if ans == answer:
    print("Correct!")
else:
    print("Oops, incorrect here is a clue: ")
    ans = input("Here is a clue: It has a famous Colorful Cathedral: ")
    if ans == answer:
        print("Correct!")
    else:
        print("Oops, here is another clue: ")
        ans = input("It is in the west of the country: ")
        if ans == answer:
            print("Correct!!!")
        else:
            print("Sorry, last chance and last clue: ")
            ans = input("Some of it's roads are made of bricks: ")
            if ans == answer:
                print("Correct, just in time.")
            else:
                print("You lose :(")

stock = 100
num = int(input("How many are you going to buy"))
if num > stock:
    print("Unfortunately we only have {} items in stock, (you ordered {} items) we will dispatch you the rest of the items ({}) when they are availble ".format(stock,num,num-stock))
    stock = 0
    print("{} items left in stock.".format(stock))
else:
    print("Thanks for buying our products! We will dispatch and deliver you {} item(s).".format(num))
    stock = stock-num
    print("{} item(s) left in stock.".format(stock))

# Print the sum of all the even and odd numbers from 20,50

even = 0
odd = 0
for i in range(20,50):
    if i % 2 == 0:
        even+=i
    else:
        odd+=i
print("Sum of all the even numbers from 20 to 50 {}, all the odd numbers {}.".format(even,odd))

# Write a program to print the sum of all the 3 digits divisible by 5
su = 0
for i in range(100,1000):
    if i % 5 == 0:
        su+=i

print("The sum of all the 3 digit numbers divisible by 5: {}.".format(su))
num = int(input("Enter a number: "))
total = 1
for i in range(num,0,-1):
    total*=i
    
print(total)

##Write a program to find factors of a given number
##Write a program to check if a given number is prime or not
##WAP to find number of factors of a number

# Factors Code
num = int(input("Enter a number: "))
factors = []
for i in range(1,num):
    if num % i == 0:
        factors.append(i)
        
print("All the factors of {}: {}.".format(num,factors))

#Prime Code
num = int(input("Enter another number: "))
factornum = 0
for i in range(1,num):
    if num % i == 0:
        factornum += 1

if factornum > 1:
    print("Number {} is not prime.".format(num))
else:
    print("Number {} is prime.".format(num))

#Number of factors code
num = int(input("Enter another number (this is the last time I'm asking you :) ): "))
factornum = 0
for i in range(1,num):
    if num % i == 0:
        factornum += 1

print("There are {} factors of {}".format(factornum,num))

num = int(input("Enter a number: "))
largest=smallest=num
for i in range(0,10):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num
print(largest)
print(smallest)

#WAP to input 10 integers and display the largest even and smallest odd integer
#WAP to input 10 integers and find the sum of 2-digit and 3-digit numbers seperately
num1 = int(input("Enter a Number: "))
largest=smallest=num1
for i in range(0,1):
    num = int(input("Enter a Number: "))
    if num > largest and num % 2 == 0:
        largest = num
    elif num < smallest and not num % 2 == 0:
        smallest = num
print("Largest even number: {}, Smallest odd number: {}.".format(largest,smallest))

sum1 = 0
sum2 = 0
for i in range(0,5):
    num = int(input("Enter a number: "))
    if num >= 10 and num > 100:
        sum1+=num
    elif num >= 100 and num <= 1000:
        sum2+=num
print("The sum of all the 2-digit numbers: {}, All the 3-digit numbers: {}".format(sum1,sum2))

#WAP to take 10 integer inputs from the user and print and display "EVEN" if all the number are even else: print "NOT EVEN"
even = True
for i in range(1,10):
    num = int(input("Enter a number: "))
    if  num % 2 != 0:
        even = False
if even:
    print("Even")
else:
    print("Not even")

#WAP to take 5 integer inputs from the user if all the numbers are same then print same else: not same
num = int(input("Enter a number: ")) 
same = True

for i in range(1,4):
    num1 = int(input("Enter a number: "))
    if num != num1:
        same = False


if same:
    print("Same")
else:
    print("Not same")

#WAP to take 10 integers from the user and check if they are in ascending order or not
start = int(input("Enter a number: "))
ascending = True
for i in range(1,10):
    num = int(input("Enter a number: "))
    if num != start+1 and ascending:
        ascending = False
    start = num

if ascending:
    print("Ascending")
else:
    print("Not ascending")

#1*2+3*4+5*6+7*8+9*10

1*2
3*4
5*6
7*8
9*10

total = 0
for i in range(1,10,2):
    total += i * (i - 1)
    print("{} * {} + ".format(i,i+1),end='')

print("\nSum of the series: {}".format(total))

total1 = 0
for i in range(1,10):
    total1 += i / (i + 1)
    print("{} / {} + ".format(i,i+1),end='')

print("\nSum of the series: {}".format(total))

total = 0
n = int(input("Enter a number: "))
x = int(input("Enter another number: "))
for i in range(1,n,2):
    total += x ** i / i + 1
    print("{} / {} /".format(i,i+1),end='')
print("\nTotal: {}.".format(total))

#S = x/2 + (x^2)/3 + (x^3)/4 +  + (x^n)/n+1

import matplotlib.pyplot as plt
import numpy as np

amplifier = 500

def noise(x,y):
    num = np.random.normal(x,y)
    if num > 0.5:
        num = 0.5
    elif num < -0.5:
        num = -0.5
    return num

def fractalNoise(x,y):
    y1 = noise(x, y) * amplifier
    y2 = noise(x, y) * amplifier + amplifier / 2
    y3 = noise(x, y) * amplifier + amplifier
    return y1 + y2 / 2 + y3 / 6

#S = x/2 + (x^2)/3 + (x^3)/4 +  + (x^n)/n+1
x = int(input("Enter a number: "))
n = int(input("Enter another Number: "))
total = 0
for i in range(1,11):
    total += (x ** i) / i + 1
    print("{} ** {} / {} + 1".format(x,i,i))
# x / 2 in the form of x ** n
print("Total: {}.".format(total))

# Write a series for x ** i / i - 1
x = int(input("Enter a number: "))
total = 0

for i in range(1,11):
    total += (x ** (i + 1)) / i
    print("({} ** ({})) / {} ".format(x,i+1,i))

print("Total: {}.".format(total))

# Fibonacci Series: 0 , 1, 1, 2, 3 ,5 ,8 , 13 , 21 ...
# lastnum + num = newnum
# 0 * 1.6
a = 0
b = 1
print(a,"\n" + str(b))
for i in range(1,100):
    c = a + b
    a = b
    b = c
    print(c)

# Tribonacci Series : 0, 1, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, etc
# 2ndlastnum + lastnum + num = newnum
a = 0
b = 1
c = 1
d = 0
print(a)
print(b)
print(c)
for i in range(0,7):
    d = a + b + c
    a = b
    b = c
    c = d
    print(d)

a = 1
b = 2
c = 5
d = 0
for i in range(0,10):
    d = (a + b + c) * 2
    a = b
    b = c
    c = d
    print(d)

b = 1
c = 2
d = 0

print(1)
print(2)

for i in range(0,15):
    d = (c) * 2 + b
    b = c
    c = d
    print(d)

Write a program to print the first 15 numbers of the Pell series.
Pell series is a series which starts from 1 and 2 and subsequent 
number are the sum of twice the previous number and the number 
previous to the previous number.
Pell series: 1,2,5,12,12,29,70,169,408,985,2378,5471,13860

Write a program to find the sum of 1st 10 numbers of Lucas series 
i.e., 2,1,3,4,7,11,18,.... Lucas series is such a series which starts 
from 2 and 1, and subsequent numbers are the sum of the previous two numbers

# Lucas Series
a = 2
b = 1
c = 0

print(2,end=', ')
print(1,end=', ')

for i in range(0, 10):
    c = a + b
    a = b
    b = c
    print(c,end=', ')

# WAP to check if the two numbers amicable and 
# Amicable: sum of factors of first number is equal to second number and Vice Versa




num = 1210
num2 = 1184

def amicable(num, num2):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    if total == num2:
        return True
    else:
        return False


if amicable(num, num2):
    print("True")
else:
    print("False")

# WAP to take a number as an input from the user and check if it is Palendrome or not
# Palendrome number: If the reverse of the number is equal to the number 
# EG: num = 1221 
# Output: Palendrome
# EG: num = 1234
# Output: Not Palendrome
num = int(input("Enter a number:"))
num2 = num
next = 0

while num > 0:
    rem = num % 10
    next = next * 10 + rem
    num //= 10

if num2 == next:
    print("Palendrome")
else:
    print("Not Palendrome")

# WAP to check if a number is an Armstrong Number
# Armstrong Number: The sum of the cube of each digit of a number should be equal to the last digit in the number
num = int(input("Enter a number: "))
num2 = num
last = num - (num // 10 * 10)
total = 0

while num > 0:
    mod = num % 10
    num //= 10
    total += (mod ** last)

if total == num2:
    print("Armstrong")
else:
    print("Not Armstrong")

# Homework: get all the armstrong number from 1-1000 (can use for loop)
for i in range(1,1000):
    num = i
    num2 = num
    last = num - (num // 10 * 10)
    total = 0

    while num > 0:
        mod = num % 10
        num //= 10
        total += (mod ** last)

    if total == num2:
        print("Armstrong: {}".format(total))

def getDays():
    day1 = input("When do you have a lesson?")
    if day1 == "Wednesday":
        print("Ok...")
    elif day1 == "Saturday":
        print("Whoops, you have a lesson right now")
    day2 = input("Do you have another lesson")
    if day2 == "Wednesday":
        print("Ok...")
    elif day2 == "Saturday":
        print("You have a lesson right now!")
getDays()
def attendedLesson():
    at = input("Have you attended todays lesson? ")
    if at == "Yes":
        print("Good Job!")
    else:
        print("You are going to have to right an apology to your teacher...")
        ap = input("Enter your apology for your teacher: ")
        ap2 = input("Enter an apology for your dad: ")
attendedLesson()

# Create a pattern
for x in range(0,5):
    for z in range(0, 5):
        print("*",end=' ')
    print("\n")

# Create a triangle
for x in range(0, 5):
    for z in range(0, x + 1): 
        print("*",end=' ')
    print("\n")

num = 5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
continues with an input

Try pyramid and Right-Angled Triangle


max = int(input("Enter a number: "))
for x in range(1, max + 1):
    for z in range(0, x): 
        print(x, end=' ')
    print("\n")

max = int(input("Enter a number: "))
for x in range(1, max + 2):
    for z in range(x, 1, -1):
        print("*",end=' ')
    print("\n")

max = int(input("Enter a number: "))
for y in range(0, max // 2):
    for x in range(0, y + 1):
        print("*",end=' ')
    print("\n")
for y in range(0, max // 2):
    for x in range(max // 2, y, -1):
        print("*",end=' ')
    print("\n")

Create the same thing but with 1,2,3,4,5
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
try 
/ |
___



max = int(input("Enter a number: ")) * 2
val = 0

for y in range(0, max // 2):
    val += 1
    for x in range(0, y + 1):
        print(val, end=' ')
    print("\n")


for y in range(1, max // 2):
    val -= 1
    for x in range(max // 2, y, -1):
        print(val, end=' ')
    print("\n")

max = 5

for y in range(0, max):
    for x in range(0, y * 2):
        print(end=' ')
    for x in range(y):
        print("*",end='')
    print("\n")

y:
*
*
*
*
*
x and y:
spaces = max - numberof*
1
5-1 = 4
5-2 = 3
5-3 = 2
    * 8 
   ** 6
  *** 4
 **** 2
/ |
___


for y in range(0, 8, 2):
    spaces = 8 - y 
    num = y + 1

    for x in range(spaces):
        print(end=' ')

    for x in range(num):
        print("*",end='')
    
    print("\n")

# Create a Pyramid

max = int(input("Enter a number: ")) + 1
val = max


for y in range(max):
    for x in range(val):
        print(end=' ')
    
    for x in range(y):
        print("*",end=' ')
    
    print("\n")
    val -= 1

# Create a Diamond Shape
max = int(input("Enter a number: ")) + 1 * 2


for y in range(max // 2):
    for x in range(max - y - 1):
        print(end=' ')
    
    for x in range(y):
        print("*",end=' ')
    
    print("\n")

for y in range(max // 2, max):
    for x in range(y):
        print(end=' ')
    
    for x in range(max - y - 1):
        print("*",end=' ')
    
    print("\n")

Try
*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********

max = int(input("Enter a number: "))

for y in range(max - 1):
    for x in range(y + 1):
        print(end=' ')
    
    for x in range(max - y):
        print("*",end=' ')

    print("\n")

for y in range(max):
    for x in range(max - y):
        print(end=' ')
    
    for x in range(y + 1):
        print("*",end=' ')
    
    print("\n")

max = int(input("Enter a number: ")) + 1

for y in range(max):
    for x in range(y):
        print(y, end=' ')
    print("\n")

max = int(input("Enter a number: ")) + 1

for y in range(1, max):
    for x in range(max - y):
        print(y, end=' ')
    print("\n")

max = int(input("Enter a number: ")) + 1

for y in range(1, max):
    for x in range(y, 0, -1):
        print(x, end=' ')
    print("\n")

Try

1

3 2

6 5 4

10 9 8 7

1 

1 2 1 

1 2 3 2 1 

1 2 3 4 3 2 1 

1 2 3 4 5 4 3 2 1

           1 

         1 2 

      1 2 3 

   1 2 3 4 

 1 2 3 4 5

         1 

        1 2 

    1 2 3 

   1 2 3 4 

 1 2 3 4 5

1

2 3 4

5 6 7 8 9
max = int(input("Enter a number: "))

for y in range(0, max):
    spaces = max - y 
    num = y + 1

    for x in range(spaces):
        print(end=' ')

    for x in range(1, num + 1):
        print(x,end='')
    
    print("\n")

1

2 3 4

5 6 7 8 9



max = int(input("Enter a number: "))
count = 1
stop = 2

for y in range(1, max + 1, 2):
    for x in range(1, stop):
        print(count, end=' ')
        count += 1

    print("\n")
    stop += 2

max = int(input("Enter a number: ")) + 1

for y in range(max):
    for x in range(1, y + 1):
        print(x, end=' ')

    for z in range(y - 1, 0, -1):
        print(z, end=' ')

    print("\n")
    

max = int(input("Enter a number: "))
val = max + 1

for y in range(max, 2, -1):
    for x in range(val - y, max):
        print(x, end=' ')

    for z in range(val - y, max, - 1):
        print(z, end=' ')
    
    print("\n")
    val += 1

import random

for y in range(1, 11):
    for x in range(y):
        print(random.randint(x,11), end=' ')
    print("\n")

num = 1
def myfunc():
    return num
print(num) # 1
print(myfunc()) # 1
print(num) #1


num = 1
def myfunc():
    num = 10
    return num
print(num) # 1
print(myfunc()) # 10
print(num) # 10

num = 1
def myfunc ():
    global num
    num = 10
    return num
print (num) # 1
print(myfunc()) # 10
print(num) # 10


def display():
    print("Hello", end = ' ')
display() # Hello
print("there!") # there!

Q26. Write a Python function to calculate the factorial of a 
number (a non-negative integer). The function accepts the number 
whose factorial is to be calculated as the argument.





Q27. Write a Python function that takes a number as a parameter 
and checks whether the number is prime or not.

# Q.26
def factorial(num):
    num = int(num)
    if num < 0:
        num = -num

    return num

print(factorial(-10))

# Q.27
def prime(num):
    val = False

    for i in range(2, num):

        if not num % i == 0:
            val = False

            break

    return val

print(prime(1))

Create a function to enter a string as an argument and check whether the string is palendrome or not
123454321


def palendrome(string):
    half1 = ""
    half2 = ""

    for i in range(len(string) // 2):
        half1 = (half1 + string[i])

    for i in range(len(string), len(string) // 2, -1):
        half2 = (half2 + string[i])

    return half1 == half2

print(palendrome("1221"))


def palendrome(string):
    return string == string[::-1]
     
print(palendrome("1221"))

Check if a given number falls in a given range

def numInRange(num, min, max):
    for i in range(min, max + 1):
        if num == i:
            return True

    return False

print(numInRange(10, 1, 10))

Write a Python function to check whether a number is perfect or not. Go to the editor
According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of 
its proper positive divisors, that is, the sum of its positive divisors excluding the number itself 
(also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of 
its positive divisors (including itself).
Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, 
and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: 
( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 
1 + 2 + 4 + 7 + 14. 
This is followed by the perfect 
numbers 496 and 8128.


def perfect(num):
    sum = 0
    for i in range(1, num - 1):
        if num % i == 0:
            sum += i
    
    return num == sum

print(perfect(8128))

# Write a function to take in a number as argument and check if the cube of each digit sums up to be equal to the orginal number
# Example: 153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3 = 153

# Power is equal to number of digits in the inputted number

def digits(num):
    digits = 0

    while num > 0:
        digits += 1
        num //= 10

    return digits

def armstrong(num):

    power = digits(num)

    sum = 0

    num2 = num

    while num > 0:
        rem = num % 10

        sum += rem ** power

        num //= 10

    return sum == num2


for i in range(10, 100000000):
    if armstrong(i):
        print("Number {} is armstrong.".format(i))

# WAP to take marks of a student for 5 subjects as user input
# And display the grades A B C D E F based on the mark 
# Create a function that will return the grades as for the marking schemer
# Create another function "average" that will calculate the average
# Last: The grades according to marks in each subject seperately
# The Final grade will be the average marks

subjects = ["Maths", "English", "Science", "French", "Physics"]

def avg(sum):
    return sum / 5

def grade(mark):
    if mark > 90:
        return "A"
    elif mark > 85:
        return "B"
    elif mark > 75:
        return "C"
    elif mark > 70:
        return "D"
    elif mark > 65:
        return "E"
    else:
        return "F"

def markingScheme():
    print("\n")

    print("Marking Scheme: \n >90 A \n >85 B \n >75 C \n >70 D \n >65 E \n Else F.")
    print("\n")

def finalGrade(marks):
    sum = 0
    for i in marks:
        sum += i
    
    average = avg(sum)
    grades = grade(average)

    print("You got a final grade is {} the average mark was {} / 100 marks.".format(grades, average))

def marksOutput(subjects, marks):
    for i in range(5):
        subject = subjects[i]
        mark = marks[i]
        grades = grade(mark)

        print("You got an {} in {}. Mark: {}.".format(grades, subject, mark))

def getMarks():
    marks = []

    for i in subjects:
        mark = int(input("How many marks did you get in {}: ".format(i)))
        marks.append(mark)
    
    print("\n")

    return marks

def main():
    marks = getMarks()
    marksOutput(subjects, marks)

    markingScheme()

    finalGrade(marks)

main()

# Homework: Output marks in a table
subjects = ["Maths", "English", "Science", "French", "Physics"]

def avg(sum):
    return sum / 5

def finalGrade(marks):
    sum = 0
    for i in marks:
        sum += i
    
    average = avg(sum)

    print("Average Mark:\t\t{}".format(average))

def marksOutput(subjects, marks):
    for i in range(5):
        subject = subjects[i]
        mark = marks[i]

        print("{}\t{}".format(subject, mark))

def getMarks():
    marks = []

    for i in subjects:
        mark = int(input("How many marks did you get in {}: ".format(i)))
        marks.append(mark)
    
    print("\n")

    return marks

def main():
    marks = getMarks()
    marksOutput(subjects, marks)


    finalGrade(marks)

main()

# Create a program for a coffee shop
# Brew Ratio: the yield of the coffee divided by dose
# Based on the Brew Ratio, determine the style of coffee
# 1:1.5 - 1:2.5 Normal Coffee, 1:1 - 1:1.5 Ristretto, 1:2.5+ Lungo
# First digit = Dose, Second digit = yield
# Customer: Inputs coffee type and amount of coffee

def main():
    typeCoffee = input("What type of coffee do you want?")
    amount = int(input("How much coffee do you want?"))

    y = 0
    dose = amount

    if typeCoffee == "Normal":
        y = dose
    elif typeCoffee == "Ristretto":
        y = dose + (dose / 4)
    elif typeCoffee == "Lungo":
        y = (dose * 2) + (dose / 2)
    else:
        print("Unfortunately, we do not have that type of coffee.")

        return 0

    print("Yield: {}. \nDose: {}.".format(y, dose))

main()

def add(n):
    if (n == 0):
        return n

    return n + add(n - 1)

print(add(10))

# Factorial: the multiplication of all non-negative / non-zero numbers below it

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

def factorial2(num):
    s = 1

    for i in range(num, 1, -1):
        s *= i

    return s


s = time.time()
factorial(999)
e = time.time()
print("Recursive factorial took {} seconds.".format(e - s))

start = time.time()
factorial2(990)
end = time.time()
print("For loop factorial took {} seconds.".format(end - start))

# Find the sum of all the the integers in an inputted list
times = int(input("How many list items do you want to add? "))

s = 0

def main(num):
    global s
    if num == 0:
        return s
    
    i = int(input("Enter a number: "))
    s += i

    main(num - 1)

print(main(times))

# Find the sum of the list recursively in a nested list
# e.g [1, 2, [3,4], [5,6]]
# Output: 21
# Check if the element is list or a number 
# e.g [1, 2, [3,4], [5,6]]
# Check value position 0 in list
# Position 0 is a number


li = [1, 2, 3, 4, 5]

sum = 0
def listLoop(num, l):
    global sum

    if num == -1:
        return sum

    sum += l[num]

    return listLoop(num - 1, l)

print(listLoop(len(li) - 1, li))


l = [1, [2, 3], 3, 4, [5, 6]]
val = int(input("Enter a number: "))

def check(num):
    try:
        t = type(l[num])
    except IndexError:
        return ("Position {} does not exist.".format(num))

    if t == int:
        return ("Position {} is a number.".format(num))
    elif t == list:
        return ("Position {} is a number.".format(num))

print(check(val))

l1 = [1, 2, 3, 4, 5, 6]
li = [1, 2, [3,4], [5]]

def getSum(l):
    sum = 0

    for i in l:
        if type(i) == list:
            for j in i:
                sum += j
        else:
            sum += i

    return sum

print(getSum(li))

l1 = [1, 2, 3, 4, 5, 6]
li = [1, 2, [3,4], [5,6]]

sum = 0
def recursiveSum(num, l):
    global sum

    t = type(l[num])

    if num == -1:
        return sum

    if t == list:
        print("h")
        raise ("List detected: Exit code 1")
        return 1
    else: 
        sum += l[num]

        return recursiveSum(num - 1, l)

print(recursiveSum(len(li) - 1, li))

numbers = [1,2,[3,[7,[8,4],9],10],[5,6]]

def recursiveSum(numbers):
    s = 0
    for element in numbers:
        if type(element) == list:
            s = s + recursiveSum(element)
        else:
            s = s + element
    return s
print(recursiveSum(numbers))

# All of the following with recursion
# Find the greatest common divisor: with recursion
# Reverse a string with recursion: Must do
# Most common multiplier

String = str(input("Enter some text: "))

def invertString(num, returnString, string):
    if num == -1:
        return returnString

    returnString = (returnString  + string[num])

    return invertString(num - 1, returnString, string)

print(invertString(len(String) - 1, "", String))

 
def LCM(num, num2):
    for i in range(2, num):
        if num % i == 0 and num2 % i == 0:
            return i

print(LCM(100, 50))

def LCM(num, num2):
    i = 2
    while num2 >= i:
        if num % i == 0 and num2 % i == 0:
            return i
    
    i += 1

    raise ValueError

print(LCM(20, 4))

# Learn how LCM and GCD works (mathmatically)
# LCM 10, 6
# 10: 10, 20, 30, 40, 50, 60
# 6: 6, 12, 18, 24, 30, 36, 42, 60
# GCD 100, 70
# 100 = 70 * 1 + 30
# 70 = 30 * 2 + 10
# 30 = 10 * 3 + 0
# GCD = 10

l = []
l2 = []  

def min(num, num2):
    if num <= num2:
        return num
    else:
        return num2


def LCM(num, num2, depth):
    global l
    global l2

    for i in range(min(num, num2), depth):
        l.append(num * i)
        l2.append(num2 * i)

    for i in range(len(l)):
        li1 = l[i]
        for j in range(len(l)):
            li2 = l2[j]
            if li1 == li2:
                return li2
    
    return LCM(num, num2, depth + 50)

print(LCM(10, 6, 10))

def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    i=1
    while True:
        i+=1
        if (greater%x==0 and greater%y==0):
            multiplier=greater
            break
        greater+=1
    return multiplier
print(lcm(10,6))



def GCD(x, y):
    i = 1

    while True:
        i += 1
        if (i % x == 0 and i % y == 0):
            return i

print(GCD(10, 6))

def GCD(x,y):
    if x<y:
        small=x
    else:
        small=y
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            gcd=i
    return gcd
    
print(GCD(60,48))

# LCM (Lowest Common Multiplier)

def lcm(x, y):

    if x > y:
       greater = x
    else:
       greater = y

    for i in range(2, 10000):
       if(i % x == 0) and (i % y == 0):
           LCM = i
           break

    return LCM

print(lcm(11, 57))

# Homework: Create any geometric shape we created using recursion
# Q1: Square
# Q2: Triangle (right-angled)


def square(length, height, num=0):
    if num == height:
        return 0

    print(("* " * length))

    return square(length, height, num + 1)

square(10, 10)
print("\n")

def triangle(height, num=1):
    if num == (height + 1):
        return 0

    print(("* " * num))

    return triangle(height, num + 1)

triangle(10)

# Inbuilt list functions:
list.append(item)
list.remove(item)
list.index(item)
list[number]
list.get(item)

numbers=[1,2,3,4,5]
print(numbers.pop())       # returns the last element of the list (if no args)
print(numbers)
print(numbers.pop(1))       # returns the removed element from teh list: SYntax: list.pop(index)
print(numbers)
# Output:
# 5
# [1, 2, 3, 4]
# 2
# [1, 3, 4]

"""