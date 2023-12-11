with open('input.txt', 'r') as file:
    input = file.read().strip()
#only 12 red, 13 green, 14 blue
sum=0

for line in input.split('\n'):
    not_in_range = True
    game_num, line = line.split(':')
    for game in line.split(';'):
        for cubes in game.split(','):
            n,color = cubes.split()
            if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
               not_in_range = False
    if not_in_range:
        sum+= int(game_num.split()[-1])
        print(game_num)
print(sum)
