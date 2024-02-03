class Computer:
    def __init__(self,name,os,cpu):
        self.comp_name=name
        self.comp_os=self.OS(os) #instance of os object
        self.comp_cpu=self.CPU(cpu) #instance of cpu object
    
    def __str__(self):
        return f'Name:{self.comp_name} OS:{self.comp_os.get_os()} CPU:{self.comp_cpu}'
        #if you dont write method here it will return instances
    class OS: #inner class
        def __init__(self,os):
            self.name=os
        
        def get_os(self):
            return self.name
    
    class CPU:
        def __init__(self,cpu):
            self.manufacturer=cpu
        def get_cpu(self):
            return self.manufacturer

u1=Computer('pc1','windows','intel')
print(u1)