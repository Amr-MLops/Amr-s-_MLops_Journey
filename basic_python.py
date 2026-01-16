x=3.556
y=-6
z=9
result1 = round(x)>>>>near num
result2= abs(y)>>>>(-)>(+)
result3 = pow(5,2)>>>>>(**num)
result4 = max(x,y,z)>>>>big num
result5 = min(x,y,z)>>>>>small num
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
# >>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<
weight = float(input("ENTER YOUR WEIGHT: "))
unit=input("killogramsor pound? (K or L)")
if unit=="K":
    weight = weight * 2.025
    unit="lps"
    print(f"your weighe is:{round(weight,2)} {unit}")
elif unit=="L":
    weight=weight/2.025
    unit="kgs"
    print(f"your weighe is:{round(weight,2)} {unit}")     
else:
    print(f"the {unit} is not valid")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<
x =5
a =6
b= 7
# print("positive" if x >0 else "negative")
# result ="even" if x %2 ==0 else "odd"
# print(result)
max_num= a if a >b else b
# print(max_num)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
name = input("enter your name: ")
result=  name.find("h") 
result= name.rfind("h")#search in back
result=  name.isdigit()#only num
result=  name.isalpha()#no space 
result=  name.count("a")#how many in this(>>>  <<<<)
result=  name.replace("a","3")
print(result)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
name = input("enter your name: ")
if len(name) > 12:
    print("you can write more 12 letter")
elif not name.find(" ")==-1: #=>>>pro<<<=if " " in name: >print("you can't write space")
    print("you can't write space")    
elif not name.isalpha():
    print("you can't write number")    
