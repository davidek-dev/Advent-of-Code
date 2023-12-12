with open('input.txt', 'r') as file:
    input = file.read().strip()

# Split the input string into individual cards
cards = input.split("Card")

# Remove empty strings and leading/trailing whitespaces
cards = [card.strip() for card in cards if card.strip()]

# Initialize the final arrays
winning_number_array = []
chosen_numbers = []

# Iterate through each card and split based on the "|"
for card in cards:
    # Split the card into left and right sides
    left, right = card.split("|")

    # Extract numbers from left and right sides
    numbers_left = [int(num) for num in left.split() if num.isdigit()]
    numbers_right = [int(num) for num in right.split() if num.isdigit()]

    # Append the numbers to the super arrays
    winning_number_array.append(numbers_left)
    chosen_numbers.append(numbers_right)

sum = 0

for index, card in enumerate(cards):
    count_winning_numbers = 0
    for win in winning_number_array[index]:
        winning_number = False
        for num in chosen_numbers[index]:
            if num == win:
                winning_number = True
        if winning_number:
            count_winning_numbers += 1        
    if count_winning_numbers != 0:
        sum += 2 ** (count_winning_numbers-1)


print(sum)