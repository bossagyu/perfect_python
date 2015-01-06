# -*- coding: utf-8 -*-
from traceback import format_tb

# 0除算のエラーを待ち受け
try:
    10/0
except ZeroDivisionError:
    print('ZeroDivisionError occuered')

# 他のエラーを待ち受けていた場合はエラーハンドリングされない
# try:
#     10/0
# except ValueError:
#     print('ValueError occuered')

# 例外オブジェクトを利用した
try:
    10/0
except ZeroDivisionError as e:
    print(format(e.args))
    print(type(e))

# 基底クラスで例外オブジェクトを待ち受ける
try:
    10/0
except ArithmeticError as e:
    print('{0}: {1}'.format(type(e),e))





