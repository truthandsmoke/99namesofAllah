import tkinter as tk
from tkinter import ttk
import time
import difflib  # For spell checking

# List of the 99 names of Allah in Arabic
names_of_allah = [
    "ٱللَّٰهُ",
    "ٱلرََّحْمَـٰنُ",
    "ٱلرََّحِيمُ",
    "ٱلْمَلِكُ",
    "ٱلْقُدُّوسُ",
    "ٱلسََّلاَمُ",
    "ٱلْمُؤْمِنُ",
    "ٱلْمُهَيْمِنُ",
    "ٱلْعَزِيزُ",
    "ٱلْجَبََّارُ",
    "ٱلْمُتَكَبِّرُ",
    "ٱلْخَلِقُ",
    "ٱلْبَارِئُ",
    "ٱلْمُصَوِّرُ",
    "ٱلْغَفََّارُ",
    "ٱلْقَهََّارُ",
    "ٱلْوَهََّابُ",
    "ٱلْرََّزََّاقُ",
    "ٱلْفَتََّاحُ",
    "ٱلْعَلِيمُ",
    "ٱلْقَابِضُ",
    "ٱلْبَاسِطُ",
    "ٱلْخَافِضُ",
    "ٱلْرََّافِعُ",
    "ٱلْمُعِزُّ",
    "ٱلْمُذِّلُ",
    "ٱلْسََّمِيعُ",
    "ٱلْبَصِيرُ",
    "ٱلْحَكِيمُ",
    "ٱلْوَدُودُ",
    "ٱلْمَجِيدُ",
    "ٱلْبَاعِثُ",
    "ٱلشََّهِيدُ",
    "ٱلْحَقُّ",
    "ٱلْوَكِيلُ",
    "ٱلْقَوِّىُّ",
    "ٱلْمَتِينُ",
    "ٱلْوَلِىُّ",
    "ٱلْحَمِيدُ",
    "ٱلْمُحْصِيُّ",
    "ٱلْمُبْصِيُّ",
    "ٱلْحَسِيبُ",
    "ٱلْجَلِيلُ",
    "ٱلْكَرِيمُ",
    "ٱلْرََّقِيبُ",
    "ٱلْمُجِيبُ",
    "ٱلْوَسِىُّ",
    "ٱلْحَكِيمُ",
    "ٱلْوَدُودُ",
    "ٱلْمَجِيدُ",
    "ٱلْبَاعِثُ",
    "ٱلشََّهِيدُ",
    "ٱلْحَقُّ",
    "ٱلْوَكِيلُ",
    "ٱلْقَوِّىُّ",
    "ٱلْمَتِينُ",
    "ٱلْوَلِىُّ",
    "ٱلْحَمِيدُ",
    "ٱلْمُحْصِيُّ",
    "ٱلْمُبْصِيُّ",
    "ٱلْحَسِيبُ",
    "ٱلْجَلِيلُ",
    "ٱلْكَرِيمُ",
    "ٱلْرََّقِيبُ",
    "ٱلْمُجِيبُ",
    "ٱلْوَسِىُّ",
    "ٱلْحكِيمُ",
    "ٱلْوَدُودُ",
    "ٱلْمَجِيدُ",
    "ٱلْبَاعِثُ",
    "ٱلشََّهِيدُ",
    "ٱلْحَقُّ",
    "ٱلْوَكِيلُ",
    "ٱلْقَوِّىُّ",
    "ٱلْمَتِينُ",
    "ٱلْوَلِىُّ",
    "ٱلْحمِيدُ",
]

