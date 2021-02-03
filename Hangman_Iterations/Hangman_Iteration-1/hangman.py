import random


def read_file(file_name):
    """
    opens and reads the file
    stores the words in a variable named words
    """
    openfile = open(file_name, "r")
    words = openfile.readlines()
    return words


def select_random_word(words):
    """
    a word in the list(words) are randomly selected
    an underscore replaces most of the letters
    """
    x = random.randint(0,len(words) - 1)
    word = words[x]
    y = random.randint(0, len(word) - 2)
    letter = word[y]
    var = word.replace(letter, "_")

    print("Guess the word: "+var)
    return word

#Lekau is the best

def get_user_input():
    """
    user input is asked for and returned
    """
    m_letter = input("Guess the missing letter: ")
    return m_letter


def run_game(file_name):
    """
    This is the main game code. 
    this is where it starts
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

