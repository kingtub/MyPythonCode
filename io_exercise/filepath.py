import os

# 根据文件路径名，提取文件名、文件夹名
path = '/Users/beazley/Data/data.csv'

# Get the last component of the path
print(os.path.basename(path))
# Get the directory name
print(os.path.dirname(path))

# 拼接文件路径
# Join path components together
print(os.path.join('tmp', 'li', 'da'))

# 提取文件扩展名
# Split the file extension
print(os.path.splitext(path))
