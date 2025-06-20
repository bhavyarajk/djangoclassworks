



#1
# import mod1
# mod1.msg()
# print(mod1.x)


# 2
# from mod1 import msg,x
# msg()
#print(x)

#3
from mod3 import msg as m #import aliasing
from mod1 import msg

msg()
m()



