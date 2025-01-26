import os
def save_to_file(s:str):
    with open ('$1\$1.txt', 'a', encoding = 'utf-8') as file:
        file.write(s)
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
def main():
    isnotcorrect = True
    result = 0
    history_item = ''
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
                            history_item = f'{c}{a}={result}'+'\n'
                            print(history_item)
                            save_to_file(history_item)
                            isnotcorrect = True
                    else:
                        print('Enter first value')
                        a=float(input())
                        print('Enter second value')
                        b=float(input())
                        if c == '+':
                                result = a+b
                                history_item = f'{a}{c}{b}={result}'+'\n'
                                print(history_item)
                                save_to_file(history_item)
                        elif c == '-':
                                result = a-b
                                history_item = f'{a}{c}{b}={result}'+'\n'
                                print(history_item)
                                save_to_file(history_item)
                        elif c == '*':
                                result = a*b
                                history_item = f'{a}{c}{b}={result}'+'\n'
                                print(history_item)
                                save_to_file(history_item)
                        elif c == '/':
                                result = a/b
                                history_item = f'{a}{c}{b}={result}'+'\n'
                                print(history_item)
                                save_to_file(history_item)
                        elif c == '^':
                                if b<0:
                                    result = power_negative(a,b)
                                else:
                                    result = power(a,b)
                                history_item = f'{a}{c}{b}={result}'+'\n'
                                print(history_item)
                                save_to_file(history_item)        
                else:
                    raise ValueError('Not corrected operation')
        except ValueError as e:
                print(f"Error: {e}")
                isnotcorrect = True
        except ZeroDivisionError:
            print('Can not division operation by 0')
            isnotcorrect = True
       

      
        

        