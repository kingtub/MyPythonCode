import os

# 判断文件、文件夹是否存在
print(os.path.exists('C:\D\Code\Octave\MyOctaveCode\Statements'))
print(os.path.exists('C:\D\Code\Octave\MyOctaveCode'))
print(os.path.exists('C:\D\Code\Octave\MyOctave'))

file = ['C:\D\Code\Octave\MyOctaveCode\Statements', 'C:\D\Code\Octave\MyOctaveCode\Statements\IfTest.m',
        r'C:\Users\Public\Desktop\Notepad++.lnk', ]

# 判断文件类型
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

# 获取文件大小
print('size1', os.path.getsize('C:\D\Code\Octave\MyOctaveCode\Statements\IfTest.m'))

