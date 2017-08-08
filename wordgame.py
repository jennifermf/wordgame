"""a hangman-style game; future updates will allow choosing how long the word should be!"""

import random

def pick_word(difficulty):         # picks from a list of words
    # would like to update to pull from a txt file
    e = ['mouse', 'house', 'ducks', 'coffee', 'beans', 'glasses', 'flower', 'tape', 'doorway', 'window', 'cars', 'faint', 'sandbox', 'peanut', 'parsley', 'boxes', 'darling', 'blackness', 'barking', 'fallen', 'farce', 'whisker']
    m = ['outlast', 'witch', 'nerves', 'faint', 'sandy', 'vines', 'batteries', 'razors', 'vegan', 'chorus',
    'parsed', 'turtle', 'giraffe', 'minced', 'sewing', 'visible', 'double', 'trouble', 'tasty', 'grease', 'soiled', 'strength', 'rolling', 'jumping', 'jiggle', 'rugged', 'frisky', 'fauna']
    h = ['intensified', 'rigging', 'swept', 'jackboot', 'copyright', 'alliterating', 'slashed', 'pittance', 'electricity', 'beater', 'chalkboard', 'woodsy', 'outlaw', 'sluggish', 'arbitrate', 'devoured', 'dismissive', 'epiphany', 'illegible', 'oscillate', 'evangelize', 'veganism', 'annihilate', 'ataxia', 'collegiate', 'paleolithic', 'glucose', 'cautioned', 'supplier', 'impounded', 'primitive', 'immobility']

    if difficulty == 'e':
        answer = random.choice(e).upper()  # need to specify short length
    elif difficulty == 'm':
        answer = random.choice(m).upper()  # need to specify medium length
    elif difficulty == 'h':
        answer = random.choice(h).upper()  # need to specify long length
    else:
        print 'Invalid choice! Why don\'t you play the easy level?'
        answer = random.choice(e).upper()  # need to specify short length
    return answer

    #word_list = open("wordlist.txt","w+")
    #word = random.choice(word_list).upper()
    #word_list.close()
    #return random.choice(words).upper()
    #return random.choice(word_list).upper()
    #need to choose based on len(word)

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
    difficulty = raw_input('Welcome to non-violent Hangman! Choose (e)asy, (m)edium, or (h)ard:  ')
    answer = pick_word(difficulty)
    choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    guesses = []
    guessed = False
    print 'This word contains {} letters.'.format(len(answer))
    while not guessed:
        text = '\nEnter 1 letter or {}-letter word.\nYour choices are: {}:  '.format(len(answer), choices)
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