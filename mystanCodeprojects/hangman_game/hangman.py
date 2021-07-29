"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is a Hangman game.
    The player can enter a alphabet as a guess.
    Then, this program appears the word looking
    like after the player guessing and shows the
    number of guess the player has.
    """
    num_left = N_TURNS
    showing = ''
    # The word looking like after the player guessing
    answer = random_word()
    for i in range(len(answer)):
        ch = '-'
        showing += ch
    while True:
        input_ch = make_guess(num_left, showing)
        if check_guess(input_ch, answer) is True:
            print('You are correct!')
            showing = cancel_dashed(input_ch, showing, answer)
            if showing == answer:
                break
        else:
            print('There is no '+input_ch+' in the words.')
            num_left -= 1
            if num_left == 0:
                break
    if showing == answer:
        print('You win!!! \nThe word was: ' + showing)
    if num_left == 0:
        print('You are completely hung :\'( ')


def cancel_dashed(guess, word, answer):
    """
    :param guess: an alphabet, the right guess made by player
    :param word: The word looks like that it hasn't completely been guessed correctly
    :param answer: a word, the correct answer
    :return: The word looks like that some of the word have been replaced by right guess
    """
    ans = ''
    for i in range(len(answer)):
        ans_ch = answer[i]
        ch = word[i]
        if ans_ch == guess:
            # Replace the showing string's dashes if the input_ch is a right guess.
            ans += guess
        else:
            ans += ch
            # Maintain the same word if the input_ch is not right.
    return ans


def check_guess(guess, answer):
    """
    :param guess: an alphabet, the guess made by player
    :param answer: a word, the correct answer
    :return: bool, if the guess is in the answer or not
    """
    for i in range(len(answer)):
        ch = answer[i]
        if ch == guess:
            return True


def make_guess(num, word):
    """
    :param num: int, the number of turns that player can guess
    :param word: The word looks like that it hasn't completely been guessed correctly
    :return: the guess made by player
    """
    print('The word looks like: ' + word)
    print('You have '+str(num)+' guesses left.')
    guess = str(input('Your guess: '))
    guess = guess.upper()
    while not guess.isalpha() or len(guess) != 1:
        # Player can enter only one alphabet.
        guess = str(input('Illegally format.\nYour guess: '))
    return guess


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
