def power(a,b):
    res = 1
    for i in range(int(b)):
          a=1/(a**b)
          res *= a
    return res
def power_negative(a,b):
    b=b*(-1)
    res = 1/power(a,b)
    return res
def factorial(a):
    if a == 0:
        return 1
    elif a > 0:
        return a*factorial(a-1)
    else:
        raise ValueError('Must be more than 0')
import os
isnotcorrect = True
result = 0
while isnotcorrect:
    print('\n\n\t Calculator Mode')
    try:
            print('Possible operations')
            operation_desc = [
            'q -- quit calculator mode',
            '+ -- addition operation',
            '- -- subtraction opration',
            '* -- multiplication operation',
            '/ -- division operation',
            '! -- factorial operation',
            '^ -- operation of reduction to power'
            ]
            operations = ['q','+','-','*','/','!','^']
            for item in operation_desc:
                print(item)
            print('Enter an operation')
            c=str(input())
            if c in operations:
                if c == 'q':
                        print('Quit from calculator')
                        isnotcorrect = False
                elif c == '!':
                        print('Enter value')
                        a=int(input())
                        result = factorial(a)
                        print(a,c,'=',result)
                        isnotcorrect = True
                else:
                    print('Enter first value')
                    a=float(input())
                    print('Enter second value')
                    b=float(input())
                
                    if c == '+':
                            result = a+b
                            print(a,c,b,'=',result)
                    elif c == '-':
                            result = a-b
                            print(a,c,b,'=',result)
                    elif c == '*':
                            result = a*b
                            print(a,c,b,'=',result)
                    elif c == '/':
                            result = a/b
                            print(a,c,b,'=',result)
                    elif c == '^':
                            if b<0:
                                result = power_negative(a,b)
                            else:
                                result = power(a,b)
                            print(a,c,b,'=',result)                
            else:
                raise ValueError('Not corrected operation')
    except ValueError as e:
            print(f"Error: {e}")
            isnotcorrect = True
            os.system('cls')
    except ZeroDivisionError:
        print('Can not division operation by 0')
        isnotcorrect = True
        os.system('cls')

      
        

        