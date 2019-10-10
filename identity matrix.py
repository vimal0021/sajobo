n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()


# The sep and end parameters of the print function help in formatting and print() allows values to printed in a new line
#for each iteration of the outer for loop.
