#Avg of n numbers

limit=int(input("Enter the no. of elements "))
a=[]
for i in range(0,limit):
    number=int(input("Enter the number"))
    a.append(number)
avg=sum(a)/limit
print("Average of elements in the list",round(avg,4))


#Numeric Types -- int, float, long, complex
