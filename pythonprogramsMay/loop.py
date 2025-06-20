# print('hello')
# print('hello')
# print('hello')
# print('hello')
# print('hello')


#While loop
#
# i=1   #iterating variable
#
# while(i<=10):   #if condition true it will execute print statement inside the loop
#     print('hello')
#     i=i+1

#1,2,3,....10
# i=1
# while(i<=10):
#     print(i)
# #     i=i+1
# #1,3,5,7,9,11
#
# # i=1
# # while(i<=11):
# #     print(i)
# #     i=i+2
#
# #5,4,3,2,1                     #-1
# i=5
# while(i>=1):
#     print(i,end=" ")
#     i=i-1
# print()
# #-8,-6,-4,-2,0                 #-2
# i=-8
# while(i<=0):
#     print(i,end=" ")
#     i=i+2
# print()
# #4,9,14,19,24,29,34            #+5
# i=4
# while(i<=34):
#     print(i,end=" ")
#     i+=5
# print()
# #3,6,12,24,48,96                #*2
# i=3
# while(i<=96):
#     print(i,end=" ")
#     i*=2
# print()
# #1,4,9,16,25,36,49              #**2
# i=1
# while(i<=7):
#     print(i**2,end=" ")
#     i=i+1
# print()
# #10,20,30,40,50,60,70,80,90,100  #+10
# i=10
# while(i<=100):
#     print(i,end="")
#     i=i+10
# print()


#1,2,4,7,11,16,22

#Write a program to print those numbers that are divisible by 2 in the range(1,100)

# i=1
# while(i<=100):
#     if(i%2==0):
#
#         print(i,end=" ")
#     i=i+1

#print all 3 digit numbers  (100-999)
# i=100
# # while(i<=999):
# #     print(i,end=" ")
# #     i=i+1
#
# # #print all 3 digit numbers divisible by 5
# #
# # # i=100
# # # while(i<=999):
# # #     if(i%5==0):
# # #         print(i,end=" ")
# # #     i=i+1
# #
# # #print those numbers that are divisible by 7 and 3 in the range 100-400
# #
# # #100-400
# # i=100
# # while(i<=400):
# #     if(i%7==0 and i%3==0):
# #         print(i)
# #     i=i+1
#
# #print those numbers that are not divisible by 7 or 3 in the range 100-400
# #
# # i=100
# # while(i<=400):
# #    if not(i%7==0 or i%3==0):
# #         print(i)
# #    i=i+1
#
#
# #Count of numbers
# #count all even numbers in the range 1-100
#
# i=1
# count=0 #before the loop count variable set to 0
# while(i<=100):
#     if(i%2==0):
#         print(i)
#         count=count+1  #After each print statement increments count by 1
#     i=i+1
# print("count of even numbers",count)  #After the loop print the total count
#
#
# #count of all 4 digit numbers that are divisible by 7
#
# # i=1000
# # count=0
# # while(i<=9999):
# #     if(i%7==0):
# #         print(i)
# #         count=count+1
# #     i=i+1
# #
# # print("count of numbers that are divisible by 7",count)
#
# #sum of numbers
# sum=0
#
# # i=1
# # while(i<=5):
# #      # print(i)
# #      sum=sum+i    #0+1+2+3+4+5
# #      i=i+1
# # print(sum)
# #
# # #product of numbers
# # product=1
# #
# # i=1
# # while(i<=5):
# #      # print(i)
# #      product=product*i  #1*1*2*3*4*5
# #      i=i+1
# # print(product)
#
# #Find
# # Sum
# # product
# # count
# # of all two digit numbers that are divisible by 3 and 5 .
#
# # i=10
# # sum=0
# # product=1
# # count=0
# #
# # while(i<=99):
# #     if(i%3==0 and i%5==0):
# #         sum+=i
# # #         product*=i
# # #         count+=1
# # #
# # #     i=i+1
# # # print(sum)
# # # print(product)
# # # print(count)
# #
# # #Factorial of a number
# #
# # num=int(input("Enter the number"))
# #
# # i=1
# # fact=1
# while(i<=num):
#    fact=fact*i
#
#    i=i+1
#
# print("factorial",fact)

#Print each characters in the string
# s=input("Enter the string")
# l=len(s)
# i=0
# while(i<=l-1):
#     print(s[i])
#     i=i+1

#Multiplication Table of a number
num=int(input("Enter the number"))

i=1
while(i<=10):
      print(num,"*",i,"=",num*i)
      i=i+1







































