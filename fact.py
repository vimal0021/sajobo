def factorial(n):
    if(n <= 1):
        return 1
        
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial is :")
print(factorial(n))



#The return statement
    #is used when a function is ready to return a value to its caller.
#def square(x):
   # y = x * x
   # return y

#toSquare = 10
#result = square(toSquare)
#print "The result of " + str(toSquare) + " squared is " + str(result)
