#Armstrong Number

# n=int(input("Enter the number"))
#
# s=str(n)
#
# l=len(s)
# sum=0
#
# for i in s:
#
#     sum=sum+int(i)**l
#
# if(sum==n):
#      print("Armstrong")
# else:
#      print("Not An Armstrong Number")


#Print Fibinocci Series
#
# # 0,1,1,2,3,5,8,13,21,34
# a=0
# b=1
#
# for i in range(1,11):
#        print(a)
#
#        a,b=b,a+b


#Remove Duplicates from the string

s="python is a programming language"
str=""
for i in s:
    if i not in str and i!=" ":

        str=str+i

print(str)

#Remove duplicates from the list
l=[1,1,4,6,6,6,3,9,2,3]
li=[]
for i in l:
    if i not in li:
        li.append(i)
print(li)












