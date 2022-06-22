import random

#open and read file to get word
def get_word_to_guess():
    open_file = open("test-word.txt")
    #print(open_file.read())
    string_word = (open_file.read())
    random_list = string_word.split()
    mystery_word = random.choice(random_list)
    return mystery_word

#get user guess
def user_guess():
    user_inpt = input("Guess a letter: ")
    if len(user_inpt) == 1 and user_inpt.isalpha():
        letter = user_inpt.lower()
        print(f"You guessed: {letter}")
        return letter
    else:
        print("\nThat guess was not a letter.\n")
        return user_guess()


def play_game():
    while True:
        get_word = get_word_to_guess()
        #print(get_word)

        def new_strings(get_word):
            return list(get_word)
        string_list = new_strings(get_word)
        split_list = string_list
        #print(split_list[:-1])
        new_list = [(character.replace(character, "_")) for character in split_list[:-1]]
        print(f"\n {new_list}\n")
        guess = []
        while len(guess) <= 7:
            user_guess = user_guess()
            # #if correct
            # if user_guess in 
            guess.append(user_guess())
            new_list = [(character.replace(character, "_")) if character not in guess else character for character in split_list[:-1]]
            print(f"\nYou have {8 - len(guess)} guesses remaing \n {new_list} \n")
        else:
            print(f"\nYou are out of guesses, the word was: {get_word} \n")
        play_again = input("Play agin? y/n ")
        if play_again == "n":
            break


if __name__ == "__main__":
    play_game()