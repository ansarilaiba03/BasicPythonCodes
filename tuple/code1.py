''' difference between list and tuple
    in list we use [] bracket but in tuple we use () bracket 
    tuples are immutable, meaning we cannot change the value of tuple
    
    eg. a[1,2,3,4]
        a[0] = 12 
        this is accepted, but

        a(1,2,3,4)
        a[0] = 12 
        this is not accepted

    tuples are like string since strings are also immutable
 '''

a = (1,2,3,4,5,5,5, "hello", print())

index = a.index(5)

print(index)