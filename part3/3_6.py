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



