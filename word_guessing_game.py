import random

word_bank = ["rocks", "beach", "dog", "toy", "animal", "something"]
chosen_word = random.choice(word_bank)
total_guess = 3
out_of_guesses = False
guess_word = " "
guess_count = 0


while guess_word != chosen_word and not(out_of_guesses):
    goes_left = total_guess - guess_count
    guess_word = input("Enter your guess word: ")
    if guess_count == total_guess:
        out_of_guesses = True
    if guess_word == chosen_word:
        print("Correct! the word was " + chosen_word)
    elif guess_word != chosen_word and guess_count < 3:
        print("wrong! try again, you have " + str(goes_left) + " goes left")
        guess_count += 1

if out_of_guesses == True:
    print('You loose! you have ran out of goes')
    print('the word was ' + chosen_word)

    #this is just a git_hub test
    #1212
    #test test 12 12
