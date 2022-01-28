#sewwy version

'''
x = y = 0
for line in open("input.txt", "r"):
    c, q = line.split()
    q = int(q)
    if c == "forward":
        x += q

    elif c == "up":
        y -= q
    elif c == "down":
        y += q
'''



def getNumber(prompt, min=None, max=None):
    while 1:
        try:
            v = int(input(prompt))
            if (not min or v>=min) and (not max or v<=max):
                return v
            else:
                print(f"Error, number should between {min} and {max}.")
        except:
            print("Error not a number.")


# height = getNumber("How tall are you in inches?", 36, 96)
# print(f"You are {height*2.54:.0f}cm tall.")

#REGEX

s = "2x^2 + 345x^1 + -156x^0"

import re
#https://docs.python.org/3/library/re.html
matches = re.findall("(-?\d+)x\^(-?\d+)", s) #\d finds decimal number, + searches for more of the precedding, x searchs for x, \^ searches for ^, the () are nets that
#only grab specific items, -? gets 0 or more

# print(matches)
x = 56 

result = 0
for coef, exp in matches:
    coef = int(coef)
    exp = int(exp)
    result += coef*x**exp

print(result)

s = s.replace("x^", "*x**")
print(eval(s))
