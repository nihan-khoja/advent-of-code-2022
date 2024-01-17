f = open('adventofcode6.txt', 'r')
input = f.read()

data = list(input)

for i in range (0, len(data)):
    if len (set([data[i],data[i+1], data[i+2], data[i+3]])) == 4:
        print (i+4)
        break
    else:
        continue

## Part 2

data2 = list(input)    
subdata2 = [data2[i:i+14] for i in range(0, len(data2))]

for i in range (0, len(subdata2)):
    if len(set(subdata2[i])) == 14:
        print (i+14)
        break
    else:
        continue