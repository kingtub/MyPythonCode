# 压缩文件
import io
import gzip
sio = io.StringIO()
i = 0
while i < 100:
    i += 1
    sio.write('asddffgghhhjjjjjjjcddsdsdssffdsfdsfdsfdsfddsfdsfdf')

with gzip.open(r'C:\Users\李金华\Downloads\co.gz', 'wt') as f:
    f.write(sio.getvalue())

with gzip.open(r'C:\Users\李金华\Downloads\co.gz', 'rt') as f:
    text = f.read()
    print(text)

