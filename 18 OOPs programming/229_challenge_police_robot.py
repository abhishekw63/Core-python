'''
->overriding the function.
'''

class Robo:
    def __init__(self,name):
        self.robo_name=name
    def msg(self):
        print(f'Hello! this is {self.robo_name}')

class PoliceRobot(Robo):
    def msg(self):
        print(f'Hey there!  i am {self.robo_name}')


r1=PoliceRobot('Abhishrk')
r1.msg()

r2=Robo('jogn')
r2.msg()