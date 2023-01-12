#!/usr/bin/env python
# coding: utf-8

# In[4]:
# ------------------------------------------------------------------------------------------------------------

# In[25]:
board=[" "," "," "," "," "," "," "," "," "," "]
test_board=["X","O","X","O","X","O","X","O","X"]


# In[26]:


from IPython.display import clear_output
def displaying_the_board(board):
    print(board[0] + "   |   " +board[1]+ "   |   " +board[2])
    print("------------------")
    print(board[3] + "   |   " +board[4]+ "   |   "+board[5])
    print("------------------")
    print(board[6] + "   |   " +board[7]+ "   |   "+board[8])
    


# In[27]:


displaying_the_board(board)

displaying_the_board(test_board)


# In[28]:


def player_input():
    marker=""
    #Ask player to choose X or O
    while marker!="X" and marker!="O":
        marker=input("Player 1 , Choose X or O: ").upper()
    if marker=="X":
        player1="X"
        player2="O"
    else:
        player1="O"
        player2="X"
    print(f'Player 1 is {player1} and Player 2 is {player2}')
    return player1,player2

    
    


# In[29]:


player_input()


# In[32]:


def place_marker(board,position,marker):
    board[position]=marker


# In[33]:


place_marker(test_board,0,"X")
displaying_the_board(test_board)


# In[34]:


def win_check(board,mark):
    return (board[0]==board[1]==board[2]==mark or  board[3]==board[4]==board[5]==mark or  board[6]==board[7]==board[8]==mark or 
     board[0]==board[3]==board[6]==mark or  board[1]==board[4]==board[7]==mark or  board[2]==board[5]==board[8]==mark or
     board[0]==board[4]==board[8]==mark or board[2]==board[4]==board[6]==mark)
    
    


# In[35]:


displaying_the_board(test_board)
win_check(test_board,"X" or "O")


# In[36]:


import random
def choose_first():
    rand=random.randint(0,1)
    if rand==0:
        return 'Player 2 goes first'
    else:
        return 'Player 1 goes first'


# In[37]:


choose_first()


# In[38]:


def space_check(board,position):
    return board[position]==" "


# In[39]:


def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
    return True


# In[40]:


full_board_check(board)


# In[41]:


def player_choice(board):
    position=10
    while position not in range(0,9) or not space_check(board,position):
        position= int(input("Choose a position between 0 and 8 : "))
    return position


# In[44]:


player_choice(board)


# In[46]:


def play_again():
    choice=input("Do you want to play again? Yes or No ?")
    return choice=="Yes".lower()
    


# In[47]:


play_again()


# In[ ]:


print("TIC-TAC-TOE")
while True:
    board=[" "," "," "," "," "," "," "," "," "," "]
    player1_marker, player2_marker = player_input()
    turn=choose_first()
    print(f'{turn}')
    play_game = input('Are you ready to play? Enter Y or N.')
    if play_game.lower()=="y":
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            displaying_the_board(board)
            position = player_choice(board)
            
            place_marker(board,position,player1_marker)

            if win_check(board,player1_marker):
                displaying_the_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    displaying_the_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            displaying_the_board(board)
            position = player_choice(board)
            place_marker(board,position,player2_marker)

            if win_check(board,player2_marker):
                displaying_the_board(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    displaying_the_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not play_again():
        break

            
    


# In[ ]:





# In[ ]:




