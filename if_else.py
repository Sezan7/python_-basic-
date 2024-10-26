n = 10
if n % 2 == 0:
    print("Numbur is dividible by 2")
elif n % 3 == 0:
    print("Number ai divisiale by 3")
else:
    print('number is not  DVIVISIAVE by  3 AND 2')

print("done!")

# ---------------------------------------------------------
# # ligical AND with if statement 

age = 20 
nationality = "bangaldeshi"
if age > 18 and age < 30 and nationality == "bangaldeshi":
    print('you are eligible for the exam')

#  logical AND with if else statement

age = 34
nationality = "bangaldeshi"
if age > 18 and age < 30 and nationality == "bangaldeshi":
    print('you are eligible for the exam')

else:
    print ("YOU ARE NOT ELIGIBLE FOR THE EXAM")

# LOGICAL and  whit if elif and else 
age = 34
nationality = "American"
if age > 18 and age < 30 and nationality == "bangaldeshi":
    print('you are eligible for the exam')

elif age > 18 and age < 30 and nationality == "American":

    print ("you are eligible for the exam . exam fee is $50 ")
else:
    print("you are not eligible for the exam ")

# ---------------------------------------------------------

# # logical OR whit if 

today = "sunday "
if today == "sunday " or today == 'strerday':
    print("today is weekend ")
elif today == "friday " or today == " monday ":
    print("wark 4 hour few")
else :
    print("practic mor and sure a future ")

# ==============================================================

# logical NOT 

# the boolean value is True then the Not opearator are false;


x = False
if not x :
    print("x is false .") 
    # x is true 

name = "johan"
if not name :
    print ("no name ")
else :
    print(f"your name is {name}")

# stirig is entry  

name = "" # antry string mean 0 
if not name :
    print ("no name ")
else :
    print(f"your name is {name}")


####-----------------------------------------------------------------------------------
# # define the menu of restarant 
menu = {
    "pizza" : 40,
    "pasta" :50,
    "burger":60,
    "salad":70,
    "coffee":80,
}

print("welcome to Python resturent")
print("pizza: tk40\npasta: rs60\nsald: rs70\ncoffee:rs80")


order_total = 0
item_1 = input("enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"orderd item {item_1} is not avaialable yet1!")
another_order = input("do you want to ass another order (yes or no )")
if another_order == "yes":
    item_2 = input("enter the name of second item = ")
    if item_2 is menu :

        order_total += menu[item_2]
        print (f"item {item_2} has been added to order ")
    else:
        print(f"ordered item {item_2} is mot abaleable ")
    
print(f"the total amount of items of pay is {order_total}")

###------------------------------------------------------------------------------

n = 10
if n % 2 == 0:
    print("Numbur is dividible by 2")
elif n % 3 == 0:
    print("Number ai divisiale by 3")
else:
    print('number is not  DVIVISIAVE by  3 AND 2')

print("done!")

# ---------------------------------------------------------
# ligical AND with if statement 

age = 20 
nationality = "bangaldeshi"
if age > 18 and age < 30 and nationality == "bangaldeshi":
    print('you are eligible for the exam')

#  logical AND with if else statement

age = 34
nationality = "bangaldeshi"
if age > 18 and age < 30 and nationality == "bangaldeshi":
    print('you are eligible for the exam')

else:
    print ("YOU ARE NOT ELIGIBLE FOR THE EXAM")

# LOGICAL and  whit if elif and else 
age = 34
nationality = "American"
if age > 18 and age < 30 and nationality == "bangaldeshi":
    print('you are eligible for the exam')

elif age > 18 and age < 30 and nationality == "American":

    print ("you are eligible for the exam . exam fee is $50 ")
else:
    print("you are not eligible for the exam ")

# ---------------------------------------------------------

# logical OR whit if 

today = "sunday "
if today == "sunday " or today == 'strerday':
    print("today is weekend ")
elif today == "friday " or today == " monday ":
    print("wark 4 hour few")
else :
    print("practic mor and sure a future ")

# ==============================================================

# logical NOT 

# the boolean value is True then the Not opearator are false;


x = False
if not x :
    print("x is false .") 
    # x is true 

name = "johan"
if not name :
    print ("no name ")
else :
    print(f"your name is {name}")

# stirig is entry  

name = "" # antry string mean 0 
if not name :
    print ("no name ")
else :
    print(f"your name is {name}")