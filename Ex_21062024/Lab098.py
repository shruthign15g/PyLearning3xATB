def decorator2(func):
    def wrapper():
        print("Hello Shruthi")
        func()
    return wrapper
@decorator2
def hello():
    print("Good Morning")

hello()
