'''
lambda function:
it is an anonymous, inline function defined using the lambda keyword
it's often used for short, simple function that are used only once or temporary
you can have multiple arduments but there will be only one expression

'''

addition = lambda a: "even" if a%2 ==0 else "odd"
print(addition(10))

addition = lambda a,b:a+b
print(addition(10,10))