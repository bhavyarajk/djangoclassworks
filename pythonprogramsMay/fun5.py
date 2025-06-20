# eg:
#
# Define a function(using string parameter)
# to find the number of occurence each character
# in the given string
#
# s="hello world"
#
#
# output:
#    {'h':1,'e':1,'l':3,'o':2,'w':1,'r':1,'d':1}
def count_occurence(s):

    d={}

    for i in s:
       if(i!=" "):
            # if i not in d :
            #     d[i]=1
            # else:
            #     d[i]+=1
            d[i]=s.count(i)
    print(d)

s="hello world"

count_occurence(s)