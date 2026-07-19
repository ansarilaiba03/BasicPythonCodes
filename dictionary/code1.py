'''
Dictionary 
syntax = {}, if we'll check the type then it is dictionary not set
s = {1,2,3,4} = this is set
s = {1:"hello", 2:33} = this is dictionary

properties:
mutable = can change the element, unlike set
duplicates = allowed
order= there is no indexing but there is keys {1:"hello"} so '1' is a key
'''

d = {10:100, 20:200, 30:300, 40:400}

d[10] = 1000 #updating
d[50] = 500 #creating, since does not exist
del d[30] #deleting

print(d)

#traversing

a = {10:100, 20:200, 30:300, 40:400}

for i in a:
    print(a[i])