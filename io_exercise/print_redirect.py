# 把当前Python文件复制到我指定的目标去
with open(r'C:\Users\李金华\Downloads\py.txt', 'wt') as fw:
    with open('C:\D\Code\Python\MyPythonCode\io_exercise\print_redirect.py', 'rt') as fr:
        for line in fr:
            print(line, file=fw, end='')
