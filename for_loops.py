# n = int (input("enter a value of n :"))
# sum = 0
# for i in range( 1, n + 1):
#     sum += i
# print(f"sum of first {n} natural numbers is {sum}:")


# # -----------------------------------------------
# for i in range (5, 0 , -1):
#     print(i)
# print( "done !")


# for i in reversed(range(1 , 6, 1)):
#     print(i )


# # ---------------------------------------------------------

# name = " sezan"
# for c in name :
#     print(c , end=' ')


# name = "johan "
# for c in name [ : : -1]:
#     print (c , end=" ")

# # --------------------------------------------------------  

# sentence = " lion is the king of the foraest "
# count = 0 
# for  word in sentence. split():
#     count += 1
# print(f"the count number {count} word in sentance")

# # ---------------------------------------------------------
# cars = [ "audi",  " bmw", " toyota"]
# for car in cars:
#     print(car)

# # -------------------------------------------------------
# #  range function 

# cars = [ "audi",  " bmw", " toyota"]

# for i in range (len ( cars)):
#     print(cars[i])


# -----------------------------------------------
# # list comprehension 
# cars = [ "audi",  " bmw", " toyota"]
# [ print (car ) for car in cars]

# # --------------------------------------------------
# #  dictonary in keys 
# course = { "name ": "python", "instructor" : "jaspreet"}
# for x in course:
#     print(course[x])


# #  value in distonary 
# course = { "name ": "python", "instructor" : "jaspreet"}
# for y in course. values():
#     print( y )

# # ----------------------------------------------------------
# #  keys mathods 
# course = { "name ": "python", "instructor" : "jaspreet"}
# for y in course. keys():
#     print( y )


# #  key and value equal 
# course = { "name ": "python", "instructor" : "jaspreet"}
# for x , y  in course . items():
#     print(course[x])

# -----------------------------------------------------------

#   loop in  if and else 

# favaute_laguse = [ "pythin ", "c", 'java', "ruby"]

# for language in favaute_laguse:
#     if " java " == language:
#         print(" i like java.")
#         break
#     else:
#         print ( " i dont like java ")

# ----------------------------------------------------------
# number = list ( range ( 0 , 100))
# for number in numbers:
#     if number > 50:
#         break
#     print( number, end=" ")

# -------------------------------------------------------
# while True:
#     num = input("enter the number ( q for quit): ")
#     if num == " q ":
#         break
#     print(num)

# # ---------------------
# for i in range (5):
#     if i == 2 or i == 4 :
#         continue
#     print(  i )

# n = 0 
# while n <= 10:
#     n += 1
#     if n % 2 != 0 :
#         continue
#     print(n , end=" ")
