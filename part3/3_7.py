# -*- coding: utf-8 -*-

# Noneについて

# Noneは偽として扱われる
if None:
    print ('None is ture!')
else:
    print ('None is false')

# Noneの判定
y = None
if y is None:
    print ('y is None')

# FalseとNoneの違い
y = False

if y is None:
    print('y is None')
else:
    print('y is not None')

