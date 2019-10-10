lower,upper=int(input("Enter the lower limit for the range:")),int(input("Enter the upper limit for the range:"))
for i in range(lower,upper+1):
    print(i if i%2!=0,end='')
