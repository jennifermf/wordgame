"""a hangman-style game; future updates will allow choosing how long the word should be!

wordfile.txt source:
http://www.ef.com/english-resources/english-vocabulary/top-3000-words/
"""

import random

def pick_word():         # picks from a list of words
    
    wordfile = [line.strip() for line in open('wordslist.txt')]
    return random.choice(wordfile).upper()
    

def check(answer,guesses,guess):
    status = ''
    matches = 0
    for letter in answer:
        if letter in guesses:
            status += letter
        else:
            status += '*'
        if letter == guess:
            matches += 1
    if matches > 1:
        print 'Yes! The word contains {} {}\'s.'.format(matches,guess)
    elif matches == 1:
        print 'Yes! The word contains the letter {}.'.format(guess)
    else:
        print 'Sorry, no {}\'s.'.format(guess)
    return status

def main():
    print('\nWelcome to non-violent Hangman! Let\'s begin!')
    answer = pick_word()
    choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    guesses = []
    guessed = False
    print 'This word contains {} letters.'.format(len(answer))
    while not guessed:
        text = 'Enter 1 letter or {}-letter word.\nYour choices are: {}:  '.format(len(answer), choices)
        guess = raw_input(text)
        guess = guess.upper()
        choices = choices.replace(guess, '-')
        if guess in guesses:
            print 'You already guessed {}.'.format(guess)
        elif not guess.isalpha():
            print 'Please choose an alphabetic character.'
        elif len(guess) == len(answer):
            guesses.append(guess)
            if guess == answer:
                guessed = True
            else:
                print 'Sorry, that is incorrect.'
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(answer, guesses, guess)
            if result == answer:
                guessed = True
            else:
                print '\n{}'.format(result)
        else:
            print 'That was an invalid entry.'
    print 'Nice job! The word is {}. You won in {} tries. :)\nThanks for playing! '.format(answer, len(guesses))
main()
# future iterations: repeat the game as often as the user wishes
