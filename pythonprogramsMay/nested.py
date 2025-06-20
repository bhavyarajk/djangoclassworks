#Nested Loop

l=['kelly','jenny','emy']

for i in l:
    for j in range(1,4):
        print(i,end="")
    print()


# 1 1 1
# 2 2 2
# 3 3 3

for i in range(1,4): #1,2,3
    for j in range(1,6):
        print(i,end=" ")
    print()
