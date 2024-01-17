f = open("adventofcode2.txt",'r')
lines = f.read()
data = lines.split('\n')

Totalscore = []

for x in data:
    if x == 'B Y':
        Totalscore.append(5)
    if x == 'A Y':
        Totalscore.append(4)
    if x == 'C Y':
        Totalscore.append(6)
    if x == 'A X':
        Totalscore.append(3)
    if x == 'B X':
        Totalscore.append(1)
    if x == 'C X':
        Totalscore.append(2)
    if x == 'A Z':
        Totalscore.append(8)
    if x == 'B Z':
        Totalscore.append(9)
    if x == 'C Z':
        Totalscore.append(7)

print (sum(Totalscore))