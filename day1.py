f = open("adventofcode.txt", 'r')
lines = f.read()

data = lines.split('\n\n')
puredata = [x.split('\n') for x in data]

lst1 = []
for x in puredata:
    lst2 = []
    for i in x:
        lst2.append(int(i))
    lst1.append(lst2)
  
sum_lst = []
for x in lst1:
    sum_lst.append(sum(x))

assert len(lst1) == len(sum_lst), "lenghts not equal"

## solving part 2

sum_lst = sorted(sum_lst)
top_3 = sum_lst[-3:]
print(sum(top_3))