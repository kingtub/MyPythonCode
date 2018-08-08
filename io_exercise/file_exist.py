import os

# 判断文件、文件夹是否存在
print(os.path.exists('C:\D\Code\Octave\MyOctaveCode\Statements'))
print(os.path.exists('C:\D\Code\Octave\MyOctaveCode'))
print(os.path.exists('C:\D\Code\Octave\MyOctave'))

file = ['C:\D\Code\Octave\MyOctaveCode\Statements', 'C:\D\Code\Octave\MyOctaveCode\Statements\IfTest.m',
        r'C:\Users\Public\Desktop\Notepad++.lnk', ]

for p in file:
    if os.path.isdir(p):
        print(p, 'is a dir')
    elif os.path.isfile(p):
        print(p, 'is a file')
    elif os.path.islink(p):
        # Is a symbolic link
        print(p, 'is a link file')
        # Get the file linked to
        print('{}\'s realpath is'.format(p), os.path.realpath(p))