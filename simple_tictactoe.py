
# coding: utf-8

# In[1]:


from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])           
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])                   
    
    
def player_input():   
    
    marker=''
    
    while marker!='X'and marker!='O':
        marker=input('Player1: Choose X or O:').upper()
        
    if marker=='X':
        
        return('X','O')
    else:
        return('O','X')
    


# In[2]:


def place_marker(board,marker,position):
    board[position]=marker


# In[3]:


def win_check(board,mark):
    
    return((board[7]==mark and board[8]==mark and board[9]==mark) or
           (board[4]==mark and board[5]==mark and board[6]==mark) or
           (board[1]==mark and board[2]==mark and board[3]==mark) or
           (board[7]==mark and board[4]==mark and board[1]==mark) or
           (board[8]==mark and board[5]==mark and board[2]==mark) or
           (board[9]==mark and board[6]==mark and board[3]==mark) or
           (board[7]==mark and board[5]==mark and board[3]==mark) or
           (board[9]==mark and board[5]==mark and board[1]==mark))


# In[4]:


import random

def choose_first():
    flip=random.randint(0,1) 
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[5]:


def space_check(board,position):
    return board[position]== ' '


# In[6]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        
    return True


# In[7]:


def player_choice(board):
    position=0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position: (1-9)'))
        
    return position      


# In[8]:


def replay():
    choice=input('Do you want to play again? Enter Yes or No')
    return choice=='Yes'


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    the_board=[' ']*10
    player1_marker,player2_marker= player_input()
    
    turn=choose_first()
    print(turn+' will go first')
    
    play_game=input('Ready to play? y or n?')
    
    if play_game=='y':
        game_on=True
    else:
        game_on=False
            
    while game_on:
        
        if turn=='Player 1':
            
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print ('PLAYER 1 HAS WON!')
                game_on=False
            else:
                if full_board_check(the_board):
                        display(the_board)
                        print("TIE GAME!")
                        break
                else:
                    turn='Player 2'
                        
        else:
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print ('PLAYER 2 HAS WON!')
                game_on=False
            else:
                if full_board_check(the_board):
                        display(the_board)
                        print("TIE GAME!")
                        break
                else:
                    turn='Player 1'
                        
if not replay():
    break

