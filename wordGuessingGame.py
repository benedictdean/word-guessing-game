import random
word_bank = ['twin', 'matcha', 'niche', 'reels', 'skibidi']
word = random.choice(word_bank)

guessedWord = ['_'] * len(word)
attempts = 6

while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedWord))

  guess = input('Guess a letter: ').lower()
   
  if guess in word:
    for i in range(len(word)):
        if word[i] == guess:
            guessedWord[i] = guess
            print('Nice guess!')
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts))

  if '_' not in guessedWord:
    print('\nCongratulations!! You guessed the word: ' + word)
    break

if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word)