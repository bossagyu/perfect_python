# -*- coding: utf-8 -*-

d = {
    'key1' : 'val1',
    'key2' : 'val2',
    'key3' : 'val3',
    'key4' : 'val4'
}


# インデックスアクセス
print d['key1']

flag = 'key1' in d
print "%d" % flag

# インデクスがない場合はnoneが返る
print d.get('key4')
print d.get('key10')


# イテレーションアクセス
for key in d:
    print key


for value in d.values():
    print value

for key,value in d.items():
    print (key,value)

# 辞書の更新
d['key1'] = 'vala'
print d['key1']

# 辞書に追加
d['key5'] = 'val5'

for key,value in d.items():
    print (key,value)


# 辞書からキーを削除
del d['key2']

print "del key2"
for key,value in d.items():
    print (key,value)

