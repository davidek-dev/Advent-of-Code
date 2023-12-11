import re 
import numpy as np

with open('input.txt', 'r') as file:
    input = file.read().splitlines()

for i in range(len(input)):
    input[i] = re.sub(r'[^\d]+', '', input[i])
    if(len(input[i])<2):
        input[i] = input[i] + input[i]
    if (len(input[i])>2):
        input[i] = input[i][0] + input[i][len(input[i])-1]
    input[i] = int(input[i])
   
total = sum(input)
print(total)