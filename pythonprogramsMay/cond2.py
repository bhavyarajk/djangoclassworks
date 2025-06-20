# # write a program to check whether an entered character is vowel or not
# #
# # ch=input("Enter the character")
# #
# # vowels="aeiouAEIOU"  #or we can use vowels=['a','e','i','o','u','A,'E','I','O','U'] or set or tuple
# # if (ch in vowels):
# #     print("Entered character is vowel")
# # else:
# #     print("not a vowel")
#
#
#
#
# # #write a program to check whether the last digit of a number is divisible by 3 or not
# #1 method
# n=int(input("Enter the number"))
# last_digit=n%10
# if(last_digit%3==0):
#     print("last digit is divisible by 3")
# else:
#     print("not divisible")

#
# #2 method
# # n=int(input("Enter the number"))
# # s=str(n)#we can directly take each digit  from a string using index
# # if(int(s[-1])%3==0):
# #     print("last digit is divisible by 3")
# # else:
# #     print("not divisible")
#
#
#
#
# # # #write a program to check whether the entered number is  a 2 digit number
# n=int(input("Enter the number"))
# if(10<=n<=99):
#     print("2 digit number")
# else:
#     print("not 2 digit number")



#
# # #write a program to check whether the two strings are equal or not
# s1=input("Enter the first string")
# s2=input("Enter the second string")
# if(s1==s2):
#     print("equal")
# else:
#     print("not equal")


#write a program to check whether a string is palindrome or not
#palindrome means string and its reversed string are same

s=input("Enter the string")
rev=s[::-1]
if(s==rev):
    print("Palindrome")
else:
    print("not Palindrome")



#write a program to check an entered number is present in the given list or not
# l=[1,2,3,4,5,6]
# num=int(input("Enter the number"))
# if (num in l):
#     print("Entered number is present")
# else:
#     print("not present")

# # #write a program to check a particular key is present in a dictionary or not
# d={100:'Arun',101:'Amal',102:'Anu'}
# key=int(input("Enter the key to be searched"))
# if key in d:
#     print("key is present")
# else:
#     print("key is not present")

#Write a program to check whether the entered "location name" contains the word 'land'
location=input("Enter the location name")
if 'land' in location:
    print("present")
else:
    print("not present")