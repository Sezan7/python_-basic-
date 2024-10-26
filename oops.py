class student:
    name = "sezan"


s1 = student()
print(s1.name)

s2 = student()
print(s2.name)
##-----------------------------------------------------------------------
# # bassic class . all the student same name

class car:
    color = "blue"
    brand = "mastang"
x = car()
print(x.brand)

#----------------------------------------------------------------------
# constructor ust __init__ use oops
class student:
    def __init__(self):
        print("Adding a new student in database:..")

x = student()
#----------------------------------------------------------------------------
#  print nah delaw print hove akanda 
# print(x) 
class student:
    def __init__(self,fullname):
        self.name = fullname
        print("Adding a new student in database:..")

x = student("sezan")
print(x.name)
del x.name
print(x.name)
#----------------------------------------------------------------------------
# privet accttibuet
class parson:
    __name ="anonymus"

    def __hello(self):
        print("hellow preson")

    def welcme (self):
        self.__hello()

p1 = parson()
print(p1.welcme())
# ______________________________________________________________

class student :
# default constructors 
    def __init__(self):
        pass
# parameterized constructors
    def __init__(self,name,marks):
        self.name = name
        self.mark = marks
        print("adding new student in database..")
        
s1 = student ("karan",90)
print(s1.name , s1.mark)
s2 = student("arjun",88)
print(s2.name , s2.mark)
# ----------------------------------------------------------
#  Methods in python oop surch as function ,dictionary , list etc
class student :
    collage_name = "knollage collage"
    name = "anonimus "
# default constructors 
    def __init__(self):
        pass
# parameterized constructors
    def __init__(self,name,marks):
        self.name = name
        self.mark = marks
    
    def welcome (self):
        print("welcome student ,", self.name)
    
    def get_marks(self):
        return self.mark

s1 = student("sezan",99)
s1.welcome()
print(s1.get_marks())
# # s1.get_marks() / ata hova nah because print kora cara . print s1  kora hoyaca akana
# ------------------------------------------------------------------------

class student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hi", self.name, "your avarage score is :",sum/3)   

s1 = student("tony stark ",[99, 98,97])
s1.get_avg()

# attedute ar name change and then avarage 
s1.name ="ironman"
s1.get_avg()

# --------------------------------------------------------------------------
# # Static mathod  is mean Name never use @static liklai ar self det hova nah 
# # dairk class mathod a nea cola jay
class student ():
    @staticmethod
    def collage():

         print("knollage is power self univercity ")

        #  this is decorator 
# --------------------------------------------------------------------------

# # Abstraction oops .******
# # hidig the importent just showing essntial valu.

class car :
     def __init__ (self):
          self.acc = False
          self.brk = False
          self.clutch = False

     def start(self):

        self.clutch = True
        self.acc = True
        self.brk = True
        print("car started ..")
key = car()
key .start()
# ---------------------------------------------------------------

# # Alll are hear .. all Encapsulation 

class Acount :
    def __init__(self,bal,acc):
        self.balance = bal
        self.accout_no = acc

    # debit method
    def debit (self,amout):
        self.balance -= amout
        print("doller", amout, "was debited")
        print("total balance = ", self.get_balance())
    
    # cridet method
    def cradit (self,amout):
        self.balance += amout
        print("doller", amout, "was cridet ")
        print ("total balance = ", self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Acount(10000,12345)
acc1.debit(1000)
acc1.cradit(500)
acc1.cradit(400000)
acc1.debit(10000)

# ------------------------------------------------------------
# # privet and public 
class Account :
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12344", " abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass)
print(acc1.reset_pass())




# ----------------------------------------------------------
# inhaitange mathod 
# dubble class writing 
class A:
        varA = "welcome to class A"

class B:
        varB = "welcome to class B"

class C(A,B):
        varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


# # example of the inharitange method
class car:
        def __init__(self, type):
                self.type = type
        

        @staticmethod
        def start():
                print("car started ..")
        
        @staticmethod
        def stop():
                print("car stapped.")
        
class ToyotaCar(car):
        def __init__(self,name,type):
                super().__init__(type)
                self.name = name
                super().start()

car1 = ToyotaCar("prius","electric")            
print(car1.type)
                
# -----------------------------------------------------------------------

# polymorphism in oops 
class Complex:
        def __init__(self, real,img):
                self.real = real
                self.img = img
        
        def showNumber (self):
                print(self.real,"i +", self.img,"j")
        
        def __add__ (self, num2):
                newReal = self.real + num2.real
                newImg = self.img +num2 .img
                return Complex(newReal,newImg)


num1 = Complex(1 , 3)
num1.showNumber()

num2 = Complex(4 , 6)
num2 . showNumber()


num3 = (num1 + num2)

num3.showNumber()
# num3 = num1.add (num2)
# print(num3)



class student :
    def __init__(self,name,intake,mark):
        self.name = name
        self.intake = intake
        self.mark = mark

    def myname (self):
        print("my name is ", self.name)
    
    def mymark (self):
        print("my mark is Economic",self.mark)
    
    def myintake(self):
        return self.intake


s1 = student("sezan","330,310,50,7687","98")
print(s1.name,s1.intake,s1.mark)
print(s1.myname())
print(s1.mymark())

s1.name = "ironman"
print(s1.myname())
print(s1 .myintake())