else:
    print(f"welcome {name}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<
num="542-57421-48-512"
result=num[::-1] return end to star
print(result)
print(num[0 :8: 2])#[star:end:step]
# >>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
price1 = 9.6535
price2 =-24
price3 =857
price4 =5746312
price5 =856752
price6 =85.261204
print(f"price1 is {price1:10}")
print(f"price2 is {price2:010}")
print(f"price3 is {price3:+}")
print(f"price3 is {price4:,}")
print(f"price3 is {price5:+,}")
print(f"price3 is {price6:.2f}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
user =int(input("entre your years you in born it: "))
name=input("entre your name: ")
age = 2025 - user
if age < 0 or age >=120:
    print("wrong year pleas enter corect age...")
elif age >=18:
    print(f"hello,you are name is {name.capitalize()} and your age is {age}")    
else:
    print("you are child")    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import time
my_time= int(input("entre your time of seconds: "))
for x in range(my_time,0,-1):
    secons=x % 60
    mumint =int(x/60) % 60
    hours = int(x /3600)
    print(f"{hours:02}:{mumint:02}:{secons:02}")
    time.sleep(1)
print("time up's")
# <>>>>>>>>>><<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>><<>>>>>
for x in range(0,11):
    print(x,end="\n$")
# <<>>>>>>>>>>>>>><<<><><<<<><<<<><<<<<>>>>>>>>>>>><<<<<<>>>>>>>>
foods=[]
prices=[]
total=0
while True:
    food = input("entre your food or (q): ")
    if food.lower()=="q":
        break
    else:
        price =float(input(f"entre the price {food}: $"))    
        prices.append(price)
        foods.append(food)
print("---------------------your cart--------------------")        
for food in foods:
    print(food,end=" ")

print()
for price in prices:
    total +=price
     
print(f"your totals is {total}: $")     
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<
menu={"pizza":120,
      "popcorn":5,
      "meet":350}

cart=[]
total=0
while True:
    food=input("entre you choase or (q:quit) : ")
    if food =="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"total is ${total:.2f}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import random
num = random.randint(0,8)
print(num)
<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import random
option=("rock","peper","scissors")

while True:
    user=input("enter you chois (rock,peper,scissors) or (q:quit) : ")
    if user == "q":
        break

    if user not in option:
        print("Invalid choice, please try again.")
        continue

    computer=random.choice(option)
    print(f"Computer chose: {computer}")
    if user == computer:
        print("It's a tie!")
    
  
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You won!")
        
    else:
        print("Computer won!")
    
    print("_" * 50)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<
def day_of_week(day):
    match day:
        case 1:
            return "it's sunday"
        case 2:
            return "it's monday"
        case 3:
            return "it's tuesday"
        case 4:
            return "it's wednesday"
        case 5:
            return "it's thurday"
        case 6:
            return "it's friday"
        case 7:
            return "it's saturday"
        case _ :
            return "it's not vallid"
        
print(day_of_week(5))   
    # <<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>  
def show_balance():
    print(f"your balance is ${balance:.2f}")

def deposit():
    amount=float(input("entre the money you went deposite: "))
    if amount <0:
        print("is not valid please try agian")
    else:
        return amount
def withdraw():
    amount=float(input("entre the money you went withdraw: "))
    if amount > balance:
        print("is not valid please try agian")
        return 0
    else:
        return amount

balance = 0
is_running=True
while is_running:
    print("banking program")
    print("___________________________")
    print("1.show balance")
    print("2.deposite") 
    print("3.withdraw")
    print("4.exit")
    print("___________________________")
    choice=input("entre the program you went: ")
    if choice=="1":
        show_balance()
        print("___________________________")
    elif choice=="2":
        balance +=deposit()
        print("___________________________")
    elif choice=="3": 
        balance -= withdraw()   
        print("___________________________")

    elif choice=="4":
        is_running=False     
        print("___________________________")
    else:
        print("is not valid please try agian")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<.
import random
def spin_row():
    symbol=['🍉','🍒','🍋','⭐','🔔']
    # result=[]
    # for symbol in range(3):
    #     result.append(random.choice(symbol))
    # return result
    # {OR}
    return[random.choice(symbol) for _ in range(3)]
def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍉":
            return bet *3
        elif row[0]=="🍒":
            return bet *4
        elif row[0]=="🍋":
            return bet *5
        elif row[0]=="⭐":
            return bet *6
        elif row[0]=="🔔":
            return bet *7
    return 0    
    

def main():
    
    balance=100
    print("_________________________")
    print("welcome you in our slot:")
    print("sympol:[🍉🍒🍋⭐🔔]")
    print("*************************")
    while balance >0:
        print(f"current balance${balance}")

        bet=input("place your bet amount: ")

        if not bet.isdigit():
            print("is not valid: ")
            continue
 
        bet=int(bet)
        if bet >balance:
            print("you can't entre amount more the balance")
            continue

        if bet<=0:
            print("you can't entre amount less or equel zero")
            continue

        balance -=bet
        row=spin_row()
        print("spining.....")
        print_row(row)

        payout=get_payout(row,bet)
        if payout>0:
            print(f"you wiiiin:${payout}")
        else:
            print("you lose this round")    

        balance +=payout    



if __name__ =='__main__':
    main()   
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<
import random
import string
chars= " "+string.punctuation+string.digits+string.ascii_letters
chars=list(chars)
Key=chars.copy()

random.shuffle(Key)
# print(f"chars:{chars}")
# print(f"key:{Key}")

real=input("enter your words: ")
fack=""
for leeter in real:
    index =chars.index(leeter)
    fack += Key[index]

print(f"this is real words:{real}")    
print(f"this is fack words:{fack}")  
# >>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>><<<<>
class Student:
    income=0 #(class variables)share data among all object in this class
    def __init__(self,name,years):
        self.name = name
        self.years = years

stu1=Student("amr",17)
stu2=Student("amr",22)
print(stu1.name)
print(stu2.name)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<>>>>>>>>>>>>>>>>>>>>...
# <<<<<<<<<<<<<<<<<<<<<<inheritance>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<>>>>>>>>>>>>>>>>>>>>...
class Animales:
    def __init__(self,name,voice):
        self.name = name 
        self.voice = voice

class Dog(Animales):
    pass

dog1 =Dog("pedpol","hawhawhaw")
print(dog1.name)
print(dog1.voice)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled

class circle(shape):
    def __init__(self, color, filled):
        super().__init__(color, filled)

class sqare(shape):
    def __init__(self, color, filled):
        super().__init__(color, filled)

circle1 =circle("red",True)
sqare1 =sqare("blue",False)
print(circle1.color)
print(sqare1.color)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>..
class Animale:
    alive =True

class Dog(Animale):
    def speak(self):
        print("woof!")

class Cat(Animale):
    def speak(self):
        print("meo!")
        
animale=[Dog() ,Cat()]
for animales in animale:
    animales.speak()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<
class Student:
    count =0
    avr_gpa = 0
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count +=1
        Student.avr_gpa += gpa
    def get_info(self):
        return f"{self.name} , {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"the total #count {cls.count}"
    
    @classmethod
    def avredge_gpa(cls):
        if cls.count ==0:
            return 0
        else:
            return f"{cls.avr_gpa / cls.count:.2f}"

stu1=Student("amr", 3.4)      
stu2=Student("osama", 2.5) 
stu3=Student("saad", 4.0)
print(Student.avredge_gpa())
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
class Book:
    def __init__(self,title,athour,pages):
        self.title =title
        self.athour =athour
        self.pages = pages
    
    def __eq__(self, other):
        return self.title == other.title
    
    def __lt__(self, other):#lessthan
        return self.pages < other.pages
    
    def __gt__(self, other):# more than
        return self.pages > other.pages
    
    def __add__(self,other):
        return f"{self.pages + other.pages}"
    
    def __contains__(self,kyword):
        return kyword in self.title and self.athour
    
book1 = Book("harry potter","geef",330)  
book2 = Book("harry pottersd","patter",218)
print("harry" in book1)  
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<,
def add_sprinkless(fucs):
    def wrapper ():
        print("you add the sprinkless")
        fucs()
    return wrapper    

@add_sprinkless
def get_ice_cream():
    print("you revice the ice cream:")

get_ice_cream()    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
try:
    number = int(input("entre your number: "))
    print(1/ number) 
except ZeroDivisionError:
    print("you cant entre the zero") 
except TypeError:
    print("you cant entre the letters or words")   
except ValueError:
    print("you cant entre the letters or words")        
# <<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<>>>>>>>>>>>>>>
class Stu:
    def __init__(self,name,sub):
        self.name=name
        self.sub=sub

    def avradge(self):
        total=0     
        for grade in self.sub.values():
            total += grade
        return total , len(self.sub)    
    
    def sub_passed(self,sub):
        if self.sub[sub]>=50:
            return True
        else:
            return False
        
    def is_passed(self):
        return self.avradge()>=50
    
students=[
    Stu("amr",{"math":70,"E":80}),
    Stu("amr",{"math":30,"E":40})
]    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<


