import os
def main():
    isnotcorrect = True
    while isnotcorrect:
        print('\n\n\t Files Mode')
        try:
                print('Possible operations')
                operation_desc = [
                'q -- quit files mode',
                'ls -- display a list of files in the current directory',
                'cd $1 -- go to the specified directory (.. - move up one level)',
                'pwd -- print current path',
                'head $1 -- display the first 512 bytes of the specified file',
                ]
                operations = ['q','ls','cd $1','pwd','head $1']
                for item in operation_desc:
                    print(item)
                print('Enter an operation')
                c=str(input())
                if c in operations or 'cd' in c or 'head' in c:
                    if c == 'q':
                            print('Quit from files mode')
                            isnotcorrect = False
                    if c == 'ls':
                        print('Display a list of files in the current directory')
                        curdir = os.getcwd()
                        print(f'current directory {curdir}')
                        files_folders = os.listdir(curdir)
                        print('content of directory:')
                        for item in files_folders:
                            print(item)
                        isnotcorrect = True
                    if 'cd' in c:
                        words = c.split()
                        if len(words)>2:
                             raise FileNotFoundError('Error')
                        if len(words)==1:
                            print('Write directory name after cd with space')
                        if len(words)==2:
                            if words[1]=='..':
                                os.chdir('..')
                            else:
                                os.chdir(words[1])
                        isnotcorrect = True
                    if c == 'pwd':
                        print(os.getcwd())
                        isnotcorrect = True
                    if 'head' in c:
                        words = c.split()
                        if len(words)>2:
                             raise FileNotFoundError('Error')
                        if len(words)==1:
                            print('Write file name after head with space')
                        if len(words)==2:
                            curdir = os.getcwd()
                            files_folders = os.listdir(curdir)
                            for item in files_folders:
                                if words[1] in item:
                                    with open(item,'rb') as file:
                                        data = file.read(512)
                                        print(data)
        except FileNotFoundError:
            print("Not found, error!")
            isnotcorrect = True
        except PermissionError:
            print("Permission denied, error!")
            isnotcorrect = True
