aList = [1, 4, 6, 4]

# 在列表末尾添加新的对象
aList.append(5)
print(aList)

# 统计某个元素在列表中出现的次数
print('aList.count(4)=', aList.count(4))
print('aList.count(6)=', aList.count(6))


# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
aSeq = [2, 3, 8]
aList.extend(aSeq)
print(aList)

# 从列表中找出某个值第一个匹配项的索引位置
print(aList.index(4))

# 将对象插入列表
aList.insert(1, 9)
print(aList)

# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(aList.pop())
print(aList)

# 移除列表中某个值的第一个匹配项
aList.remove(4)
print(aList)

# 反向列表中元素
print('reverse=', aList.reverse())
print(aList)

# 对原列表进行排序
aList.sort()
print(aList)
