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
  print("Assalam o alikum sir, have a nice day")
elif greetings>=timenow:
  print("Assalam o alikum sir, it's morning")
elif greetings<=timenow:
  print("Assalam o alikum sir, it's after noon")
if greetings==12:
  print("Assalam o alikum sir, it's night")
else:
  ("time u just entered is not valid")