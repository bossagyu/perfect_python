# -*- coding: utf-8 -*-

x = [1,2,3.0,"a","bbb"]

# インデックシング
print x[0]

# インデックシング(後ろから)
print x[-1]

# リストのスライス
print x[1:3]
print x[1:]

# イテレーション
for item in x:
    print(item)

# リストの追加
x.append("aaaa")

for item in x:
    print(item)

# リストの更新
x[1] = "hoge"

print x[1:2]

# リストを逆順にする
x.reverse()


for item in x:
    print(item)


print "test"
print x
