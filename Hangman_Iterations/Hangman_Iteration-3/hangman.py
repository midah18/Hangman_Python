import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


def random_fill_word(word):
    """
    a word is randomly picked out from thw list
    it loops the the word appending most of the letters
    replacing the appended letters with an underscore
    the new letter with the underscore is joined
    """
    x = random.randint(0, len(word)- 2)
    new_list = []
    letter = word[x]
    
    for i in word:
        if i == letter:
            new_list.append(i)
        else:
            new_list.append('_')
    j = ''.join(new_list)
    return(j)
    

def is_missing_char(original_word, answer_word, char):
    if char in original_word and char not in answer_word:
        return True
    else:
        return False


def fill_in_char(original_word, answer_word, char):
    """
    letter inputed by user is compared to the individual letters of the answer word
    to check if the letter is present
    """
    list_orignal = list(original_word)
    list_ans = list(answer_word)
    count = 0
    for x in list_orignal:
        if  x == char:
            list_ans[count] = x
        count += 1
    return ''.join(list_ans)


def do_correct_answer(original_word, answer, guess):
    """
    function name is equated to a variable named answer
    """
    answer = fill_in_char(original_word, answer, guess)
    return answer


def do_wrong_answer(answer, number_guesses):
    """
    if wrong letter is inputed:
        > message is printed
        > number of guesses is also printed
        > stickman is printed out in stages
    """
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)


def draw_figure(number_guesses):
    if number_guesses == 4:
        print("/"+"-"*4)
        print("|\n"*3+"|")
        print("_"*7)
    elif number_guesses == 3:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|\n"*3)
        print("_"*7)
    elif number_guesses == 2:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|"+" "*2+"/"+" "+"\\")
        print("|\n"*2)
        print("_"*7)
    elif number_guesses == 1:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|"+" "*2+"/|" +"\\")
        print("|"+" "*3 +"|")
        print("|")
        print("_"*7)
    elif number_guesses == 0:
        print("/"+"-"*4)
        print("|"+" "*3+"0")
        print("|"+" "*2+"/|"+"\\")
        print("|"+" "*3 +"|")
        print("|"+" "*2+"/ " +"\\")
        print("_"*7)


def run_game_loop(word, answer):
    """
    user input is asked for
    number of guesses is intialized to 5 and decreases per wrong letter
    if the words "quit" or "exit" is in user input, game is exited
    """
    print("Guess the word:", ''.join(answer))
    number_guesses = 5
    list_word = list(word)
    while answer != list_word and number_guesses > 0:
        if word == answer:
            return
        char_guess = get_user_input()

        if char_guess == "exit" or char_guess == "quit":
            print("Bye!")
            return
       
        if is_missing_char(word, answer, char_guess):
            answer = do_correct_answer(word, answer, char_guess)
            print(''.join(answer))
        else:
            number_guesses = number_guesses - 1
            do_wrong_answer(answer, number_guesses)  
    if number_guesses == 0:
        print("Sorry, you are out of guesses. The word was: " + word)
    else:
        print("Winner!!!")
    return


    print("Guess the word: "+str(answer))
    guess = get_user_input()
    if is_missing_char(word, answer, guess) is True:
        answer = do_correct_answer(word, answer, guess)
    else:
        do_wrong_answer(answer, 0)


if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)
