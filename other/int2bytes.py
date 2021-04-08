x = 935
bs = x.to_bytes(4, "big")
k = int.from_bytes(bs, 'big')
print(k)  # 935
print(935 % 256)  # 167
print(935 / 256)  # 3.65234375
print(bs[2])  # 3
print(bs[3])  # 167
