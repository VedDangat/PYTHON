import random

print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/ ''')

stages = [
    '''
       _______
         |/      |
         |      (_)
         |      \\|/
         |       |
         |      / \\
         |
        _|___
    ========
    ''',
    '''
       _______
         |/      |
         |      (_)
         |      \\|/
         |       |
         |      / 
         |
        _|___
    ========
    ''',
    '''
       _______
         |/      |
         |      (_)
         |      \\|/
         |       |
         |      
         |
        _|___
    ========
    ''',
    '''
       _______
         |/      |
         |      (_)
         |      \\|/
         |       
         |      
         |
        _|___
    ========
    ''',
    '''
       _______
         |/      |
         |      (_)
         |      
         |     
         |      
         |
        _|___
    ========
    ''',
    '''
       _______
         |/      |
         |      
         |      
         |      
         |      
         |
        _|___
    ========
    '''
]

word_list = ["cricket", "football", "hockey","tennis","badminton"]
chosen_word = random.choice(word_list)

lives = 5
guessed_letters = []
game_over = False

display = "_" * len(chosen_word)
print("Word:", display)

while not game_over:
    guess = input("\nEnter your guess: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print("Wrong guess!")

    new_display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            new_display += letter
        else:
            new_display += "_"

    display = new_display

    print("Word:", display)
    print("Lives Left:", lives)
    print(stages[lives])

    if lives == 0:
        game_over = True
        print("YOU LOSE")
        print("The word was:", chosen_word)

    if "_" not in display:
        game_over = True
        print("YOU WIN")
