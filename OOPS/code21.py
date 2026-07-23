'''
filter
filter as the name suggest is used to filter out the stuff
takes a list (or other sequence)
checks each item using a function (test)
keeps only the items that pass the test
works only on true or false
'''

def even(x):
    if x%2==0:
        return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9]

result = filter(even,a)

print(list(result))

# or

output = filter(lambda x : True if x%2 == 0 else False, a)
print(list(output))
