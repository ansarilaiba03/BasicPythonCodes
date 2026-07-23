def decorate(func):
    def wrapper(*args,**kwargs):
        print("The addition is: ")
        func(*args,**kwargs)
        print("thankyou")
    return wrapper

@decorate
def addition(a,b,c,d):
    print(a+b+c+d)

addition(10,10,10,10)
