inp = open('in.txt', 'r')
indata = inp.read().split()
count = 0

for x in range(len(indata)-1):
    if(int(indata[x]) < int(indata[x+1])):
        count += 1

inp.close()
print(count)
