'''
args and kwargs
you always don't have to use args and kwargs the main thing is *, ** you can use any names in front of them

args = arguments
prints a tuple
'''

def addition(*args):
    sum = 0
    for i in args:
        sum += i
    print(f"sum : {sum}")

addition(1,2,3,4,5,6,7,8,9)