f = open('adventofcode5.txt', 'r')
input = f.read()

crates = (['D','T','W','F', 'J', 'S', 'H', 'N'], 
          ['H','R','P', 'Q', 'T', 'N', 'B', 'G'], 
          ['L', 'Q', 'V'], ['N', 'B', 'S', 'W', 'R', 'Q'],
           ['N', 'D', 'F', 'T', 'V', 'H', 'M', 'B'], 
           ['M','D','B','V','H','T','R'], 
            ['D', 'B', 'Q', 'J'], ['D','N','J','V','R','Z','H','Q'], 
            ['B','N','H','M','S'])

data = input.split()
cleandata = [elem for elem in data if elem != 'move']
list2 = [elem for elem in cleandata if elem != 'to']
list3 = [elem for elem in list2 if elem != 'from']
list4 = []
for element in list3:
     list4.append(int(element))

list5 = []
for i in range(0,len(list4), 3):
    list5.append([list4[i], list4[i+1], list4[i+2]])    

def moves(x,y,z):
    item = crates[y-1][:x]
    crates[z-1].append(item)

for i in list5:
    x,y,z = i[0], i[1], i[2]
    moves(x,y,z)

for i in crates:
    print(i.pop())

## solution for Part 2

data = input.split()
cleandata = [elem for elem in data if elem != 'move']
list2 = [elem for elem in cleandata if elem != 'to']
list3 = [elem for elem in list2 if elem != 'from']
list4 = []
for element in list3:
     list4.append(int(element))

list5 = []
for i in range(0,len(list4), 3):
    list5.append([list4[i], list4[i+1], list4[i+2]])    

## print(list5)

def moves(x,y,z):
    item = crates[y-1]
    timepass = len(item)
    item1 = item[timepass-x:]
    del crates[y-1][-x:]
    crates[z-1].extend(item1)

for i in list5:
    x,y,z = i[0], i[1], i[2]
    moves(x,y,z)

for i in crates:
    print(i.pop())