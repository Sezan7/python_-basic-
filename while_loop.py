n = 1 
while n <= 3:
    print(n)
    n += 1

#--------------------------------------------
i = 1
while i <= 5:
    print(i)
    i += 1



####-----------------------------------------
# for loops use 
# ----infinite for loops ----------
items = [ 0 ]
for item in items:
    print(item)
    item .append (item)

x = 0 
for x in  range (6):
    print("sezan")

##------------------------------------------------------------

i = 1
while True:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
    
    if i == 10:
        break
    
    i += 1

##-------------------------------------------------------------

number = int(input("Enter a positive integer: "))
sum = 0
i = 1

while i <= number:
    sum += i
    i += 1

print("The sum of numbers from 1 to", number, "is:", sum)

##-----------------------------------------------------------
number = int(input("Enter a non-negative integer: "))
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    while number > 0:
        factorial *= number
        number -= 1
    print("The factorial of", number, "is", factorial)

##-------------------------------------------------------
import random

secret_number = random.randint(1, 100)
guess = 0

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess < secret_number:
        print("Too low. Guess again.")
    elif guess > secret_number:
        print("Too high. Guess again.")
    else:
        print("Congratulations! You guessed the correct number.")


##------------------------------------------------------
while True:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("Result:", result)
    elif choice == 2:
        # ... similar for other operations 

    #elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")



##------------------------------------------------------
n  = int (input ("enter a value of n :"))
sum = 0

while n > 0 :
    sum += n 
    n -= 1
print(f"sum is {sum}")


n = 100
while True:
    print(n )
    n -= 1
#  break nah dela negative ar dik cola jaita para 


while True:
    line = input("enter the line (typr 'q' to quit )")
    if line == "q":
        break
    print(line)




#  q nah dela coltai thakva arki ata 

while True:
    n = input("enter teh number :")
    if n == 'q':
        break
    print(n)
# ----------------------------------------------------------------
fruits = ["apple","banana","mango","strawberry"]
fruits_len = len(fruits)
index = 0

fruit_found = False

while index < fruits_len:
    if fruits[index] == "orange":
        fruit_found = True
        print("orange is availabele .")
        break
    index += 1

if  not fruit_found:
    print("orange is not available ")
# --------------------------------------------
item = 0 
while True:
    print(item)
# -----------------------------