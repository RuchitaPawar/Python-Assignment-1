def checkNumber(value):
 if(value < 0):
   print("Negative Number")
 elif(value > 0):
   print("Positive number")
 else:
   print("Zero")

number = input("Enter number:")
num = int(number)

checkNumber(num)