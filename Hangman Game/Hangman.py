import random

# List of 5 predefined words
words = ["python", "engineer", "laptop", "coding", "matrix"]

# Pick a random word
word = random.choice(words)

# To store guessed letters
guessed_letters = []

# Incorrect guesses allowed
max_wrong = 6
wrong_guesses = 0

# Display word with blanks
display_word = ["_"] * len(word)

print("🎯 Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("You have 6 wrong guesses.\n")

# Game loop
while wrong_guesses < max_wrong and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only ONE alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct!\n")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print("❌ Wrong!\n")

# Final result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("💀 Game Over! The word was:", word)
