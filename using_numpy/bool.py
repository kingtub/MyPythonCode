import numpy as np

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

b = arr < 6 # 结果b是一个布尔数组， 形状如arr
c = np.zeros_like(arr)
c[b] = 1  # 在小于6的元素位置做个标记
print('b:', b)
print('c:', c)
print(np.sum(c))
print('accuryRate:', np.sum(c)/float(c.size))

print(np.percentile(arr, 50))
print(np.percentile(arr, 25))