#program to swap(interchange) two numbers

# Using third variable
x=2
y=3

temp=x
x=y
y=temp
print("After swapping",x,y)

#Without using third variable
x=2
y=3
x,y=y,x
print("After swapping",x,y)

#Without using third variable
x=2
y=3

x=x+y
y=x-y
x=x-y

print("After swapping",x,y)




