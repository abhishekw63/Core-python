'''
a class whose object can be used as function name or method is called caller class'''
class dept:
    def __init__(self):
        self.depts={'HR':"Human resources department",
                    'acc':'Account and finnace',
                    'ele':'Electrical Department',
                    }
    def __call__(self,dept):
        return self.depts[dept]

name=dept()
res=name('ele')
print(res)

print('*' * 100)

def Depts():
    depts={'HR':"Human resources department",
                    'acc':'Account and finnace',
                    'ele':'Electrical Department',
           }
    def dname(dept):
        return depts[dept]
    
    return dname

d=Depts()
res=d('HR')
print(res)        