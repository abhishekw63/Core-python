day=int(input('enter the number:'))

match day:
    case 1:
        print('sunday')
    case 2:
        print('monday')
    case 3:
        print('tuesday')
    case 4:
        print('wednesday')
    case 5:
        print('thursday')
    case 6:
        print('friday')
    case 7: 
        print('saturday')
    case _:
        print('holiday')
    
