'''
5251578181
6158452313
1818578571
3844615143
6857251244
2375817613
8883514435
2321265735
2857275182
4821156644


(j, i) 1 = i-1, j-1
        2 = i-1, j
        3 = i-1, j+1

'''

FLASHES = 0
FLASHED = []

def printArr(arr):
    for i in range(len(arr)):
        print("[", end="")
        for j in range(len(arr[0])):
            print(arr[i][j], end="")
        print("]")

def flash(i, j, arr):
    if (j==0) and (i==0):
        arr[i][j+1] += 1
        arr[i+1][j+1] += 1
        arr[i+1][j] += 1
    elif j==0 and i==(len(arr))-1:
        arr[i-1][j] += 1
        arr[i-1][j+1] += 1
        arr[i][j+1] += 1
    elif j==len(arr[0])-1 and i==0:
        arr[i][j-1] += 1
        arr[i+1][j-1] += 1
        arr[i+1][j] += 1
    elif j==(len(arr[0]))-1 and i == len(arr)-1:
        arr[i][j-1] += 1
        arr[i-1][j-1] += 1
        arr[i-1][j] += 1
    elif j==0:
        arr[i][j+1] += 1
        arr[i-1][j] += 1
        arr[i-1][j+1] += 1
        arr[i+1][j] += 1
        arr[i+1][j+1] += 1
    elif i == 0:
        arr[i][j-1] += 1
        arr[i][j+1] += 1
        arr[i+1][j-1] += 1
        arr[i+1][j] += 1
        arr[i+1][j+1] += 1
    elif j == len(arr[0])-1:
        arr[i][j-1] += 1
        arr[i+1][j-1] += 1
        arr[i+1][j] += 1
        arr[i-1][j-1] += 1
        arr[i-1][j] += 1
    elif i == len(arr)-1:
        arr[i][j-1] += 1
        arr[i-1][j-1] += 1
        arr[i-1][j] += 1
        arr[i-1][j+1] += 1
        arr[i][j+1] += 1
    else:
        arr[i-1][j-1] += 1
        arr[i-1][j] += 1
        arr[i-1][j+1] += 1
        arr[i][j-1] += 1
        arr[i][j+1] += 1
        arr[i+1][j-1] += 1
        arr[i+1][j] += 1
        arr[i+1][j+1] += 1
    arr[i][j] = 0
    global FLASHES
    FLASHES += 1

    return arr

def checkForFlashes(arr, k=None, l=None):
    global FLASHED
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 9:
                flash(i, j, arr)
                # if k is not None and l is not None:
                #     arr[k][l] = 0
                FLASHED.append([i, j])
                checkForFlashes(arr)
    return 

def step(arr, endVal=100):
    #THIS IS WHERE STUFF CHANGED
    global FLASHED
    global FLASHES
    # flashes = 0
    steps = 0
    while FLASHES != 100:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                arr[i][j] += 1
                # if arr[i][j] > 9:
                #     arr = flash(i, j, arr)
        checkForFlashes(arr)
        for coord in FLASHED:
            arr[coord[0]][coord[1]] = 0
        FLASHED = []
        if FLASHES != 100:
            FLASHES = 0
        steps += 1
    
    return arr, steps


f = open("input.txt", "r")
arr = []
for line in f:
    arr.append(list(line.strip()))

for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j] = int(arr[i][j])

arr, steps = step(arr)
printArr(arr)
print(steps)

# print(FLASHES)
# print(FLASHED)
#ONE HOUR NINE MINUTES
#01:09:00 ON THE DOT