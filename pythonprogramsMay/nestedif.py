# #write a program to check whether the given number is a positive even or
# #a positive odd or a negative even or a negative odd number
# n=int(input("Enter the number"))
#
# # if(n>0):
# #      if(n%2==0):
# #           print("positive even")
# #      else:
# #           print("positive odd")
# #
# # else:
# #     if(n%2==0):
# #            print("negative even")
# #     else:
# #            print("negative odd")

n=int(input("Enter the number"))

if(n%2==0):
     if(n%3==0):
          print("divisible by 2 and 3")
     else:
          print("divisible by 2 and not by 3")

else:
    if(n%3==0):
           print("divisible by 3 and not by 2")
    else:
           print("not by 2 and 3")
