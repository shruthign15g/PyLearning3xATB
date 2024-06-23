
# Decorators : Decorators are nothing but the functions which takes a function as an
# argument and returns a function.

def mydecorator(func):
    def inner():
        print("Before function execution")
        func()
        print("After function execution")
    return inner

def my_decorator(funca):

    def wrapper():
        print("Execution begins...............")
        print("*******************************")
        funca()
        print("*******************************")
        print("Execution Ends")

    return wrapper()

@my_decorator
def say_hello():
    print("Shruthi")
def say_hello123():
    print("Vachu")


my_decorator (say_hello123)()


