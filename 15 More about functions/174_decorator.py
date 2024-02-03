'''def decorator(fun):
    def wrapper():
        print('*' * 10)
        fun()
        print('*' * 10)

    return wrapper


def display():
    print('hello1')

res=decorator(display)
res()'''

def decorator(fun):
    def wrapper(msg):
        print('*' * 10)
        fun(msg)
        print('*' * 10)

    return wrapper

@decorator#Using the @decorator syntax before defining a function indicates that the function should be decorated by the decorator function
def display(msg):
    print(msg)

'''res=decorator(display)
res('abhishek')'''

display('abhishek')