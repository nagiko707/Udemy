num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))
#type()は型を出力することができる。

num = name
print(num, type(num))

num = 1
name = '1'

new_num = int(name)
print(new_num, type(new_num))

'''
:を使って型を書くこともできる。
num: int = 1
name: str = '1'
'''

#変数宣言の一番前に数字をつかわない。
