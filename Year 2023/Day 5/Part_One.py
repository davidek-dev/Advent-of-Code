with open('./input.txt', 'r') as file:
    input = file.read().strip()

# Parse the input
input = input.split('seed-to-soil map:')
print(input)