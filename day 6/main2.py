inp = open('in.txt', 'r')
a = inp.read().split(',')
inp.close()

# print(a)

b = []
for aa in a:
    b.append(int(aa))

print(b)
b_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

for bb in b:
    b_count[bb] += 1

for i in range(256):
    temp = b_count[0]
    b_count[0] -= b_count[0]
    for j in range(1, 9):
        b_count[j-1] += b_count[j]
        b_count[j] -= b_count[j]
    b_count[6] += temp
    b_count[8] += temp
    # print(b_count)


sum = 0

for j in range(0, 9):
    sum += b_count[j]

print(sum)
