count = 0

while count < 5:
    print(count)
    count += 1
#虫で確認してみる。

count = 0
while True:
    if count >= 5:
        break

    if count == 2:

        count += 1
        continue
    print(count)
    count += 1

"""    
インデントに気を付ける。
break文はwhile文の途中で抜ける。
continueは次のprintにはいかずにスキップして次のループに行く。
continueは次の行にはいかずにすっ飛ばして次のループにいってくださいと。
"""