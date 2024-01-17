f = open('adventofcode4.txt', 'r')
lines = f.read()
data = lines.split()
result = []
for element in data:
    temp = element.split('-')
    first_num = temp[0]
    last_num = temp[2]
    temp = temp[1].split(',')
    second_num = temp[0]
    third_num = temp[1]
    set_one = set(range(int(first_num), int(second_num)+ 1))
    set_two = set(range(int(third_num), int(last_num)+ 1))
    z = set_one.intersection(set_two)
    if len(z) >= 1:
        result.append(1)
    # elif len(z) == len(set_two):
    #     result.append(1)
    else:
        result.append(0)

print(sum(result))