import re
val = 0
nums = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
nums_rev = {v: k for k, v in nums.items()}
with open("1-1\input.txt") as f:
    for line in f:
        line = line.strip()
        digits_str = []
        digits = re.findall("[0-9]", line)
        digits_loc = []
        for digit in digits:
            ind = line.index(digit)
            while ind in digits_loc:
                ind = line[ind+1:].index(digit)+len(line[:ind+1])
            digits_loc.append(ind)
        for ind, num in enumerate(nums):
            if num in line:
                low = {
                    line.index(nums_rev[ind]): [num, len(nums_rev[ind])]
                }
                high = {
                    line.rindex(nums_rev[ind]): [num, len(nums_rev[ind])]
                }
                if not low == high:
                    digits_str.append(low)
                    digits_str.append(high)
                else:
                    digits_str.append(low)
        min_in_digits = digits_loc[0]
        max_in_digits = digits_loc[-1]

        if len(digits_str) > 0:
            min_in_strings = min(digits_str, key=lambda x: list(x.keys())[0])
            max_in_strings = max(digits_str, key=lambda x: list(x.keys())[0])
            min_key = list(min_in_strings.keys())[0]
            max_key = list(max_in_strings.keys())[0]
            if min_in_digits < list(min_in_strings.keys())[0]:
                _min = line[min_in_digits]
            else:
                _min = nums[line[min_key:min_in_strings[min_key][1]+min_key]]
            if max_in_digits > list(max_in_strings.keys())[0]:
                _max = line[max_in_digits]
            else:
                _max = nums[line[max_key:max_in_strings[max_key][1]+max_key]]
        else:
            _min = digits[0]
            _max = digits[-1]
        digit = str(_min) + str(_max)
        if len(digit) > 2:
            raise "AAAAA"
        val += int(digit)
print(val)