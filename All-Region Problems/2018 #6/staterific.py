def printList(s):
    pass

def leastoGreat(s):
    pass

def greattoLeast(s):
    pass

def M(s):
    pass

def stdDeviation(s):
    pass


x = input("Give me comma delimited numbers. Up to a thousand: ")
x = x.split(",")
while len(x) > 1000:
    x = input("Give me comma delimited numbers. Up to a thousand: \n")
    x = x.split(",")

z = input("What do you want to do? \n1:Print List\n2:Sort least to greatest\n3:Sort greatest to least\n4:Print mean, median, and mode\n5:Print Population Variance and Standard Deviation\n")
while int(z) > 5 or int(z) <= 0:
    z = input("What do you want to do? \n1:Print List\n2:Sort least to greatest\n3:Sort greatest to least\n4:Print mean, median, and mode\n5:Print Population Variance and Standard Deviation\n")

if z == 1:
    printList(x)
elif z == 2:
    leastoGreat(x)
elif z == 3:
    greattoLeast(x)
elif z == 4:
    M(x) 
elif z == 5:
    stdDeviation(x)
