import random
class Dice:
    def __init__(self,sides):
        self.dice_sides=sides
    def roll_dice(self):
        print(f'After rolling dice:{random.randint(1,self.dice_sides)}')

d=Dice(6)#for 1 dice
d.roll_dice()
d.roll_dice()
d.roll_dice()
print('--------------------------------------')
d1=Dice(12) #2 dices
d1.roll_dice()
d.roll_dice()


