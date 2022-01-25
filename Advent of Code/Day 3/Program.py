f = open("Advent of Code\Day 3\input.txt", 'r')

data = []
for line in f:
    x = line.strip()[::-1]
    data.append(list(x))
# data = [list('1111000'), list('0000111'), list('0000111')]
GAMMA = []
EPSILON = []
d = len(data[0])


for i in range(d):
    temp1 = []
    for byte in data:
        temp1.append(byte.pop())
        continue
    # print(temp1)
    most_common = max(temp1, key=temp1.count)
    least_common = min(temp1, key=temp1.count)
    # print(most_common)
    # print(least_common)
    # input("Waiting...")
    GAMMA.append(most_common)
    EPSILON.append(least_common)

GAMMA = ''.join(GAMMA)
GAMMA = int(GAMMA, 2)
EPSILON = ''.join(EPSILON)
EPSILON = int(EPSILON, 2)

print(GAMMA)
print(EPSILON)
print(GAMMA*EPSILON)



#GAMMA = get most common bit for each column, turn to decimal
#EPSILON = get least common bit for each column, turn to decimal
#TIME ON PART 1 ~ 30 minutes

