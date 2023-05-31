#!/usr/bin/env python
# coding: utf-8

# In[2]:


#from IPython.display import clear_output
#clear_output()


# In[3]:


def player_XorO():
    global player1
    global player2
    player1 = ''
    player2 = ''
    print('Welcome to Tic Tac Toe!')
    while player1 not in ['X','O']:
        player1 = input("Player 1: Do you want to be X or O: ")
        if isinstance(player1, str) != True or player1.upper() not in ['X','O']:
            print("Oops! Something went wrong, please only choose X or O")
        if player1.upper() == 'X':
            player2 = 'O'
            player1 = 'X'
        elif player1.upper() == 'O':
            player2 = 'X'
            player1 = 'O'
    print(f"Player 1 will be {player1}! Player 1 will go first")


# In[4]:


placeholder = ['#','  ','  ','  ','  ','  ','  ','  ','  ','  ']
def board():
    print(f'   {placeholder[7]} | {placeholder[8]} | {placeholder[9]}   ')
    print( '-------------')
    print(f'   {placeholder[4]} | {placeholder[5]} | {placeholder[6]}   ')
    print( '-------------')
    print(f'   {placeholder[1]} | {placeholder[2]} | {placeholder[3]}   ')


# In[5]:


def win_check1():
    global game_on 
    global turn_engine
    if ( (placeholder[1]== placeholder[2] == placeholder[3] == 'X')
    or (placeholder[4] == placeholder[5] == placeholder[6] == 'X') 
    or (placeholder[7] == placeholder[8] == placeholder[9] == 'X') 
    or (placeholder[7] == placeholder[4] == placeholder[1] == 'X') 
    or (placeholder[8] == placeholder[5] == placeholder[2] == 'X') 
    or (placeholder[9] == placeholder[6] == placeholder[3] == 'X') 
    or (placeholder[7] == placeholder[5] == placeholder[3] == 'X') 
    or (placeholder[1] == placeholder[5] == placeholder[9] == 'X') 
    or (placeholder[1] == placeholder[2] == placeholder[3] == 'O') 
    or (placeholder[4] == placeholder[5] == placeholder[6] == 'O') 
    or (placeholder[7] == placeholder[8] == placeholder[9] == 'O') 
    or (placeholder[7] == placeholder[4] == placeholder[1] == 'O') 
    or (placeholder[8] == placeholder[5] == placeholder[2] == 'O') 
    or (placeholder[9] == placeholder[6] == placeholder[3] == 'O') 
    or (placeholder[7] == placeholder[5] == placeholder[3] == 'O') 
    or (placeholder[1] == placeholder[5] == placeholder[9] == 'O') ): 
        print("Game Over! Congratulations Player 1 is the winner!")
        game_on = False
        turn_engine = ''
    elif '  ' not in placeholder:
        print("Game Over! It's a draw")
        game_on = False
        turn_engine = ''


# In[6]:


def win_check2():
    global game_on 
    global turn_engine
    if ( (placeholder[1]== placeholder[2] == placeholder[3] == 'X')
    or (placeholder[4] == placeholder[5] == placeholder[6] == 'X') 
    or (placeholder[7] == placeholder[8] == placeholder[9] == 'X') 
    or (placeholder[7] == placeholder[4] == placeholder[1] == 'X') 
    or (placeholder[8] == placeholder[5] == placeholder[2] == 'X') 
    or (placeholder[9] == placeholder[6] == placeholder[3] == 'X') 
    or (placeholder[7] == placeholder[5] == placeholder[3] == 'X') 
    or (placeholder[1] == placeholder[5] == placeholder[9] == 'X') 
    or (placeholder[1] == placeholder[2] == placeholder[3] == 'O') 
    or (placeholder[4] == placeholder[5] == placeholder[6] == 'O') 
    or (placeholder[7] == placeholder[8] == placeholder[9] == 'O') 
    or (placeholder[7] == placeholder[4] == placeholder[1] == 'O') 
    or (placeholder[8] == placeholder[5] == placeholder[2] == 'O') 
    or (placeholder[9] == placeholder[6] == placeholder[3] == 'O') 
    or (placeholder[7] == placeholder[5] == placeholder[3] == 'O') 
    or (placeholder[1] == placeholder[5] == placeholder[9] == 'O') ): 
        print("Game Over! Congratulations Player 2 is the winner!")
        game_on = False
        turn_engine = ''
    elif '  ' not in placeholder:
        print("Game Over! It's a draw")
        game_on = False
        turn_engine = ''


# In[7]:


def game_engine1():
    global player1
    global turn_engine
    global placeholder
    player_position = ''
    success = False
    while success == False:
        player_position = input("Player 1! Choose your position: (1-9): ")
        if player_position.isdigit():
            if int(player_position) in range(1, 10):
                if placeholder[int(player_position)] == '  ':
                    success = True
                else:
                    print('Oops, that position is filled! Please choose a number from 1-9 to choose your position')
            else:
                print('Oops, you picked an invalid number! Please choose a number from 1-9 to choose your position')
        else:
            print('Oops, you did not pick a number! Please choose a number from 1-9 to choose your position')
    placeholder[int(player_position)] = player1
    turn_engine = True


# In[8]:


def game_engine2():
    global player2
    global turn_engine
    global placeholder
    player_position = ''
    success = False
    while success == False:
        player_position = input("Player 2! Choose your position: (1-9): ")
        if player_position.isdigit():
            if int(player_position) in range(1, 10):
                if placeholder[int(player_position)] == '  ':
                    success = True
                else:
                    print('Oops, that position is filled! Please choose a number from 1-9 to choose your position')
            else:
                print('Oops, you picked an invalid number! Please choose a number from 1-9 to choose your position')
        else:
            print('Oops, you did not pick a number! Please choose a number from 1-9 to choose your position')
    placeholder[int(player_position)] = player2
    turn_engine = False


# In[9]:


def replay():
    global game
    global placeholder
    ask = ''
    success = True
    while success:
        ask = input("Do you want to play again? Yes or No?: ")
        if ask.upper() not in ['YES','NO']:
            print("Please only choose only Yes or No")
        else:
            if ask.upper() == 'YES':
                placeholder = ['#','  ','  ','  ','  ','  ','  ','  ','  ','  ']
                success = False
                #
            elif ask.upper() == 'NO':
                success = False
                game = False


# In[10]:


placeholder = ['#','  ','  ','  ','  ','  ','  ','  ','  ','  ']
game = True

while game == True:
    turn_engine = False # the condition for player1/player2 move
    game_on = True # the continue game condition
    player_position = ''
    player_XorO()#sets the symbol X or O for player1 and 2
    board()#prints the board
    while game_on == True:
        while turn_engine == False:
            game_engine1() #fills and prints the new board after each turn (for player 1)
            #clear_output()
            board()
            win_check1() # to check if the board has any rows filled
            break
        while turn_engine == True:
            game_engine2() #fills and prints the new board after each turn (for player 2)
            #clear_output()
            board() 
            win_check2() #to check if the board has any rows filled
            break
    replay() #replay option//closes the
