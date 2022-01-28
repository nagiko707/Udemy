#何も値が入っていないことをNoneという。

is_empty = None
print(is_empty)

#helpで見てみる。

if is_empty is not None:
    print('None!!!')
#==ではなしにisをつかって判定する。

#isはオブジェクト同士を同じにしないと認識しない。
print(1 == True)
print(1 is True)
print(True is True)
print(None is None)

"""
isで判定するときはNoneの時
変数の値が一緒な時は等号を使う。
"""
