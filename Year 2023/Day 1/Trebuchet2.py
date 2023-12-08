import re 
import numpy as np

with open('input.txt', 'r') as file:
    input = file.read().splitlines()





for i in range(len(input)):
    input[i] = input[i].replace("nine", "ni9ne")
    input[i] = input[i].replace( "eight", "ei8ght")
    input[i] = input[i].replace( "seven", "se7ven")
    input[i] = input[i].replace("six", "s6ix")
    input[i] = input[i].replace("five", "fi5ve")
    input[i] = input[i].replace("four", "fo4ur")
    input[i] = input[i].replace("three", "th3ree")
    input[i] = input[i].replace( "two", "tw2o")
    input[i] = input[i].replace("one", "o1ne")
    
    
    input[i] = re.sub(r'[^\d]+', '', input[i])
    if(len(input[i])<2):
        input[i] = input[i] + input[i]
    if (len(input[i])>2):
        input[i] = input[i][0] + input[i][len(input[i])-1]
    input[i] = int(input[i])

total = sum(input)
print(total)