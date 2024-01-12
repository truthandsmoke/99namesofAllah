import time
from difflib import SequenceMatcher
import random

# Dictionary of Allah's names and their definitions
allah_names_and_definitions = {
    "Ar-Rahman": "The Most Gracious",
    "Ar-Rahim": "The Most Merciful",
    "Al-Malik": "The King",
    "Al-Quddus": "The Holy",
    "As-Salam": "The Peace",
    "Al-Muhaymin": "The Guardian",
    "Al-Aziz": "The Almighty",
    "Al-Jabbar": "The Compeller",
    "Al-Mutakabbir": "The Majestic",
    "Al-Khaliq": "The Creator",
    "Al-Bari": "The Evolver",
    "Al-Musawwir": "The Fashioner of Forms",
    "Al-Ghaffar": "The Forgiving",
    "Al-Qahhar": "The Subduer",
    "Al-Wahhab": "The Bestower",
    "Ar-Razzaq": "The Provider",
    "Al-Fattah": "The Opener",
    "Al-Alim": "The Knower of All",
    "Al-Qabid": "The Constrictor",
    "Al-Basit": "The Reliever",
    "Al-Khafid": "The Abaser",
    "Ar-Rafi": "The Exalter",
    "Al-Muizz": "The Bestower of Honor",
    "Al-Mudhill": "The Humiliator",
    "As-Sami": "The Hearer of All",
    "Al-Basir": "The Seer of All",
    "Al-Hakam": "The Judge",
    "Al-Adl": "The Just",
    "Al-Latif": "The Subtle One",
    "Al-Khabir": "The All-Aware",
    "Al-Halim": "The Forbearing",
    "Al-Azim": "The Magnificent",
    "Al-Ghafur": "The Forgiver and Concealer of Faults",
    "Ash-Shakur": "The Rewarder of Thankfulness",
    "Al-Ali": "The Highest",
    "Al-Kabir": "The Greatest",
    "Al-Hafiz": "The Preserver",
    "Al-Muqit": "The Nourisher",
    "Al-Hasib": "The Accounter",
    "Al-Jalil": "The Mighty",
    "Al-Karim": "The Generous",
    "Ar-Raqib": "The Watchful One",
    "Al-Mujib": "The Responder to Prayer",
    "Al-Wasi": "The All-Encompassing",
    "Al-Hakim": "The Perfectly Wise",
    "Al-Wadud": "The Loving One",
    "Al-Majid": "The Majestic One",
    "Al-Baith": "The Resurrector",
    "Ash-Shahid": "The Witness",
    "Al-Haqq": "The Truth",
    "Al-Wakil": "The Trustee",
    "Al-Qawi": "The Strong",
    "Al-Matin": "The Firm",
    "Al-Wali": "The Friend",
    "Al-Hamid": "The Praiseworthy",
    "Al-Muhsi": "The Accounter of All",
    "Al-Mubdi": "The Originator",
    "Al-Muid": "The Restorer",
    "Al-Muhyi": "The Giver of Life",
    "Al-Mumit": "The Taker of Life",
    "Al-Hayy": "The Living",
    "Al-Qayyum": "The Self-Subsisting",
    "Al-Wajid": "The Perceiver",
    "Al-Majid": "The Illustrious",
    "Al-Wahid": "The One",
    "Al-Ahad": "The Unique",
    "As-Samad": "The Eternal Refuge",
    "Al-Qadir": "The Powerful",
    "Al-Muqtadir": "The Determiner of All",
    "Al-Muqaddim": "The Expediter",
    "Al-Muakhkhir": "The Delayer",
    "Al-Awwal": "The First",
    "Al-Akhir": "The Last",
    "Az-Zahir": "The Manifest",
    "Al-Batin": "The Hidden",
    "Al-Wali": "The Protecting Friend",
    "Al-Mutaali": "The Supreme",
    "Al-Barr": "The Kind",
    "At-Tawwab": "The Ever-Returning",
    "Al-Muntaqim": "The Avenger",
    "Al-Afuww": "The Pardoner",
    "Ar-Rauf": "The Compassionate",
    "Malik-ul-Mulk": "The Owner of All",
    "Dhu-l-Jalal wa-l-Ikram": "The Lord of Majesty and Bounty",
    "Al-Muqsit": "The Equitable",
    "Al-Jami": "The Gatherer",
    "Al-Ghani": "The Self-Sufficient",
    "Al-Mughni": "The Enricher",
    "Al-Mani": "The Preventer of Harm",
    "Ad-Darr": "The Creator of The Harmful",
    "An-Nafi": "The Creator of Good",
    "An-Nur": "The Light",
    "Al-Hadi": "The Guide",
    "Al-Badi": "The Incomparable",
    "Al-Baqi": "The Everlasting",
    "Al-Warith": "The Inheritor of All",
    "Ar-Rashid": "The Righteous Teacher",
    "As-Sabur": "The Patient",
    "Al-Ahad": "The One"
}

