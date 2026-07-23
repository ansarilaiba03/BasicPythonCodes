'''
comprehensions:
comprehensions are used to create list, dictionary and sets, but you don't have to use multilpe lines of code for loops and if-else statements

'''

#LIST
# l = []
# for i in range(1,21,1):
#     if i%2==0:
#         l.append(i)
# print(l)

# OR

l = [i for i in range(1,21) if i%2==0]
print(l)


#DICTIONARY

l = {i: i**2 for i in range(1,11)} 
print(l)