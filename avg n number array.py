n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))



#a.append(elem) appends the element to the list.
#sum(a) gives the total sum of all the elements in the list and dividing it by the total number
#round(avg,2) rounds the average upto 2 decimal places.
