Y = 0
X = 0
AIM = 0
# down: AIM += 
# up: AIM -=
#forward: X += and Y += AIM*X


f = open("Advent of Code\\Day 2\\input.txt")
directions = []
for line in f:
    directions.append(line.strip())

# print(directions)

for direction in directions:
    if 'forward' in direction:
        X += int(direction[-1])
        Y += (int(direction[-1])*AIM)
    if 'up' in direction:
        AIM -= int(direction[-1])
    if 'down' in direction:
        AIM += int(direction[-1])
    

print(Y)
print(X)
print(Y*X)
#PART 1 ~ 5 minutes   
#PART 2 ~ 5 minutes at most
#TOTAL ~ 10 minutes

