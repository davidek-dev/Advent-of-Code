import re

with open('input.txt', 'r') as file:
    input = file.read()

sum = 0

# Define a regular expression pattern to match groups of numbers and non-dot/non-number characters
num_pattern = r'\d+'
sym_pattern = r'[^\n.\d]+'

# Use re.finditer to find all occurrences of the pattern along with their positions
sym_matches = re.finditer(sym_pattern, input)
num_matches = re.finditer(num_pattern, input)

# Extract the matched groups and their starting positions
symbol_positions = [(match.group(), match.start()) for match in sym_matches]
number_positions = [(int(match.group()), match.start()) for match in num_matches]

for num in number_positions:
    check = False
    for sym in symbol_positions:
        if sym[1] == num[1]-1 or sym[1] == (num[1]+len(str(num[0]))) or ((sym[1]>=num[1]-142) and (sym[1] <=num[1]+len(str(num[0]))-141)) or ((sym[1]>= num[1]+140) and (sym[1] <=num[1]+len(str(num[0]))+141)):
            check = True
    if check:
        sum += num[0]

print(sum)