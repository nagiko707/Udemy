#def＝定義する
def say_something():
    #print('hi')
    s = 'hi'
    return s

result = say_something()
print(result)


#定義してから呼び出す
#呼び出すとき
#say_something()

#return=返り値

#変数
def what_is_this(color):
    #print(color)
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('green')
print(result)

#what_is_this('red')
