import random
import pandas as pd

# Predefined word list
words = ["apple", "banana", "grape", "orange", "mango"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []
stats = []

print("🎮 Welcome to Hangman with Pandas!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ Already guessed.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        result = "Correct"
    else:
        attempts -= 1
        result = "Wrong"

    # Record each guess in stats
    stats.append({
        "Guess": guess,
        "Result": result,
        "Attempts Left": attempts,
        "Current Word": "".join(guessed)
    })

# Final result
if "_" not in guessed:
    print("\n🎉 You won! The word was:", word)
    outcome = "Win"
else:
    print("\n💀 You lost! The word was:", word)
    outcome = "Loss"

# Create DataFrame from stats
df = pd.DataFrame(stats)
df["Game Outcome"] = outcome

print("\n📊 Game Summary:")
print(df)

df.to_csv("hangman_game_stats.csv", index=False)
