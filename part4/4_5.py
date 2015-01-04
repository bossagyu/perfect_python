# -*- coding: utf-8 -*-

result = [x**2 for x in range(1,11)]
print result

result = [x**2 for x in range(1,11) if x%2 == 0]
print result

# セット内包表記
result = {x**2 for x in range(1,11)}
print result

# 辞書内包表記
result = {x*2:x**2 for x in range(1,11)}
print result

# リスト内包表記をジェネレータとして、遅延することもできる
result = (x**2 for x in range(1,11))
print next(result)
print next(result)
print next(result)
print next(result)

