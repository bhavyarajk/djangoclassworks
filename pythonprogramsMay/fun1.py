#Functions


#sum of two numbers
# def add():
#     n1=int(input("Enter the first number"))
#     n2=int(input("Enter the second number"))
#     sum=n1+n2
#     print(sum)
#
# add()

# def add(n1,n2):
#     sum=n1+n2
#     print(sum)
#
# add(56,34)


#Define a function to find the factorial of a number using single parameter
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial",f)
fact(5)


#Define a function to check whether a number is even or odd
def check_num(n):
    if(n%2==0):
        print("even")
    else:
        print('odd')
check_num(9)
check_num(6)

#Define a function to find the reverse of a string

def reverse_string(s):
    rev=""
    for i in s:
        rev=i+rev
    print("Reversed String",rev)


reverse_string("hello")

reverse_string('python')





