# -*- coding: utf-8 -*-

from collections import OrderedDict

# OrderdDictを利用すると辞書の順序を保証できる
od = OrderedDict()

od['b'] = 1
od['1'] = 2
od['aa'] = 3
od['0'] = 4

for k,v in od.items():
    print('{}:{}'.format(k,v))

