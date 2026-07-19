a = {1,2,3,4,5}
b = {4,5,6,7,8}

s = a.union(b)
print(f"union: {s}")
#or
s = a|b
print(f"union: {s}")


r = a.intersection(b)
print(f"intersection: {r}")
#or
r = a&b
print(f"intersection: {r}")


t = a.difference(b)
u = b.difference(a)
print(f"difference a = {t}")
print(f"difference b = {u}")
#or
t = a-b
u = b-a
print(f"difference a = {t}")
print(f"difference b = {u}")


v = a.symmetric_difference(b)
print(f"symmetric difference: {v}")
#or
v = a^b
print(f"symmetric difference: {v}")