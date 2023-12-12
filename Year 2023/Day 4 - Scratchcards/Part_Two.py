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



# Dictionary to store the count of scratchcards for each card
scratchcard_count = {i: 1 for i in range(len(cards))} # initalize with each card being once in the staple


for index in range(len(cards)):
    count_winning_numbers = 0
    for win in winning_number_array[index]:
        if any(num == win for num in chosen_numbers[index]):
            count_winning_numbers += 1

    # If no winning numbers, continue to the next card
    if count_winning_numbers == 0:
        continue

    # Otherwise, simulate winning additional scratchcards
    for x in range(1, count_winning_numbers + 1):
        scratchcard_count[index + x] += scratchcard_count[index] #if the current num card is a win, transfer the amount of the current card to the next card
        # and iterate to the following + repeat, with the following

# Calculate the total number of scratchcards
total_scratchcards = sum(scratchcard_count.values())
print(total_scratchcards)
