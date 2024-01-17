f = open('adventofcode3.txt', 'r')
lines = f.read()
data = lines.split('\n')

## Data Clean-up
def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = 3  # Number of items in the sublist
 
puredata = list(divide_chunks(data, n))
print(puredata)

lst1 = []
for x in puredata:
    lst2 = []
    for y in x:
        listofChars = list(y)
        lst2.append(listofChars)
    lst1.append(lst2)
print(lst1)

# ## Helper function for finding intersection
# def commmon(loc1, loc2, loc3):
#     z = loc3.intersection(loc1.intersection(loc2))
#     return (z)

# # Helper function to break a list of char into 2 parts
# def index(loc, num):
#     loc1 = loc[:(int(num/2))]
#     loc2 = loc[(int(num/2)):]
#     return(loc1,loc2)

# Helper to convert 
def convertlow(char):
    y = ord(char) - 96
    return (y)

def converthigh(char):
    y = ord(char) - 38
    return (y)

final_lst = []
for x in lst1:
    a,b,c = set(x[0]), set(x[1]), set(x[2])
    d = a.intersection(b.intersection(c))
    z = list(d)[0]
    y = ord(z)
    if  y >= 97:
        final_lst.append(convertlow(z))
    else:
        final_lst.append(converthigh(z))
print(final_lst)

print (sum(final_lst))