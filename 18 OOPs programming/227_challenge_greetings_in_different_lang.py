

class English:
    def greeting():
        print('English')



class Hindi:
    def greeting():
        print('Namaskar')


def greet(greet_obj):
    greet_obj.greeting()

e1=English
greet(e1)
h1=Hindi
greet(h1)