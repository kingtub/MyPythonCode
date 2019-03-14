# 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
seq = ('name', 'age', 'sex')
aDict = dict.fromkeys(seq)
print("New Dictionary : {}".format(str(aDict)))
aDict2 = dict.fromkeys(seq, 10)
print("New Dictionary : {}".format(str(aDict2)))