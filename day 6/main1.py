inp = open('in.txt', 'r')
a = inp.read().split(',')
inp.close()

b = []
for aa in a:
    b.append(int(aa))

# print(b)

for day in range(80):
    for i in range(len(b)):
        if(b[i] == 0):
            b[i] = 6
            b.append(8)
        else:
            b[i] -= 1

print(len(b))
