import collections

def getMessage():
    msg = ""
    with open("\\nothing_to_see_here.txt", "r") as f:
        msg = "".join(f.readlines())
    
    return msg.split("\n")

def rotate(msg, key):
    RING = 0
    ROTATION = 1
    commands = key.split("-")
    rotation_commands = []

    #formatting commands to just numbers.
    for i, c in enumerate(commands):
        rotation_commands.append(c.split("_"))
        rotation_commands[i][RING] = int(rotation_commands[i][RING][1])
        x = rotation_commands[i][ROTATION] 
        if "cc" in x:
            x = -1 * int(x[2:])
        else:
            x = int(x[1:])
        
        rotation_commands[i][ROTATION] = x

    print(rotation_commands)

    new_msg = ""
    rotated_rings = []
    for i, c  in enumerate(rotation_commands):

        ring = c[RING]
        # print(ring)
        top_string = msg[ring-1][ring-1:len(msg[0])-ring+1]
        top = []
        for i in range(len(top_string)):
            top.append(top_string[i])

        bottom_string = msg[len(msg)-ring][ring-1:len(msg[0])-ring+1]
        bottom = []
        for i in range(len(bottom_string)):
            bottom.append(bottom_string[i])

        left = []
        right = []
        for i in range(len(msg)):
            for j in range(len(msg[0])):
                if i>ring-1 and i<(len(msg)-ring) and j == ring-1:
                    left.append(msg[i][j])
                elif i>ring-1 and i<(len(msg)-ring) and j==(len(msg[0])-ring):
                    right.append(msg[i][j])

        added_sides = top + right + bottom + left
        # print(added_sides)

        added_sides = collections.deque(added_sides)
        added_sides.rotate(c[ROTATION])
        
        shifted_ring = list(added_sides)
        rotated_rings += shifted_ring
    
    return rotated_rings #rotates rings as requested, simply unformatted back into string form.

            
def column_shift(msg):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

out = open("i_looked_anyway.txt", "w")
msg = getMessage()
msg = msg[:-1]
key = input("Enter Encryptionb Key:\n")

rotated_rings = rotate(msg, key)
# print(rotated)

