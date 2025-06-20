# #write a program to check whether the entered number is 2 digit/3digit/4 digit number
# num=int(input("Enter the number"))
# if(10<=num<=99):
#     print("2 digit")
# elif(100<=num<=999):
#     print('3digit')
# elif(1000<=num<=9999):
#     print('4 digit')
# else:
# #     print('number is either single digit or more than 5 digit')
#
# # #write a program to print the Grade of a student based on entered score
# #
# # 91-100    Grade A
# # 81-90     Grade B
# # 71-80     Grade C
# # 61-70     Grade D
# # below 61  Grade E
#
# s=int(input("Enter the score"))
#
#
# # if(91<=s<=100):
# #     print('GradeA')
# # elif(81<=s<=90):
# #     print('GradeB')
# # elif(71<=s<=80):
# #     print('GradeC')
# # elif(61<=s<=70):
# #     print('GradeD')
# # elif(s<=60):
# #     print('GradeE')
# # else:
# #     print('invalid')
#
#
# #Write a Basic Calculator program to perform Arithmetic Operations(+,-,*,/)
#
# n1=int(input("Enter the number"))
# n2=int(input("Enter the number"))
# op=input("Enter the choice:+ ,- ,*, /")
# if(op=="+"):
#     print('sum',n1+n2)
# elif(op=="-"):
#     print('difference',n1-n2)
# elif(op=="*"):
#     print('product',n1*n2)
# elif(op=="/"):
#     print('Quotient',n1/n2)
# # else:
# #     print('invalid operation')
#
# #Write program to print the number of days in  a month
# #
# # #1st Method
# #
# # l1=['january','march','may','july','august','october','december'] #31 days
# # l2=['april','june','september','november']
# # l3=['february']
# #
# # month_name=input("enter the monthname")
# #
# # if (month_name in l1):
# #     print('31 days')
# # elif (month_name in l2):
# #     print('30days')
# # elif (month_name in l3):
# #     print('28 or 29 days')
# # else:
# #     print('invalid')
# #
# #2nd method
d={'january':31,'february':28,'march':31}

month_name=input("Enter the monthname")
if month_name in d:
    print(d[month_name])
else:
    print('invalid')
#


















