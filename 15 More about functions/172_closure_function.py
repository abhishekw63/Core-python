def fun1(msg):
    #msg='hello'
    def inner_fun1():
        print('*' * 10)
        print(msg)
        print('*' * 10)
    
    return inner_fun1

returned=fun1('abhishek')
returned()