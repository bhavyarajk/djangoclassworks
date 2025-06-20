# # l=[12,56,34,90,11,55]
# #
# # new=[i for i in l if i%2==0]
# #
# # print(new)
#
# #
# l=['apple','banana','orange','pineapple','avocado']
#
# new=[i for i in l if len(i)>5]
# print(new)
# #
# # create a new list with elements whose length>5
# #
# # l=[12,39,'hello',8.7,-90,-11,5]
# # #
# # # create a new list with only string types
# # new=[i for i in l if type(i)==str]
# # print(new)
# # #
# # # create a new list with only positive values
# # new=[i for i in l if type(i)!=str and i>0]
# # print(new)
# # # create a new list with only float values
# # new=[i for i in l if type(i)==float]
# # print(new)
# #
# # #Creating a list with elements whose value is divisible by 3 in the range 1,100
# # new=[i for i in range(1,100) if i%3==0]
# # print(new)
#
#
# #Set Comprehension
#
# s="hello world"
#
# new={i for i in s}
# print(new)
#
# new={i for i in s if i!=" "}
# print(new)
from ctypes.wintypes import PWORD

#Dictionary Comprehension

l=[1,2,3,4]

new={i:i**2 for i in l}
print(new)

new={i:l[i] for i in range(len(l))}
print(new)

#Given a string s

s="python is a programming language"

#creating a dictionary where keys the words in the sentence and values are the length of each word.

# l=s.split()

new={i:len(i) for i in s.split()}

print(new)
















