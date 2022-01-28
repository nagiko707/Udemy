y = [1, 2, 3]
x = 1

# xがyのリストの中に入っている場合
if x in y:
    print('in')

# xがyのリストの中に入っていない場合
if 100 not in y:
    print('not in')

a = 1
b = 2

# aとbがイコールではない場合
if not a == b:
    print('Not equal')
"""
↑はあまり望ましくないからこちらを使うとよい。
if a != b:
    print('Not equal')
"""

is_ok = True

if not is_ok:
    print('hello')

