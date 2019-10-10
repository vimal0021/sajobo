
def add(x, y):
   return x + y


def subtract(x, y):
   return x - y


print("Enter choice.\n 1.Add\n 2.Subtract")
choice = input("Enter your choice:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == 2:
   print(num1,"-",num2,"=", subtract(num1,num2))
   
else:
   print("Invalid input")





#There are several parts of the syntax for a function definition :
   # syntax is def function_name():
 #A more general 

