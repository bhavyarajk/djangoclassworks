# #Sum of elements
#
# # given a list
#sum of all numbers greater than 50
# # l=[11,34,67,23,90]
# # sum=0
# # for i in l:
# #     if i>50:
# #         sum=sum+i
# # print(sum)
# # #
# # #sum of all elements in the range(1,20)
# #
# # sum=0
# # for i in range(1,21):
# #     sum=sum+i
# # print(sum)
#
# # #Given a dictionary
# #
# # d={'num1':34,'num2':55,'num3':89,'num4':60,'num5':14}
# #
# # #sum of all even values
# #
# # sum=0
# #
# # for i in d.values():
# #     if(i%2==0):
# #         sum=sum+i
# #
# # print(sum)
#
# #Factorial of a number
# # num=int(input("Enter the number"))
# # fact=1
# #
# # for i in range(1,num+1):
# #     fact=fact*i
# # print(fact)
#
#
#
# #Multiplication table of a number
# num=int(input("Enter the number"))
# for i in range(1,11):
#     print(num*i,end="  ")


#Factors of a number

# num=int(input("Enter the number"))
#
# for i in range(1,num+1):
#
#           if(num%i==0):
#                     print(i)


#
# Given a dictionary'

d={101:['Arun',23,'ekm'],
     102:['Anu',25,'tvm'],
      103:['Amal',27,'ekm'],
       104:['kiran',30,'tcr']}

# print all names from the given data

for i in d.values():
    print(i[0])

# print the average age of all the students

sum=0
for i in d.values():
    sum=sum+i[1]
average=sum/len(d)
print('Average',average)

# print the details of  the students whose place is 'ekm'
for i in d.values():
    if(i[2]=="ekm"):
        print(i)













