import fnmatch

from hangman_helper import *


def update_word_pattern(word, pattern, letter):
    """
    Takes as parameters the word, the current pattern, and a letter and returns an updated pattern containing the given
    letter.
    :param word: entire word
    :param pattern: current pattern
    :param letter: letter that was guessed
    :return: updated pattern in string format
    """
    pattern_list = list(pattern)
    word_list = list(word)
    new_pattern = ""
    for i in range(len(word)):
        if word_list[i] == letter:
            pattern_list[i] = letter
    return new_pattern.join(pattern_list)


# print(update_word_pattern('apple', '___l_', 'p'))


def run_single_game(list_words, score):
    """
    The function receives a list of words and a number of points with which the player starts the game and runs one game
    The function returns the number of points the player has at the end of the game.
    :param list_words: list of words
    :param score: current score
    :return: updated score
    """
    wrong_guess_lst = []
    word = get_random_word(list_words)
    message = "Enter your guess"
    pattern = ''
    guessed_letter_list = []
    for i in word:
        pattern = pattern + "_"
    while "_" in pattern and score > 0:
        display_state(pattern, wrong_guess_lst, score, message)
        user_input = get_input()
        letter = user_input[1]
        if user_input[0] == 1 and len(str(letter)) > 1:
            message = "Incorrect input"
            guessed_letter_list.append(letter)
            continue
        if user_input[0] == 1 and not letter.isalpha():
            message = "Incorrect input"
            guessed_letter_list.append(letter)
            continue
        if user_input[0] == 1 and not letter.islower():
            message = "Incorrect input"
            guessed_letter_list.append(letter)
            continue
        if user_input[0] == 1 and letter in guessed_letter_list:
            message = "Letter already guessed, please guess another letter"
            guessed_letter_list.append(letter)
            continue
        if user_input[0] == 1 and letter.isalpha() and letter.islower():
            score = score - 1
            if letter not in word:
                message = "Incorrect Guess! Try Again"
                wrong_guess_lst.append(letter)
                guessed_letter_list.append(letter)
                continue
            if letter in word:
                pattern = update_word_pattern(word, pattern, letter)
                n = word.count(letter)
                points = n * (n + 1) // 2
                score = score + points
                message = "Guess the next letter"
                guessed_letter_list.append(letter)
                continue
        if user_input[0] == 2:
            score = score - 1
            if user_input[1] == word:
                n = pattern.count('_')
                points = n * (n + 1) // 2
                score = score + points
                pattern = word
                continue
            else:
                message = "Incorrect word! Guess a word or letter again"
                continue
    if score <= 0:
        message = "You Lose"
    elif "_" not in pattern:
        message = "You Won"
    display_state(pattern, wrong_guess_lst, score, message)
    return score


def main():
    list_words = load_words(file='words.txt')
    initial = POINTS_INITIAL
    interested = True
    games_played = 0
    while interested:
        score = run_single_game(list_words, initial)
        games_played += 1
        print("Your have finished the Game!!")
        print("Games Played: " + str(games_played))
        print("Current Score: " + str(score))
        if score > 0:
            interested = play_again("Do you want to play another round?")
            initial = score
        if score == 0:
            interested = play_again("Do you want to play a new game again?")
            initial = POINTS_INITIAL
            games_played = 0


if __name__ == "__main__":
    main()
