from tkinter import *

# To indicate whose turn. True for player 1; False for player 2
flag = True
 
# To store what user has pressed (Stone/Paper/Scissor)
input1 = ''
input2 = ''

def record_name():
    global root, player1, player2
    root = Tk()
    Label(text="Player 1 Name: ").grid(row=1, column=0, padx=10, pady=10)
    Label(text="Player 2 Name: ").grid(row=2, column=0, padx=10, pady=10)

    player1 = Entry()
    player1.grid(row=1, column=1, padx=10)

    player2 = Entry()
    player2.grid(row=2, column=1, padx=10)
    
    start_button = Button(text="Start the Game", command=start_game)
    start_button.grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()

def start_game():
    # => player1_points and player2_points are labels for displaying points.
    # => Declaring them global so that the in case of win, they can be updated outside the scope
    #    of this function. 
    # => Declaring active_player label global because it needs to be updated when turn changes.
    # => Declaring name1 and name2 global because updating active_player label will require
    #    the name of players who are playing.

    global root, player1_points, player2_points, active_player, name1, name2, result_label
    
    name1, name2 = player1.get(), player2.get()

    root.destroy()
    root = Tk()
    root.title("Stone Paper Scissor  " + name1 + " vs " + name2)
    
    Label(text=name1 + ":", fg='black',bg='red').grid(row=0, column=0, padx=20, pady=20)
    Label(text=name2 + ":", fg='black',bg='red').grid(row=0, column=3, padx=20  , pady=20)

    active_player = Label(text= name1 + "'s turn", fg='black',bg='yellow')
    active_player.grid(row=1, column=2, padx=30)

    player1_points = Label(text=0)
    player1_points.grid(row=0, column=1, padx=5)

    player2_points = Label(text=0)
    player2_points.grid(row=0, column=4, padx=10)

    Button(text="Stone", command=lambda: handle_turn('Stone'), width=10, font=('Times New Roman',10)).grid(row=2, column=2, pady=6)
    Button(text="Paper", command=lambda: handle_turn('Paper'), width=10, font=('Times New Roman',10)).grid(row=3, column=2, pady=6)
    Button(text="Scissor", command=lambda: handle_turn('Scissor'), width=10, font=('Times New Roman',10)).grid(row=4, column=2, pady=6)
    
    Button(text='Reset', command=reset, width=10, font=('Times New Roman',10), border='2px').grid(row=5, column=2, pady=20)

    result_label = Label(text='-By Ajay Jain', fg='white', bg='grey')
    result_label.grid(row=6, column=2, pady=5)

def handle_turn(input_):
    # => Flag is to indicate whose turn.. Declaring it global will allow to update it in function
    # => input1 and input2 stores what player has choosed (among stone/paper/scissor)
    # => player1_points and player2_points, which were defined in start_game function are used
    #    to update points.
    # => active_player is a label which will be updated when and where flag('whose turn')
    #    is updated.
    
    global flag, input1, input2, player1_points, player2_points, active_player
    if flag==True:       # Player 1's turn
        input1 = input_
        flag= False
        active_player['text'] = name2 + "'s turn"
    else:                # Player 2's turn
        input2 = input_
        flag = True
        active_player['text'] = name1 + "'s turn"
     
    # breaking the function in case either of the input is not yet collected.
    if input1 == '' or input2 == '' :
        return

    winner = check_win()
    # return True if player 1 won and return False if player 2 won and None in case of draw.
    # Player who wins gets 1st chance in next game. So updating Flag variable to player who won
    if winner == None:               # Match DRAW!
        pass
    elif winner:                     # Player 1 won
        player1_points['text'] +=1
        flag = True
        active_player['text'] = name1 + "'s turn"
    elif not winner:                 # Player 2 won
        player2_points['text']+=1
        flag = False
        active_player['text']= name2 + "'s turn"
    else:
        pass   
        
    # Resetting them for the new match.    
    input1 = ''
    input2 = ''    

def check_win():
    global result_label
    result_label['text'] = ''
    
    # return True if player 1 won and return False if player 2 won and None in case of draw.
    if input1 == 'Stone' and input2 == 'Paper':
        result_label['text']= name2 + ' won'
        return False
    elif input1 == 'Paper' and input2 == 'Scissor':
        result_label['text']= name2 + ' won'
        return False
    elif input1 == 'Scissor' and input2 == 'Stone':
        result_label['text']=name2 + ' won'
        return False    
    elif input1 == 'Stone' and input2 == 'Scissor':
        result_label['text']=name1 + ' won'
        return True
    elif input1 == 'Paper' and input2 == 'Stone':
        result_label['text']=name1 + ' won'
        return True
    elif input1 == 'Scissor' and input2 == 'Paper':
        result_label['text']=name1 + ' won'
        return True    
    elif input1 == input2:
        result_label['text']='Match was draw.'
        return None
    else:
        pass

def reset():
    global flag, player1_points, player2_points, input1, input2, active_player, result_label

    flag = True
    active_player['text'] = name1 + "'s turn"

    player1_points['text'] = player2_points['text'] = 0
    input1 = input2 = ''

    result_label['text'] = '-By Ajay Jain'
        
record_name()

