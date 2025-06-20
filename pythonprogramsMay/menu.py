
def sum(n1,n2):
    s=n1+n2
    print(s)

def sub(n1,n2):
    s=n1-n2
    print(s)

def mul(n1,n2):
    s=n1*n2
    print(s)

def div(n1,n2):
    s=n1/n2
    print(s)



while(1):

    print('Arithmetic Operations')
    print('1.ADDITION')
    print('2.SUBTRACTION')
    print('3.MULTIPLICATION')
    print('4.DIVISION')

    ch=int(input("Enter the choice"))
    if ch in [1,2,3,4]:
        n1=int(input("Enter the number"))
        n2=int(input("Enter the number"))
    if ch==1:
        sum(n1,n2)
    elif ch==2:
        sub(n1,n2)
    elif ch==3:
        mul(n1,n2)
    elif ch==4:
        div(n1,n2)
    else:
        exit()
