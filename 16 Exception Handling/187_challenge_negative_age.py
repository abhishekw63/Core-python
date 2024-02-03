class NegativeAge(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return 'NegativeAgeError:'+self.msg

def stage(age):
    if age<0:
        raise NegativeAge('negative age is not permitted')
    elif age>=0 and age<10:
        print('child')
    elif age>=10 and age<20:
        print('teenager')
    elif age>=20 and age<50:
        print("adult")
    else:
        print('senior citizer')

age=-2
msg=''
try:
   msg=stage(age)
except NegativeAge as error:
    print(error)