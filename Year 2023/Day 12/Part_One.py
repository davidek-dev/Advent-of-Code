with open('input.txt', 'r') as file:
    input = file.read().strip()

# Parse the input
input = input.split('\n') # Split by new line
input = [(line[0], int(line[1:])) for line in input] # Convert to tuple
print(input) # Debug
