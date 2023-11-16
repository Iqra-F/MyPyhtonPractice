import os
#DAY10-------------
'''intA= input("1st: " )
intB= input("2nd: ")
print(int(intA)+float(intB))

#DAY11-------------
#USING DOUBLE QOUTES  IN A STRING
#(1)either use single quote to enclose the string
mystring=('hello, my name is "Iqra Fatima" and I am doing bechlors.')
print(mystring)
#(2)or use backslash\ and double quote
mystring=('hello, my name is \"Iqra Fatima" and I am doing bechlors.')
print(mystring)'''
#for multi lines string use ''' or """ at the begining and at the end
#example1:

mystr='''hello!
my name is:
"Iqra fatima"
 And
i am a bechlor's student'''
print(mystr)

#example2:

mystr ='''hello!
 my name is:
"Iqra fatima" so there are

'only'
32+60 90 only 

\"111121"

///###$$%$%%^&#!$@#%^**()
w2392yb fcv 

                  y 2 23prereredkflxmcm,dpqm12X
 And 


i am a bechlor's student'''

print(mystr)

#accessing characters/elements of a string using lop or index

#using index
mypro="i use whatsapp"
print(mypro[0])
print(mypro[2])
print(mypro[3])
print(mypro[4])
#using loop
for item in mypro:
 print(item)

#DAY12--------------
#string slicing

new = 'iqra here'
print(new[0:9]) #can also be written as print(new[:])last index 9  will not be printed, noticed
print(len(new))# printing length of a string
print(new[0:(len(new)-5)]) # can also be written as print(new[0:-5])
print(new[0-9:0-8])  # can also be written as print(new[-9:-8])
# -ve indexing
print(new[-9:-5]) #ereh arqi, asnwer=iqra
name="harry"
print(name[-4:-2]) #yarrh, answer=ar

#DAY13------------------
'''string methods
sting is immutable(can't be changed), but we can use some methods that can create a new 
string keeping the original one intact e.g upper() method will create a new string of upper
case in output only keeping original string intact'''

sentence="!!! my name ##### is iqra!!!!!"
print(sentence.upper())
print(sentence.lower())
print(sentence.rstrip("!"))#will remove special character from end only 
print(sentence.replace("iqra","fatima"))
print(sentence.split(" "))#create a list of string in which each separated word become a list item, 
#note only there should be one space in double quotes split(" ")
print(sentence.capitalize())#capataliza only first letter of a string
print(sentence)# see original string remains intact
print(sentence.center(60))#will print sring in center after 30 spaces and 30 is length of string itself
print(len(sentence))
print(len(sentence.center(60)))# answer=60 bcs 30 are spaces and 30 is string length
myintro="my name is iqra, iqra ,iqra , fatima, iqra"
print(myintro.count("iqra"))#will count how many times iqra occured in string
print(myintro.endswith("qra"))#return True if string end with mentioned word
print(myintro.endswith("iqra",0,12))#value in-between 0 to 12 index
print(myintro.find("is"))#return the index no of 1st occurance of given  word , and return -1 if given
#word not found
print(myintro.index("is"))#it s sme like find() method but returns error instrad of -1 if value not found
copystring="i am 22 years old"
print(copystring.isalnum())#return True if string is alphanumeric i.e contain A-Z,a-z & 0-9
print(copystring.isalpha())#return True if string is alphanumeric i.e contain A-Z,a-z only otherwise False
print(copystring.islower())#return True if all characters are lower case only otherwise False
print(copystring.isprintable())#return True if string is containing all printable words i.e
#doesn't contain non printable words like \n etc, otherwise return False
print(copystring.isspace())#return True if string contains white spaces only like "   " ,otherwise False
print(copystring.isprintable())#return True if string is containing all words with first letter capatalized
#like "I Am A Very Good Girl" ,otherwise return False 
print(copystring.swapcase())#changes the character casing of a string i.e upper to lower and vice versa
'''
#DAY14--------------------
#if-else(conditional statements)
#conditional opereators:<,>,<=,>=,==
a=int(input("enter a number: "))
b=int(input("enter another number: "))
print("my age is: ",a)
print("your age is: ",b)
#without using conditional statements:
print(a==b)#If true then retun True otherwise False
print(a<=b)#If true then retun True otherwise False
print(a>=b)#If true then retun True otherwise False
print(a>b)#If true then retun True otherwise False
print(a<b)#If true then retun True otherwise False
#nowusing conditional statements:
if a==b:
  print("You both are having same age")
elif a<=b:
  print("I am younger and innocent than u")
elif a>=b:
  print("I am older than u")
elif (a>b):
  print("I am older than u")
elif a<b:
  print("I am younger and innocent than u") 
elif a!=b:
  print("You both are not having same age")    
else:
  print("please enter valid nombers")  
#nested if
if a==b:
  print("You both are having same age")
elif a!=b:
    print("there is a difference in our ages let's check how: ")
    if a<=b:
       print("I am younger and innocent than u")
    elif a>=b:
        print("I am older than u")  
else:
  print("please enter valid nombers") 

#DAY15--------------------
#IF-else excercise(mini project)
import time
timenow =time.strftime("%H,%M,%S")
print(timenow)
timenow =time.strftime("%H")
print(timenow)
timenow =time.strftime("%M")
print(timenow)
timenow =time.strftime("%S")
print(timenow)
greetings=time.strftime(input("please enter current time here in format \"hours,mins,seconds: "))
if greetings==timenow:
  print("Assalam o alikum sir, it's morning")
elif greetings>timenow:
  print("Assalam o alikum sir, it's morning")
elif greetings<timenow:
  print("Assalam o alikum sir, it's after noon")
elif greetings!=timenow:
  print("Assalam o alikum sir, it's night")
else:
  ("time u just entered is not valid")

#DAY16---------------------
#matchcase statements:an addition to python 3.10, very necessay to modern programmers
#it's like switch statement in c or c++
z=input("input your city name: ")
match z:
   case "Chakwal":
    print("it's a rural area mostly but it has a lot of visitor's palces")
   case "Rawalpindi":
    print("it's Pakiustan's capital")
   case "Karachi":
    print("it's famous as \"The City Of lights")
   case _ if "Lahore":# u can also use if statement in match statement
    print("Lahore Lahaore ay")
   case _:
    print("it's nice area")
   
#note that there is no break statement in match statement as in switch statement

#DAY17---------------------
#For loop
for i in range(0,20001,200):#print 0-20000 jumping 200 after each iteration
  print(i)
  #note that last no of 20001 will not be printed, it prints 1 no less 
  #to print last no write print(i+1) instead of print(i)
  print(i+1)
#while loop
#the above values can be printed using while loop as follows:
i=1
while 1<20000:
 print(i)
 if i==19000:
  break
 elif i==18995:
  continue
 i +=1
 #above is incrementing while loop
 #below is example of decrementing while loop
x=30
while(x>-30):
 print(x*x)
 x -=1
#else with while loop will be executed of loop is over
else:
  print("loop is over")

#extra questions practice 
my=[22,67,3,9,1,54]
my.sort(reverse=True)
print(my)
names = ["Baby", "Honey", "Harry", "Sandy", "Joy"]
name = input("Enter Name to Check\n:")
if name in names:
    print(name, "Yes it is in the list")
else:
    names.insert(0,"iqra")
 
print(names)
'''
#Emulating do-while loop in python
'''do..while is a loop in which a set of instructions will execute at least once (irrespective of the 
condition) and then the repetition of loop's body will depend on the condition passed at the end of 
the while loop. It is also known as an exit-controlled loop.
How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar
behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with 
a break statement wrapped in an if statement that checks a given condition and breaks the iteration 
if that condition becomes true:

Example:'''
while True:#now the loop will execute at lest once even the if condition within body of loop is false as we do in do-while loop
 print("see the loop is executed once even if it doesn't go to if condition still")
 num3=int(input("Enter a positive number: "))
 print(num3)
 if not num3>=0:
    break