def is_partial_match(user_input, correct_name):
    similarity_ratio = SequenceMatcher(None, user_input.lower(), correct_name.lower()).ratio()
    return similarity_ratio >= 0.65

def reveal_letters(name, revealed_letters):
    revealed = ''
    for letter in name:
        if letter in revealed_letters:
            revealed += letter + ' '
        else:
            revealed += '_ '
    return revealed

def allah_game():
    correct_answers = []
    incorrect_answers = []
    correct_definitions = []
    incorrect_definitions = []
    score = 0
    start_time = time.time()
    last_correct_time = start_time

    print("Welcome to the Allah Names Game!")
    print("Type as many names of Allah as you can.")
    print("You get 10 points for typing two names consecutively within 8 seconds.")
    print("You get 11 points if they are 4 seconds apart.")
    print("Type 'quit' to quiz definitions, 'quitquit' to end the game.\n")

    entered_names = []
    entered_definitions = []
    game_log = []
    hints_given = 0
    revealed_letters = set()
    names_entered = set()

    while True:
        current_time = time.time()

        print(f"Current Points: {score} | Elapsed Time: {current_time - start_time:.2f} seconds | Invested Time: {(current_time - start_time) * 10:.2f} seconds")
        
        if len(allah_names_and_definitions) == 0:
            print("\nNow, let's quiz for definitions!")
            break

        correct_name = random.choice(list(allah_names_and_definitions.keys()))
        
        while correct_name in names_entered:
            correct_name = random.choice(list(allah_names_and_definitions.keys()))

        print("Current Allah Name:")
        partial_name = reveal_letters(correct_name, revealed_letters)
        print(partial_name)

        user_input = input("Type the name of Allah (or 'hint' for a hint): \n")

        if user_input.lower() == 'quit':
            if input("Type 'quitquit' to end the game: \n").lower() == 'quitquit':
                break
            else:
                continue
        elif user_input.lower() == 'hint':
            if hints_given < 3:
                hints_given += 1
                random_letter = random.choice(correct_name)
                revealed_letters.add(random_letter)
                print(f"Hint {hints_given}: '{random_letter}' has been revealed in the name.")
            else:
                print("You've used all available hints.")
        else:
            if any(is_partial_match(user_input, name) for name in allah_names_and_definitions):
                correct_answers.append((correct_name, current_time - start_time))
                score += 1

                if score >= 2:
                    time_difference = current_time - last_correct_time
                    if time_difference <= 4:
                        score += 11
                    elif time_difference <= 8:
                        score += 10
                    last_correct_time = current_time

                names_entered.add(correct_name)

                game_log.append((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time)), f"Entered: {user_input} | Allah Name: {correct_name}"))

                entered_names.append(user_input)
            else:
                incorrect_answers.append(correct_name)

    total_time_names = time.time() - start_time
    final_score_names = score * int(total_time_names) * 10

    print("\nNow, let's quiz for definitions!")

    while allah_names_and_definitions:
        name, definition = allah_names_and_definitions.popitem()
        user_input = input(f"What is the definition of '{name}'? \n")

        if user_input.lower() == definition.lower():
            correct_definitions.append(name)
            correct_answers.append((name, current_time - start_time))
            score += 10

            if score >= 2:
                time_difference = current_time - last_correct_time
                if time_difference <= 4:
                    score += 11
                elif time_difference <= 8:
                    score += 10
                last_correct_time = current_time

            game_log.append((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time)), f"Entered Definition for: {name}"))

        else:
            incorrect_definitions.append(name)

    total_time_definitions = time.time() - start_time - total_time_names
    final_score_definitions = score * int(total_time_definitions) * 10

    print("\nGame Over! Your total score is:", final_score_names + final_score_definitions, "points.")
    print(f"Total Time Elapsed for Names: {total_time_names:.2f} seconds")
    print(f"Total Time Elapsed for Definitions: {total_time_definitions:.2f} seconds")
    print(f"\nNumber of Correct Names Entered: {len(correct_answers)}")
    print(f"Number of Correct Definitions Guessed: {len(correct_definitions)}")

    print("\nCorrect Names Entered:")
    for name, time_taken in correct_answers:
        if time_taken <= 4:
            print(f"{name} - Achieved in 4 seconds")
        elif time_taken <= 8:
            print(f"{name} - Achieved in 8 seconds")
        else:
            print(f"{name} - Not within time bonus")

    print("\nIncorrect Names Entered:")
    for name in incorrect_answers:
        print(name)

    print("\nCorrect Definitions Guessed:")
    for name in correct_definitions:
        print(name)

    print("\nIncorrect Definitions Guessed:")
    for name in incorrect_definitions:
        print(name)

    export_choice = input("Would you like to export the game log? (yes/no): ").lower()
    if export_choice == 'yes':
        export_filename = input("Enter the filename to export (e.g., log.txt): ")
        with open(export_filename, 'w') as file:
            file.write("Game Log:\n")
            for entry in game_log:
                file.write(f"{entry[0]} - {entry[1]}\n")

if __name__ == "__main__":
    allah_game()
