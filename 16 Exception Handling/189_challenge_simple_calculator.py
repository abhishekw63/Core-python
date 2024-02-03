class InvalidFormulaException(Exception): #creating a custom exception class
    pass

def evaluate(expression):
    expression_list=expression.split()
    if len(expression_list)< 3:
        raise InvalidFormulaException('Formula should be in this form, ex:10 + 15')
    else:
        num1=int(expression_list[0])
        num2=int(expression_list[2])
        operand=expression_list[1]

        if operand=='+' or operand=='-' or operand=='/' or operand=='*':
            if operand=='-':
                print(num1-num2)
            elif operand=='*':
                print(num1*num2)
            elif operand=='/':
                print(num1/num2)
            else:
                print(num1+num2)

        else:
            raise InvalidFormulaException('Formula should be in this form, ex:10 + 15') 

try:
    evaluate('10+15')
except  InvalidFormulaException as err:
    print(err)
'''
10 ? 15
10+15

'''