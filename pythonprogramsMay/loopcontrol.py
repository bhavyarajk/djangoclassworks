# #BREAK
#
# # s="hello"
# #
# # for i in s:
# #     if(i=="l"):
# #         break
# #     print(i)
# #
# # #Continue
# # s="hello"
# #
# # for i in s:
# #     if(i=="l"):
# #         continue
# #     print(i)
#
# #1
# s="python is a programming language"
#
# # print the string upto a specific character (including that character)
#
# for i in s:
#     print(i)
#     if(i=='a'):
#         break
#
#
#
# #2
# colors=['red','green','blue','black','orange','yellow']
#
# # print the first occurence of color value starting  with 'b'
# #print only the color values containing letter 'n'
#
# #Given a list
#
# l=[34,23,12,89,45]

# skip the even values and print only odd numbers


#print those numbers that are not divisible by 3 in the range(1,100)  using continue

# #
# l=[1,2,3,4]
# l1=[]
# sum=0
# for i in l:
#     sum=sum+i
#
# #
# #     l1.append(sum)
# # print(l1)
#
#
# #Reverse of a number
# #1st Method
# n=1234
# s=str(n)
# rev=""
# for i in s:
#      rev=i+rev
# print(rev)

#2nd Method

# n = 1234
# rev = 0
# while (n > 0):
#     digit = n % 10 #(lastdigit)
#
#     rev = rev * 10 + digit
#
#     n = n // 10 #(floordivision)
#
# print(rev)

#Sum of digits in a number
#
# n=5656
# s=str(n)
#
# sum=0
# for i in s:
#     sum=sum+int(i)
#
# print(sum)

# #Prime number
#
# n=int(input("Enter the number"))
# if(n>1):  #if number greater than 1
#     for i  in range(2,n):
#         if(n%i==0):
#             print("not prime")
#             break
#     else:
#         print("prime")
# else: #if n==1 or n==0 or negative number
#     print("not prime")










