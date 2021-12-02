inp = open('in.txt', 'r')

steps = inp.read().split('\n')
print(steps)

horizontal = 0
depth = 0
aim = 0

for i in steps:
    if(i[0] == 'f'):
        horizontal += int(i[-1])
        depth += aim * int(i[-1])
    elif(i[0] == 'd'):
        aim += int(i[-1])
    else:
        aim -= int(i[-1])

print(horizontal, depth, horizontal*depth)

inp.close()
