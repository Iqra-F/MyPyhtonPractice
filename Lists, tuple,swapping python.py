import os
print(os.listdir())
'''#lists
mlist=[1,30,1,90,52,4,5]
#to print list items 
print(mlist[0])
print(mlist[1])
print(mlist[2])
print(mlist[3])
print(mlist[4])
#to sort list
#it will change original list
mlist.sort()
print(mlist)
#to print reverse of sorted  list
#it will change original list
mlist.reverse()
print(mlist)
#list can store mixed data types
mixlist=["iqra", "fatima",32,59,56,"iqra fatima is a good girl"] 
print(mixlist[5])
 
#list slicing(means printing only that part items which u want to print and neglect other items
#it will not change original list
#it will print items from index 1 to 4
print(mixlist[1:4])
#it will print items from index 1 to 5
print(mixlist[1:5])
#it will print full list i.e from 0 index to 5 index
print(mixlist[0:5])
#the first and last index values are default if we don't write any value like below I  did
#it will print full list i.e from 0 index to 6 index
print(mixlist[:])
print(mixlist[5])
#no matter if the last item u mention in list to print is out of range , it will print the list till last item
#like here i write 100 as last item to print but it will not through errr saying "index is out of range"
print(mixlist[0:100])

#extended slicing, used to prin elements of list by skiping or jumping items 
#print(mixlist[0:5:1]) are default values in extended slicing 0=1st indes, 5=last index
# it will jump or skip one item and print others
print(mixlist[0:5:2])
# and 1 is default for 3rd value after 2nd semi colon , i can also write as
print(mixlist[::])
#OR
print(mixlist[0:5:1]) # to print all values
# nagative extended slicing ,  it will first reverse the list and them jump index
new=[1, 2 ,3, 4 ,32 ,5 ,6 ,7 ]
print(new[::-2]) # but there is a problem that it only works if 1st and 2nd values are set as default values
#otherwise it will return empty list


# printing length , max no and min no in a list
SIBLINGS =["IQRA",1, "SAFINA",2, "AYHSA ",3, "SABA" ,4, "SULEMAN",5]
print(len(SIBLINGS))
nums=[1,6,8,92,52,3,38]
print(max(nums))
print(min(nums))
'''
#to add items at the end of a list
nums=[]
nums.append(99)
nums.append(100)
nums.append(1000)
print(max(nums))
print(nums)
# u can create an empty list and then append items in it

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#u can insert item at any index, here 1st no is index and 2nd no is value to insert

me =[30,31,32,33]
print(me)
me.insert(1,50)
print(me)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# to remove last item in list
thislist.remove("orange")
print(thislist)

# to remove last item in list
thislist.pop()
print(thislist)
#to chande value of any index:
thislist[1] ="kela"
print(thislist)

#tuple
#difference b/w lists and tulpe
#in list u can chane value at any index but in tuple it is not allowed
tp=(1,2,3,4,5)
print(tp)
#to create a tuple of only one item u need to place a comma after 1st item like:
tps=(32,)
print(tps)

#SWAPPING
# normally to swap values we se formula:
a=10
b=20
temp=a
a=b
b=temp
print(a,b)

#in python this can be done simply by writing:
a=33
b=39
a,b = b,a
print (a,b)


#EXTEND LIST
#To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#Unpack a list/collection:
#If you have a collection of values in a list, tuple etc.
#  Python allows you to extract the values into variables.
#  This is called unpacking.
 
mycollection=[1,2,3,4,5,6]
x,y,z,a,b,c=mycollection
print(x,y,z,a,b,c)





