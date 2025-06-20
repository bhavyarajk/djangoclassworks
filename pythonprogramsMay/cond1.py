#Program to check whether a number is positive number or negative number

n=int(input("Enter the number"))

if(n>0):
    print("number",n," is positive")

else:
    print("number",n," is negative")


#Program to check whether the number is even or odd number
n = int(input("Enter the number"))

if (n %2== 0):
    print("number", n, " is even number")

else:
    print("number", n, " is odd number")

#program to check whether the number is divisible by 7 or not
n = int(input("Enter the number"))

if (n %7== 0):
    print("number", n, " is divisible by 7")

else:
    print("number", n, " is not divisible by 7")
#program to check whether the number is multiple of 3 and 5
n = int(input("Enter the number"))

if (n %3== 0 and n%5==0):
    print("number", n, " is a multiple of 3 and 5")

else:
    print("number", n, " is not a multiple of 3 and 5")


