# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO顾名思义就是在内存中读写str。
import io
s = io.StringIO()
with open('C:\D\Code\Python\MyPythonCode\io_exercise\string_io.py', 'rt', encoding='utf-8') as f:
    for line in f:
        s.write(line)

print(s.getvalue())

