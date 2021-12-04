inp = open('in.txt', 'r')
a = inp.read().split()
inp.close()
print(a)

count0 = [0]*len(a[0])
count1 = [0]*len(a[0])
epsilon = 0
gamma = 0

for no in a:
    i = 0
    for digit in no:
        if(digit == '0'):
            count0[i] += 1
        else:
            count1[i] += 1
        i += 1

print(count0, count1)

count = []

for (i, j) in zip(count0, count1):
    if(i > j):
        print('yes')
        count.append(0)
    else:
        print('no')
        count.append(1)

print(count)

for i in range(len(count)):
    epsilon += count[len(count)-1-i]*(2**i)
    gamma += (~-count[len(count)-1-i])*(2**i)

print(epsilon, -gamma, epsilon*-gamma)
