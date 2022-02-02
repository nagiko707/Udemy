'''
def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)
#引数を増やしたい場合、カンマで区切って増やす。

menu(entree='beef', drink='beer', dessert='ice')
#順序を間違えないようにする。
#順序を間違えないようにキーワードをつける。
'''

#デフォルト引数とは、defの中に書くこと。
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu()
