def planet(id):
    if id>0 and id<=9:
        dict1={
            1:'Mercury',
            2:'Venus',
            3:'Earth',
            4:'Mars',
            5:'Jupiter',
            6:'Saturn',
            7:'Uranus',
            8:'Neptune',
            9:'Pluto'
        }
        print(f'Id is {id} and correspoinding planet is {dict1[id]}.')
    else:
        print('invalid id '+ str(id)+'.')

planet(90)