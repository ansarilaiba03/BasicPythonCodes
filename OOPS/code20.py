'''
maps 
map is used for applying a function to mulplt items
takes a list (or any sequence (typle,set,etc))
applies the same funtion to every item in that list
gives you back a new list
'''

a = [1,2,3,4,5]

result = map(lambda x: x**x , a)
print(list(result))

# or

def double(y):
    return y**2

output = map(double, a)
print(list(output))