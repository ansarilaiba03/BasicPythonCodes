#find greatest element and print its index too

a = [1,5,588,662,84,99]

g = a[0]
index = 0

for i in range(1, len(a), 1):           
        if a[i]> g:
            g = a[i]
            index = i

print(f"index= {index} and number= {g}")