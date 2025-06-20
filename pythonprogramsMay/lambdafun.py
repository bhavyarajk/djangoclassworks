# #LAMBDA
#
# #Square of a number
# s=lambda x:x**2
# print(s(5))
#
# #Addition of two numbers
# sum=lambda a,b:a+b
# print(sum(3,5))
#
# #Product of two numbers
# product=lambda a,b:a*b
# print(product(5,8))
#
# #Square root of a number
# s=lambda x:x**0.5
# print(s(5))
#
# #length of a string
# s="hello"
# l=lambda x:len(x)
# print(l(s))
#
# # #name value from a dictionary
# # d={'name':'arun','age':23,'place':'ekm'}
# # n=lambda x:x['name']
# #
# # #first index of a list
# # colors=['red','green','blue','black']
# # # first=lambda l:l[0]
# # # print(first(colors))
# #
# # def first(l):
# #     return l[0]
# #
# # print(first(colors))
#
# #MAP
# l=[1,2,3,4]
# #create a list of squares
# print(map(lambda x:x**2,l))
# print(list(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))
#
# # #create a list of names
# # d=[{'name':'arun','age':23},{'name':'amal','age':25},{'name':'anu','age':34}]
# #
# # #map(function,sequence)
# # print(list(map(lambda x:x['name'],d)))
# #
# # #create a list of authors
# # l=[['book1','john',300],['book2','sam',350],['book3','mike',200]]
# # print(list(map(lambda x:x[1],l)))
# #
# # #create a list of length
# # s=['red','green','blue','orange','yellow','orange']
# # print(map(list(lambda x:len(x),s)))
# #
# # #create a list of square roots
# # l=[16,25,81,100,4]
# #
# # print(list(map(lambda x:x**0.5,l)))
#
#
# #FILTER
# #Given a sequence
#
# n=[23,78,12,81,10,52]
# print(list(filter(lambda x:x%2!=0 and x>50,n)))
#
# # filter odd numbers whose value
# # is greater 50
#
# #Given a sequence
# l=['apple','orange','pineapple','avocado']
# # filter the elements whose length
# #
# # is greater than 5
# print(list(filter(lambda x:len(x)>5,l)))



#REDUCE FUNCTION

#sum of elements in a list
#
# l=[1,2,3,4]
#
# import functools
# print(functools.reduce(lambda a,b:a+b,l))

# Given a sequence
#
l=[-12,9,56,11,-7,-3,-1,90,45,22,-16]
# import functools
# # sum of positive odd numbers
# y=list(filter(lambda x:x%2!=0 and x>0,l))
# print("Sum of Positive odd numbers",functools.reduce(lambda a,b:a+b,y))
#
# # sum of negative odd numbers
# y=list(filter(lambda x:x%2!=0 and x<0,l))
# print("Sum of Negative odd numbers",functools.reduce(lambda a,b:a+b,y))
# # sum of positive even numbers
# y=list(filter(lambda x:x%2==0 and x>0,l))
# print("Sum of Positive even numbers",functools.reduce(lambda a,b:a+b,y))
# # sum of negative even numbers
# y=list(filter(lambda x:x%2==0 and x<0,l))
# print("Sum of Negative even numbers",functools.reduce(lambda a,b:a+b,y))
# count of positive numbers
y=list(filter(lambda x:x>0,l))
print("count of positive numbers",len(y))
# count of negative numbers
y=list(filter(lambda x:x<0,l))
print("count of negative numbers",len(y))
# Use filter() and reduce()












