import re

def sanitize(s):
    allowed_characters = "1234567890"
    for c in s:
        if c not in allowed_characters:
            s = s.replace(c, "")
    
    
    return s

def luhn_check(s):
    vals = []

    for i, c in enumerate(s):
        if i%2==0:
            x = 2*(int(c))
      
            if x > 9:
                x, y = str(x)[0], str(x)[1]

                x = int(x) + int(y)

            vals.append(int(x))
        else: 
            vals.append(int(c))

    return sum(vals) % 10 == 0

def writeFile(bool, s):
    if bool:
        with open("valid_cards.txt", "w+") as f:
            f.write(f"{s}\n")
    else:
        with open("invalid_cards.txt", "w+") as f:
            f.write(f"{s}\n")

            

#12345678
# while True:
#     unsanitized = input("Please input a credit card number: ")
#     sanitized = sanitize(unsanitized)
#     print(f"unsanitized: {unsanitized} & sanitized: {sanitized}")

#     luhn_value = luhn_check(sanitized)
#     if luhn_value:
#         print(f"VALID - {sanitized}")
#     else:
#         print(f"INVALID - {sanitized}")
    
#     writeFile(luhn_value, sanitized)

#     x = input("Would you like to continue? Yes / No input only: ")
#     while (x.lower() != "yes") and (x.lower() != "no"):
#         x = input("Would you like to continue? Yes / No input only: ")
#     if x.lower() == "no":
#         break
#     else:
#         continue