# List of the 99 English transliterations of the names
english_transliterations = [
    "Allah",
    "Ar-Rahman",
    "Ar-Raheem",
    "Al-Malik",
    "Al-Quddus",
    "As-Salam",
    "Al-Mu'min",
    "Al-Muhaymin",
    "Al-Aziz",
    "Al-Jabbar",
    "Al-Mutakabbir",
    "Al-Khaliq",
    "Al-Bari",
    "Al-Musawwir",
    "Al-Ghaffar",
    "Al-Qahhar",
    "Al-Wahhab",
    "Ar-Razzaq",
    "Al-Fattah",
    "Al-Alim",
    "Al-Qabid",
    "Al-Basit",
    "Al-Khafid",
    "Ar-Rafi",
    "Al-Mu'izz",
    "Al-Mudhill",
    "As-Sami",
    "Al-Basir",
    "Al-Hakim",
    "Al-Wadud",
    "Al-Majid",
    "Al-Ba'ith",
    "Ash-Shahid",
    "Al-Haqq",
    "Al-Wakil",
    "Al-Qawiyy",
    "Al-Matin",
    "Al-Waliyy",
    "Al-Hamid",
    "Al-Muhsi",
    "Al-Mubsi",
    "Al-Hasib",
    "Al-Jalil",
    "Al-Karim",
    "Ar-Raqib",
    "Al-Mujib",
    "Al-Wasi",
    "Al-Hakim",
    "Al-Wadud",
    "Al-Majid",
    "Al-Ba'ith",
    "Ash-Shahid",
    "Al-Haqq",
    "Al-Wakil",
    "Al-Qawiyy",
    "Al-Matin",
    "Al-Waliyy",
    "Al-Hamid",
    "Al-Muhsi",
    "Al-Mubsi",
    "Al-Hasib",
    "Al-Jalil",
    "Al-Karim",
    "Ar-Raqib",
    "Al-Mujib",
    "Al-Wasi",
    "Al-Hakim",
    "Al-Wadud",
    "Al-Majid",
    "Al-Ba'ith",
    "Ash-Shahid",
    "Al-Haqq",
    "Al-Wakil",
    "Al-Qawiyy",
    "Al-Matin",
    "Al-Waliyy",
    "Al-Hamid",
    "Al-Muhsi",
    "Al-Mubsi",
    "Al-Hasib",
    "Al-Jalil",
    "Al-Karim",
    "Ar-Raqib",
    "Al-Mujib",
    "Al-Wasi",
    "Al-Hakim",
    "Al-Wadud",
    "Al-Majid",
]

# List of the 99 English definitions for the names
english_definitions = [
    "The God",
    "The Most Gracious",
    "The Most Merciful",
    "The King",
    "The Most Holy",
    "The Source of Peace",
    "The Guardian of Faith",
    "The Protector",
    "The Almighty",
    "The Compeller",
    "The Supreme",
    "The Creator",
    "The Evolver",
    "The Fashioner",
    "The Forgiver",
    "The Subduer",
    "The Bestower",
    "The Provider",
    "The Opener",
    "The All-Knowing",
    "The Constrictor",
    "The Expander",
    "The Abaser",
    "The Exalter",
    "The Giver of Honour",
    "The Giver of Dishonour",
    "The All-Hearing",
    "The All-Seeing",
    "The Wise",
    "The Loving",
    "The Most Glorious",
    "The Resurrector",
    "The Witness",
    "The Truth",
    "The Trustee",
    "The Strong",
    "The Firm",
    "The Friend",
    "The Praiseworthy",
    "The Accounter",
    "The Reckoner",
    "The Mighty",
    "The Generous",
    "The Watchful",
    "The Responder",
    "The Vast",
    "The Wise",
    "The Loving",
    "The Most Glorious",
    "The Resurrector",
    "The Witness",
    "The Truth",
    "The Trustee",
    "The Strong",
    "The Firm",
    "The Friend",
    "The Praiseworthy",
    "The Accounter",
    "The Reckoner",
    "The Mighty",
    "The Generous",
    "The Watchful",
    "The Responder",
    "The Vast",
    "The Wise",
    "The Loving",
    "The Most Glorious",
    "The Resurrector",
    "The Witness",
    "The Truth",
    "The Trustee",
    "The Strong",
    "The Firm",
    "The Friend",
    "The Praiseworthy",
    "The Accounter",
    "The Reckoner",
    "The Mighty",
    "The Generous",
    "The Watchful",
    "The Responder",
    "The Vast",
    "The Wise",
    "The Loving",
    "The Most Glorious",
]

# Create a variable to store the start time
start_time = None

def update_stopwatch():
    if start_time is not None:
        elapsed_time = time.time() - start_time
        remaining_time = 780 - elapsed_time  # 13 minutes (780 seconds) for 99 names
        if remaining_time > 0:
            minutes, seconds = divmod(int(remaining_time), 60)
            stopwatch_label.config(text=f"Time Remaining: {minutes:02d}:{seconds:02d}")
            root.after(1000, update_stopwatch)
        else:
            stopwatch_label.config(text="Time's up!")

def submit_answer(correct_answer):
    global score, name_revealed, last_correct_answer_time
    guess = english_entry.get().strip()

    # Check if the guess is the correct answer with at least 65% accuracy
    if difflib.SequenceMatcher(None, guess.lower(), correct_answer.lower()).ratio() > 0.65:
        result_label.config(text="Correct!")
        english_entry.config(state="disabled")
        submit_button.config(state='disabled')
        name_revealed = False
        elapsed_time = time.time() - last_correct_answer_time
        last_correct_answer_time = time.time()

        # Scoring system
        if elapsed_time < 4:
            score += 2  # 200% score
        elif elapsed_time < 8:
            score += 1.5  # 150% score
        else:
            score += 1  # 100% score

        # Update the number of correct answers
        correct_answers_label.config(text=f"Correct Answers: {score}")
    else:
        result_label.config(text="Incorrect. The correct answer is: " + correct_answer)

    if current_name_index < total_names:
        root.after(1250, reveal_name)
    else:
        result_label.config(text="Quiz completed. Your score: {:.2f} points".format(score))

