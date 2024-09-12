import random

# Dictionary for resistor color codes and their corresponding values
color_code_4_band = {
    'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4,
    'Green': 5, 'Blue': 6, 'Violet': 7, 'Gray': 8, 'White': 9
}

multiplier_code = {
    'Black': 1, 'Brown': 10, 'Red': 100, 'Orange': 1_000, 'Yellow': 10_000,
    'Green': 100_000, 'Blue': 1_000_000, 'Gold': 0.1, 'Silver': 0.01
}

tolerance_code = {
    'Brown': 1, 'Red': 2, 'Green': 0.5, 'Blue': 0.25, 'Violet': 0.1, 'Gray': 0.05, 'Gold': 5, 'Silver': 10
}


# Function to format resistance values with engineering prefixes using short-hand letters
def format_resistance(value):
    if value >= 1_000_000:
        return f"{value / 1_000_000:.2f}MΩ"  # Megaohms
    elif value >= 1_000:
        return f"{value / 1_000:.2f}kΩ"  # Kiloohms
    else:
        return f"{value:.2f}Ω"  # Ohms


def generate_4_band_resistor():
    band1 = random.choice(list(color_code_4_band.keys())[1:])  # First band cannot be black
    band2 = random.choice(list(color_code_4_band.keys()))
    multiplier = random.choice(list(multiplier_code.keys()))
    tolerance = random.choice(list(tolerance_code.keys()))

    resistance_value = (color_code_4_band[band1] * 10 + color_code_4_band[band2]) * multiplier_code[multiplier]
    tolerance_value = tolerance_code[tolerance]

    return [band1, band2, multiplier, tolerance], resistance_value, tolerance_value


def generate_5_band_resistor():
    band1 = random.choice(list(color_code_4_band.keys())[1:])  # First band cannot be black
    band2 = random.choice(list(color_code_4_band.keys()))
    band3 = random.choice(list(color_code_4_band.keys()))
    multiplier = random.choice(list(multiplier_code.keys()))
    tolerance = random.choice(list(tolerance_code.keys()))

    resistance_value = (color_code_4_band[band1] * 100 + color_code_4_band[band2] * 10 + color_code_4_band[band3]) * \
                       multiplier_code[multiplier]
    tolerance_value = tolerance_code[tolerance]

    return [band1, band2, band3, multiplier, tolerance], resistance_value, tolerance_value


def play_game():
    while True:
        print("\nWelcome to the Resistor Color Code Game!")

        choice = input("Choose resistor type (4 or 5) or type 'exit' to quit: ").strip().lower()

        if choice == "4":
            bands, resistance, tolerance = generate_4_band_resistor()
            print(f"4-band Resistor Colors: {bands}")
        elif choice == "5":
            bands, resistance, tolerance = generate_5_band_resistor()
            print(f"5-band Resistor Colors: {bands}")
        elif choice == "exit":
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice! Please select either '4' or '5', or type 'exit' to quit.")
            continue

        # Ask the user to guess the resistance value and the tolerance
        user_resistance_guess = float(input("Guess the resistance value (in ohms): "))
        user_tolerance_guess = float(input("Guess the tolerance percentage (±%): "))

        # Check if the user's guess is within the tolerance range
        lower_bound = resistance * (1 - tolerance / 100)
        upper_bound = resistance * (1 + tolerance / 100)

        # Format the resistance value to use engineering short-hand letters
        formatted_resistance = format_resistance(resistance)

        # Check if both resistance and tolerance guesses are correct
        if lower_bound <= user_resistance_guess <= upper_bound and user_tolerance_guess == tolerance:
            print(
                f"\033[92mCorrect! The resistance value is {formatted_resistance} with ±{tolerance}% tolerance.\033[0m")
        else:
            print(
                f"\033[91mIncorrect! The actual resistance value is {formatted_resistance} with ±{tolerance}% tolerance.\033[0m")


# Run the game
play_game()
