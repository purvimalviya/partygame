import random
print('\n Would you like it if i choose people for you ? (yes/no) ')
answer = input()

file = open('dares.txt', 'r')
text = file.readlines()


while answer == 'no' or answer == 'NO' or answer == 'No':
    result = random.choice(text)
    var1 = input('WHO IS THE TASK FOR? ')
    var2 = input('WHO WILL BE A PART OF THE TASK? ')
    result1 = result.replace("blank1", var1)
    result2 = result1.replace("blank2", var2)
    task = result2
    print(task)

if answer == 'yes' or answer == 'YES' or answer == 'Yes':
    playerslist = []
    newlist = []
    n = int(input('how many are you? '))
    for i in range(0, n):
        player = input('enter player name : ')
        playerslist.append(player)
        newlist.append(player)
    print(playerslist)
    temp = playerslist

    while answer == 'yes' or answer == 'YES' or answer == 'Yes':

        if len(temp) == 1:
            temp.extend(newlist)

        result = random.choice(text)
        var1 = random.choice(temp)
        temp.remove(var1)
        var2 = random.choice(temp)
        if var1 == var2:
            continue
        result1 = result.replace("blank1", var1)
        result2 = result1.replace("blank2", var2)
        task = result2
        print(task)
        input('P R E S S  E N T E R')


else:
    print('enter valid answer')