def reveal_arabic_name(i=0):
    if current_name_index < total_names:
        arabic_name = names_of_allah[current_name_index]
        if i <= len(arabic_name):
            revealed_arabic = arabic_name[:i]
            arabic_label.config(text=revealed_arabic, font=("Arial", 40))
            root.after(1250, lambda: reveal_arabic_name(i + 1))
        else:
            reveal_name()
            update_stopwatch()
    else:
        reveal_name()
        update_stopwatch()

def reveal_arabic_name(i=0):
    if current_name_index < total_names:
        arabic_name = names_of_allah[current_name_index]
        if i <= len(arabic_name):
            revealed_arabic = arabic_name[:i]
            arabic_label.config(text=revealed_arabic, font=("Arial", 40))
            root.after(1250, lambda: reveal_arabic_name(i + 1))
        else:
            root.after(1250, reveal_name)  # Move to the next name
    else:
        reveal_name()
        update_stopwatch()

def reveal_name():
    global name_revealed, current_name_index, last_correct_answer_time, start_time
    if current_name_index < total_names:
        arabic_name = names_of_allah[current_name_index]
        english_transliteration = english_transliterations[current_name_index]
        english_definition = english_definitions[current_name_index]

        arabic_label.config(text=arabic_name, font=("Arial", 40))  # Display the full Arabic name
        english_label.config(text="", font=("Arial", 20))
        definition_label.config(text=english_definition, font=("Arial", 10))
        name_revealed = True

        current_name_index += 1
        english_entry.delete(0, tk.END)
        english_entry.config(state="normal")
        english_entry.focus()

        correct_answer = english_transliteration
        submit_button.config(command=lambda: submit_answer(correct_answer))
        submit_button.state(['!disabled'])

        start_time = time.time()  # Start the stopwatch
        
def submit_answer(correct_answer):
    global score, name_revealed, last_correct_answer_time
    guess = english_entry.get().strip()

    # Check if the guess is the correct answer with at least 65% accuracy
    if difflib.SequenceMatcher(None, guess.lower(), correct_answer.lower()).ratio() > 0.65:
        result_label.config(text="Correct!")
        english_entry.config(state="disabled")
        submit_button.config(state='disabled')
        name_revealed = False
        elapsed_time = time.time() - last_correct_answer_time
        last_correct_answer_time = time.time()

        # Scoring system
        if elapsed_time < 4:
            score += 2  # 200% score
        elif elapsed_time < 8:
            score += 1.5  # 150% score
        else:
            score += 1  # 100% score

    else:
        result_label.config(text="Incorrect. The correct answer is: " + correct_answer)

    if current_name_index < total_names:
        root.after(1250, reveal_name)
    else:
        result_label.config(text="Quiz completed. Your score: {:.2f} points".format(score))

def on_entry_key_press(event):
    # Handle the Enter key press in the English entry field
    if name_revealed:
        reveal_name()

def enter_custom_name():
    # Function to enter a custom name
    custom_name = custom_name_entry.get()
    # Perform actions with the custom name as needed

root = tk.Tk()
root.title("99 Names of Allah Quiz")

stopwatch_label = ttk.Label(root, text="", font=("Arial", 12))
stopwatch_label.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

correct_answers_label = ttk.Label(root, text="Correct Answers: 0", font=("Arial", 12))
correct_answers_label.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

arabic_label = tk.Label(root, text="", font=("Arial", 40))
arabic_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

english_label = tk.Label(root, text="Guess: ", font=("Arial", 10))
english_label.grid(row=1, column=0, padx=10, pady=10)

definition_label = ttk.Label(root, text="", font=("Arial", 10))
definition_label.grid(row=1, column=1, padx=10, pady=10)

english_entry = ttk.Entry(root, font=("Arial", 10))
english_entry.grid(row=2, column=0, padx=10, pady=10)
english_entry.bind("<Return>", on_entry_key_press)

custom_name_entry = ttk.Entry(root, font=("Arial", 10))
custom_name_entry.grid(row=2, column=1, padx=10, pady=10)

custom_name_button = ttk.Button(root, text="Enter Custom Name", command=enter_custom_name)
custom_name_button.grid(row=2, column=2, padx=10, pady=10)

submit_button = ttk.Button(root, text="Submit", state='disabled')
submit_button.grid(row=2, column=3, padx=10, pady=10)

result_label = ttk.Label(root, text="", font=("Arial", 10))
result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

total_names = len(names_of_allah)
current_name_index = 0
name_revealed = False
score = 0
last_correct_answer_time = 0

reveal_arabic_name()
root.mainloop()
