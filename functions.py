# part 1
student_2 = [40,60,90]
sum_of_marks = sum(student_2)
total_sub = len(student_2)
avarage = sum_of_marks / total_sub
print("avarage of student 2 is ", avarage)

#---------------------------------------------------------
## function is use to stucture bulding 

def sum (a,b):  # patameter is 
    c= a + b
    print("sum is ",c)

sum(12,24)  #Argoment is
sum(3,5)

#-------------------------------------------------------------------------------------
def multi (a,b):
    c = a * b 
    return f" the sum is c = {c}"

a = multi(20,10)
print(a)


#----------------------------------------------------------

def xyz (a,b):
    a= 10
    b= 20
    c = a*b
    return c

x = xyz(10,30)
print(x)
#---------------------------------------------------------------
def lines ():
    line = int(input("Enter a number of line ="))
    for i in range (1, line+1):
        for j in range (i):
            print("*" , end= " ")
        print()    

    return f"the {line} number of trinangle has been cer"

tringel = lines()
print(tringel)

#-------------------------------------------------------
def sezan ( k, f):
    sef = (k + f)
    return sef

here = sezan(56,6)
print(here)

# ----------------------------------
def sezan (a,b):
    seza = (a + b)
    return seza 

mr = sezan(20 , 10)
print(mr)