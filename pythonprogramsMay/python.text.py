# #Features
# from unicodedata import numeric
#
# #Datatypes
# numeric  -int,float,complex
# text  -string('')
# list  -[]
# tuple -()
# dictionary-{key:value}
# set -{}
# boolean-True or False
# none -None


# Q1.
# Given a dictionary

d={'title':'ABC','author':'john','price':200}

   # a).print all the values inside the dictionary
print(d.values())
   # b).Print all the keys of dictionary
print(d.keys())
   # c).print the value of a key 'price'
print(d['price'])
   #
   #  d).change the  'price' value into 300
d['price']=300
   #  e).Add new key value pair 'language':'english'
d['language']='english'
   #  f).print the length of dictionary
print(len(d))
   #
# Q2.
l={'emp001':['Arun','ekm',23],'empl002':['Amal','tvm',24],'emp003':['Anu','ekm',27]}

# a)print the names of all the employees
print(l['emp001'][0],l['emp002'][0],l['emp003'][0])
# b)print the average age from the given data
print((l['emp001'][2]+l['emp002'][2]+l['emp003'][2])/3)
# c)print the place of the employee with id 'emp003'
print(l['emp003'][1])
# d)change the place value of employee with id 'emp002'
l['emp002'][1]="tcr"

