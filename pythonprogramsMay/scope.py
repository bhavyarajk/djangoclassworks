#Global Scope

x=20   #global variable declared inside the main part of the program/outside a functio
print(x)     #displays  20
def fun():
     print(x)    #it also displays 20

fun()

#local scope


def fun():
    x=20  #local variable,it is declared inside a function block
    print(x)  #displays 20


fun()
print(x)   #shows "not defined" error since x is a local variable.