
#Display the position of a particular character in a string
#
# s="python is a programming language"
# ch=input("Enter the character")
# print("position",s.index(ch))


#Find the largest element from the list
l=[34,67,90,12,45,23,11]
#using max()
# print(max(l))

#without using max() function
# max=l[0]
# for i in l:
#     if(i>max):
#         max=i
#
# print(max)

# #Find the second largest element from the list
l=[34,67,90,12,45,23,11]
l.sort()
print(l[-2])



# #Find the maximum length word from the string
s="python is a programming language"
l=s.split() #list of words
print(l)
length=max([len(i) for i in l])
print(length)

for i in l:
    if len(i)==length:
        print(i)
        break

#
#
# # #Find the smallest element from the list
# # # l=[34,67,90,12,45,23,11]
# # print(min(l))
# #or
# # min=l[0]
# # for i in l:
# #     if(i<max):
# #         min=i
# #
# # print(min)
#
#
# # #find second smallest from the list
# l=[34,67,90,12,45,23,11]
# l.sort()
# print(l[1])

#Find the common element from the given sequences

l1=[12,56,34,21,90]
l2=[56,24,89,11,12]

#1
# #intersection()
# s1=set(l1)
# s2=set(l2)
# print("common elements",s1.intersection(s2))

#2
for i in l1:
    if i in l2:
        print(i)



#Find the maximum salary from the given data

l={1:['arun',23,20000],2:['amal',26,30000],3:['kiran',25,35000]}

#max(seq)

new=[]
for i  in l.values():
    new.append(i[2])
print(new)
print(max(new))































