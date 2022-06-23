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
# open_file()

##convert words from open and read .txt doc into a list
def create_word_list(file):
    word_list = []
    for item in open_file():
        for word in item.split():
            # print(word) ***WORKS***
            word_list.append(word)
    return word_list
# create_word_list()

###randomly pick word from word list
def get_word(file):
    mystery_word = random.choice(create_word_list(file))
    # print(mystery_word) #***WORKS***
    return mystery_word


####convert random word letters from string to list
def create_list(file):
    letter_list = []
    for line in file:
        for word in line.split():
            letter_list.append(word)
    #print(letter_list) #***WORKS***
    return letter_list
# create_list()


#####get user guess
def user_guess():
    user_inpt = input("\nGuess a letter: ")
    return user_inpt


######track number of guesses, store correct and incorrect guesses
def tracker(file):
    correct_guesses = []
    incorrect_guesses = []
    display = [(letter.replace(letter, "_")) for letter in file]
    print(display)
    guesses_left = 8 
    while len(incorrect_guesses) < 8:
        letter = user_guess()
        #if single letter entered convert to lowercase
        if letter.isalpha() and len(letter) == 1:
            lower_guess = letter.lower()
            #if letter is in mystery word: add to correct guesses, notify user, update display
            if lower_guess in file:
                if lower_guess not in correct_guesses:
                    correct_guesses.append(lower_guess)
                    print(correct_guesses)
                    display = [(letter.replace(letter, "_")) if letter not in correct_guesses else letter for letter in file]
                    print("\n")
                    print(display)
                    print(f"\nGreat guess! {lower_guess} is in the mystery word.") #works
                    if display == file:
                        print("\nCongratulations - you won!")
                        break #works

            elif lower_guess in correct_guesses or lower_guess in incorrect_guesses:
                print("Oops! You already guessed that letter! Accidents happen - you will not lose a turn for this error. Please try ain!") #works
                
            else:
                print(f"{lower_guess} is not in the word.") #works
                guesses_left -= 1
                incorrect_guesses.append(lower_guess) 

    #valid letter not entered by user - notify them and prompt to try again
        elif not letter.isalpha():
            print("You did not enter a valid letter. Please try again!")    #works
        print(f"Correct letters guessed: {correct_guesses} \t\tIncorrect letters guessed: {incorrect_guesses} \t\tGuesses left: {guesses_left}") #works
    if guesses_left == 0:
        print(f"You did not guess the mystery word, which is {file}. Game over.")


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