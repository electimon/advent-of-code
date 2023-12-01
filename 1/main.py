import re
val = 0
with open("1\input.txt") as f:
    for line in f:
        digits = re.findall("[0-9]", line)
        digit = digits[0] + digits[-1]
        val += int(digit)
print(val)