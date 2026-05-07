import random

words = ["python", "apple", "laptop", "school", "garden"]

word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

display_word = ["_"] * len(word)

print("===== Welcome to Hangman Game =====")

while incorrect_guesses < max_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))
    print("Remaining chances:", max_guesses - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        print("Wrong Guess!")
        incorrect_guesses += 1

if "_" not in display_word:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n Game Over!")
    print("The correct word was:", word)