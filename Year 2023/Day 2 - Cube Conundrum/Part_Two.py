from collections import defaultdict

with open('input.txt', 'r') as file:
    input = file.read().strip()

sum=0

for line in input.split('\n'):
    
    min_needed_cubes = defaultdict(int)
    game_num, line = line.split(':')

    for game in line.split(';'):

        for cubes in game.split(','):
            n,color = cubes.split()
            min_needed_cubes[color] = max(min_needed_cubes[color], int(n))

    score = 1

    for v in min_needed_cubes.values():
        score *= v
    sum +=score

print(sum)
