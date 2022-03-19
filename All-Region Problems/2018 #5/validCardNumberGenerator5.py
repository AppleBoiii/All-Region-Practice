import random
from Program import luhn_check

i = 0
nums = []
while i < 10:
    n = str(random.randrange(1000000000000000, 9999999999999999))
    
    if luhn_check(n): 
        nums.append(n)
        i += 1

print("VALID CARD NUMBERS")
for i, c in enumerate(nums):
    print(f"{i+1}: {c}")

