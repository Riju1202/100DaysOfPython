# Day 6 - Practice done in reeborgs world site
# Day 7 - Hangman Project
import wonderwords
import hangman_resources
ran = wonderwords.RandomWord()
diff = input("Choose a difficulty level: Easy, Medium, Hard?\n").lower()
if diff == "easy":
    lives = 10
    word = ran.word(word_min_length=3, word_max_length=8).lower()
elif diff == "medium":
    lives = 7
    word = ran.word(word_min_length=5, word_max_length=10).lower()
elif diff == "hard":
    lives = 5
    word = ran.word(word_min_length=8, word_max_length=15).lower()
else:
    print("Invalid Input")
    exit()
print(f"Word is {word}")
ans = "_" * len(word)
hangman_resources.logo()
s = hangman_resources.states()
while lives > 0:
    new_word = ""
    print(f"Your word is \n {ans}")
    guess = input("Guess a letter: ").lower()
    if guess in word:
        print("You guessed right")
        for i in range(len(word)):
            if word[i] == guess:
                new_word += guess
            else:
                new_word += ans[i]
        ans = new_word# use new_word logic to update ans or use "ans = ans[:i] + guess + ans[i+1:]""
    else:
        print("You guessed wrong")
        lives -= 1
        print(f"You have {lives} lives left")
    if ans == word:
        print("You won")
        break
    if lives < 7:
        print(s.states[6-lives])
if lives == 0:
    print("You lost")
print(f"The word was {word}")
hangman_resources.over()