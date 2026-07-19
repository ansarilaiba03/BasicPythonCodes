# find the second greatest element

a = [1,3,6,66,77,33,68]

larg = a[0]
sec_larg = a[0]

for i in a:
    if i > larg:
        sec_larg = larg
        larg = i
    elif i > sec_larg:
        sec_larg = i
    
print(f"largest: {larg} and second largest: {sec_larg}")