import re

with open('input.txt', 'r') as file:
    input = file.read()

sum = 0

# Define a regular expression pattern to match groups of numbers and non-dot/non-number characters
num_pattern = r'\d+'
gear_pattern = r'\*'


# Use re.finditer to find all occurrences of the pattern along with their positions
gear_matches = re.finditer(gear_pattern, input)
num_matches = re.finditer(num_pattern, input)

# Extract the matched groups and their starting positions
gear_positions = [(match.group(), match.start()) for match in gear_matches]
number_positions = [(int(match.group()), match.start()) for match in num_matches]

for gear in gear_positions:
    gear_ratio = 0
    for num in number_positions:
        if gear[1] == num[1]-1 or gear[1] == (num[1]+len(str(num[0]))) or ((gear[1]>=num[1]-142) and (gear[1] <=num[1]+len(str(num[0]))-141)) or ((gear[1]>= num[1]+140) and (gear[1] <=num[1]+len(str(num[0]))+141)):
            for num2 in number_positions:
                if num != num2 and (gear[1] == num2[1]-1 or gear[1] == (num2[1]+len(str(num2[0]))) or ((gear[1]>=num2[1]-142) and (gear[1] <=num2[1]+len(str(num2[0]))-141)) or ((gear[1]>= num2[1]+140) and (gear[1] <=num2[1]+len(str(num2[0]))+141))):
                    gear_ratio = num[0] * num2[0]
    if gear_ratio != 0:
        sum += gear_ratio

print(sum)