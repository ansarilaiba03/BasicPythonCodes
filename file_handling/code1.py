'''
file handling means performing CRUD operations that is 
C - creating
R - Reading
U - Updating
D - Deleting

modes:
'r' = Read(default) - file must exist
'w' = write - creates a file or overwrites
'a' = append - adds to end of file
'x' = created - created a new file, fails if it exists
'''

p = open('if-else\code1.py')

print(p.read())