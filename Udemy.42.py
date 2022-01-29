some_list = [1, 2, 3, 4, 5]

'''
i = 0
while i < len(some_list):
    print(some_list[i])
    i += 1
'''

'''
for i in some_list:
    print(i)
'''

'''
for s in 'abcde':
    print(s)
'''

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
        #break
    print(word)