'''
Sets
we use {} brackets 
it is mutable, meaning we can change the value of a set
eg. a = {1,2,3,4}
    a[0] = 12
    this is accepted

duplicate values are not allowed... if it is present, it will not print the dupliacte number 

unordered= meaning it does not have an index so you cannot access it using indexing
'''

a = {1,2,3,4}

a.remove(4)  #remove element
a.discard(2) #remove element
a.add(10)    #add element

print(a)

a.pop()    #removes element, mostly first element
print(a)
a.pop()
print(a)

b={1,2,3,4,5,6,9}

b.clear() #removes all elements

print(f"b= {b}")