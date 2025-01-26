import importlib
import Calculator
import files
isnotcorrect = True
while isnotcorrect:
    print('\n\n\t General Program')
    try:
            print('Possible operations')
            operation_desc = [
            'quit -- quit the program',
            'calc -- Calculator Mode',
            'files -- Files Mode',
            ]
            operation = ['quit','calc','files']
            for item in operation_desc:
                print(item)
            print('Enter an operation')
            c=str(input())
            if c in operation:
                if c == 'quit':
                        print('Quit from program')
                        isnotcorrect = False
                elif c == 'calc':
                        Calculator.main()
                        isnotcorrect = True
                elif c == 'files':
                        files.main()
                        isnotcorrect = True
            else:
                raise ValueError('Not corrected operation')
    except ValueError as e:
        print(f"Error: {e}")
        isnotcorrect = True


