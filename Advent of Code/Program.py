Y = 0
X = 0


f = open("Advent of Cdoe\\input.txt")
directions = []
for line in f:
    directions.append(line.strip())

# print(directions)

for direction in directions:
    if 'forward' in direction:
        X += int(direction[-1])
    if 'up' in direction:
        Y -= int(direction[-1])
    if 'down' in direction:
        Y += int(direction[-1])
    

print(Y)
print(X)
print(Y*X)
#PART 1 ~ 5-7ish minutes

