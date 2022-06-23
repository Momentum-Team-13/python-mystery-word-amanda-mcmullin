import random

######itemized steps that need to work for game to function 
#open, read, and close file
def open_file():
    file = "words.txt"
    # print("Your file is", file)
    with open(file) as open_file:
        read_file = open_file.readlines()
        # print(read_file) ***WORKS***
        return read_file
open_file()

##convert words from open and read .txt doc into a list
def create_word_list():
    word_list = []
    for item in open_file():
        for word in item.split():
            # print(word) ***WORKS***
            word_list.append(word)
    return word_list
create_word_list()

###randomly pick word from word list
def get_word():
    mystery_word = random.choice(create_word_list())
    print(mystery_word) #***WORKS***
    return mystery_word


####convert random word letters from string to list
def create_list():
    letter_list = []
    for letter in get_word():
        letter_list.append(letter)
    print(letter_list) #***WORKS***
    return letter_list
create_list()

#currently - with all lines below commented out - code above works perfectly

#####get user guess
def user_guess():
    user_inpt = input("Guess a letter: ")
    return user_inpt


######track number of guesses, store correct and incorrect guesses
def tracker(file):
    correct_guesses = []
    incorrect_guesses = []
    display = [(letter.replace(letter, "_")) for letter in file]
    print(display)
    while len(incorrect_guesses) < 8:
        letter = user_guess()
        #if single letter entered convert to lowercase
        if letter.isalpha() and len(letter) == 1:
            lower_guess = letter.lower()
            #if letter is in mystery word: add to correct guesses, notify user
            if lower_guess in file:
                if lower_guess not in correct_guesses:
                    correct_guesses.append(lower_guess)
                    print(f"Great guess! {lower_guess} is in the mystery word.")
                    #update display with correct letter or letters in the place of blanks
                    display = [(letter.replace(letter, "_")) if letter not in correct_guesses else letter for letter in file]
                    print(display)
                    #if all letters in display are correctly guessed, inform user and break the while loop
                    if display == correct_guesses:
                        print("You guessed the mystery word - YOU WIN!!!")
                        break
                else:
                    print("Oops! You already guessed that letter! Accidents happen - you will not lose a turn for this error. Please try again!")
            #guess is not in word - notify player and add guess to incorrect guesses
            else:
                print(f"{lower_guess} is not in the word.")
                incorrect_guesses.append(lower_guess)    
                #valid letter not entered by user - notify them and prompt to try again
        else:
            print("You did not enter a valid letter. Please try again!")    
        print(f"Correct letters guessed: {correct_guesses} \n Incorrect letters guessed: {incorrect_guesses}")
    print(f"You did not guess the mystery word, which is {mystery_word}. Game over.")


#combine all the components to play the game
def play_game():
    open_text_file = open_file()
    converted_file = create_word_list(open_text_file)
    obtain_word = get_word(converted_file)
    letters_of_mystery_word = create_list(obtain_word)
    print(letters_of_mystery_word)
    tracker(letters_of_mystery_word)

if __name__ == "__main__":
    play_game()