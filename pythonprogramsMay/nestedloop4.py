# **
# **
# ****
# ****
# ******
# ******
# ********
# ********


# * *
# * * * *
# * * * * * *
# * * * * * * * *

# for i in range(2,9,2):
#     for p in range(2):
#         for j in range(1,i+1):
#             print('*',end=" ")
#         print()

k=3*2
for i in range(1,9,2):
    for p in range(1,k+1):
        print(end=" ")
    k=k-2
    for j in range(1,i+1):
        if(j%2==0):
            print('A',end=" ")
        else:
            print('1',end=" ")

    print()


