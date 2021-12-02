inp = open('in.txt', 'r')
indata = inp.read().split()
count = 0
slide = []

for x in range(len(indata)-2):
    sum = 0
    for y in range(3):
        sum += int(indata[x+y])
    slide.append(sum)

for x in range(len(slide)-1):
    if(slide[x] < slide[x+1]):
        count += 1

inp.close()
print(count)
