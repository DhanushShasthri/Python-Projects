stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
#words in game
word_list=["bottle","book","laptop","pen","phone","bag"]
#choosing random number
chosen_word=random.choice(word_list)
display=[]
#attempts or mistakes in game
lives=6
#length of chosen word
word_length=len(chosen_word)

for i in range (word_length):
    display+="_"
print(display)
game_ended= False
while not game_ended:
    guess=input("Guess a letter:").lower()
    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
            print(display)
    if guess not in chosen_word:
            lives=lives-1
            if lives==0:
                game_ended=True
                print("you lose, person is no more")


if "_" not in display:
    game_ended=True
    print("You win")
    print(stages[lives])