# DAY18------------------
#loops
# DAY19------------------
#break & continue statement
# DAY 20 & 21------------------
#functions
# DAY22--------------------
#lists
mymarks=[20,19,30,"Iqra",100,33]
print(type(mymarks))
print(mymarks[0])
print(mymarks[4])
print(mymarks[2])
#or u can use loop
for i in range(0,len(mymarks)):
 print(mymarks[i])
#-ve indexing
print(mymarks[-3])
#OR u can place len(mymarks) before  to get the same result if it is confusing to u
print(mymarks[len(mymarks)-3]) # by converting into positive indexing
#OR
print(mymarks[6-3])    #since len(mymarks) is 6

# to check if any value is an item  of the list or not
if 100 in mymarks:
  print("present")
else:
  print("absent")
#same thing applies on string to check if these letters are members of string or not?
if "Iq" in" Iqra" and 33 in mymarks :
   print("yup")
else:
  print("no")
# if u want to print the whole list u can do following
print(mymarks)
#OR
print(mymarks[:])
#list comprehension
#List comprehensions are used for creating new lists from other iterables like lists, tuples,
#  dictionaries, sets, and even in arrays and strings.
#Syntax:List = [Expression(item) for item in iterable if Condition]

lst = [i*i for i in range(10)]
print(lst)
#We can check if a given item is present in the list. This is done using the in keyword.
lst = [i*i for i in range(10) if i%2==0] #i%2==0 means no should be divisible of 2 i.e even no
print(lst)

#DAY23-------------------------
#lists
l=[1,2,3,4,4,4,5]
l.append(5)#add 5 at the end of the list
l.sort()# sort in ascending order
l.sort(reverse=True)# sort in descending order
l.reverse()#reverse the original list
print(l)
print(l.index(2))#return value at index 2 i.e value=3
print(l.count(4))#return count of how many times 4 appeared
m=l
m[0]=9
print(m)
print(l)
#both m & l have same values i.e having same address
#making changes in m also reflected in  l
# if u want to only make changes in m not in l then 
# make a new copy of l whose address is stored in m and now
#  it is possible that making changes in m would not be reflected in l as;
m=l.copy()
m[0]=9
m.insert(0,3)
m[2]=30
print(m)
print(l)
# to add another list's content in alaready existing list at the end
n=[60,70,63]
m.extend(n)#it will add 60,70,63 at the end of m
print(m)
#but it will make changes in m
# if u want add two lists without the existing one then store them into a new one as:
k= m+n
print(k)

#DAY24----------------------


