import os

numA= int(input("please enter first number: "))
numB= int(input("please enter second number: "))
Operation=input("enter operation to perform like:+,-,*,/,%:  ")


if Operation=="+":
 print("sum of these two numbers is : ",numA+numB )

elif Operation=="-":
 print("Difference of these two numbers is: ",numA-numB )

elif Operation== "*":
 print("product of these two numbers is : ",numA*numB )

elif Operation== "/":
 print("division of these two numbers is: ",numA/numB )


elif Operation=="%" :
 print("modulus of these two numbers is : ",numA%numB )

else:
 ("Invalid Operation")



