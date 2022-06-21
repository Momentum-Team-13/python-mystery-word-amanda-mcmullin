import random


#get random word from text file
def random_word_selector(file):
    word_list = open(file, "r")
    random_word = random.choice(word_list.read().split())
    word_list.close()
    # print(random_word)
    return random_word

mystery_word = random_word_selector('test-word.txt')
print(mystery_word)


#display blanks/dashes for letters in random word
#join - joins items into a string; whatever is separating terms goes before .join
def mystery_word_with_blanks():
    mystery_word_blanks = []
    for i in range(len(mystery_word)):
        mystery_word_blanks.append('_')
    return ''.join(mystery_word_blanks)

mystery_word_blanks = mystery_word_with_blanks()
print(mystery_word_blanks)


#get user guess 
def user_guess():
    current_guesses = []
    current_user_guess = input("Guess a letter: ").lower()
    current_guesses.append(current_user_guess)
    print(current_user_guess)
    print(current_guesses)
user_guess()


def play_game():    
    pass


if __name__ == "__main__":
    play_game()
    