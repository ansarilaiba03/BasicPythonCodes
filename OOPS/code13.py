'''
decorator: is just a function that modifies another function without changing its actual code
'''
def decorate(func):
    def wrapper():
        print("begin")
        func()
        print("end")
    return wrapper

@decorate
def hello():
    print("hello")

hello()
