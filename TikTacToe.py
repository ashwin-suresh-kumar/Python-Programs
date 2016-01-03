'''
Created on Dec 22, 2015

@author: Ashwin Suresh Kumar
'''
from random import randint

first_row = ['NA']*3
second_row = ['NA']*3
third_row = ['NA']*3

flag_p1 = 0
#flag_p2 = 0

def print_board():
    global first_row
    global second_row
    global third_row
    print "\n"
    print "%s  | %s | %s" %(first_row[0],first_row[1],first_row[2])
    print "--------------"
    print "%s  | %s | %s"%(second_row[0],second_row[1],second_row[2])
    print "--------------"
    print "%s  | %s | %s"%(third_row[0],third_row[1],third_row[2])
    print "\n"
def check_win(player):
    global first_row
    global second_row
    global third_row
        
    if( first_row[0] == first_row[1] == first_row[2] == 'X' or first_row[0] == first_row[1] == first_row[2] == 'O' or
        first_row[0] == second_row[0] == third_row[0] == 'X' or first_row[0] == second_row[0] == third_row[0] == 'O' or
        first_row[0] == second_row[1] == third_row[2] == 'X' or first_row[0] == second_row[1] == third_row[2] == 'O' or
        first_row[1] == second_row[1] == third_row[1] == 'X' or first_row[1] == second_row[1] == third_row[1] =='O' or
        second_row[0] == second_row[1] == second_row[2] == 'X' or second_row[0] == second_row[1] == second_row[2] == 'O' or
        first_row[2] == second_row[1] == third_row[0] == 'X' or first_row[2] == second_row[1] == third_row[0] == 'O' or
        first_row[2] == second_row[2] == third_row[2] == 'X' or first_row[2] == second_row[2] == third_row[2] == 'O' or
        third_row[0] == third_row[1] == third_row[2] == 'X' or third_row[0] == third_row[1] == third_row[2] == 'O' or
        third_row[2] == second_row[1] == first_row[0] =='X' or third_row[2] == second_row[1] == first_row[0] == 'O' ):
        print 'Player %s is the winner' %player
    else:
        swap_player()
    
def swap_player():
    global flag_p1
    if (flag_p1 == 1):
        flag_p1 = 0
        play(2)
    else:
        play(1)
        
def insert_to_board(player,p_input,symbol):
    position = int(p_input)
    global first_row
    global second_row
    global third_row
    
    if(position != 1 or position != 2 or position != 3 or position != 4 or position != 5 or position != 6 or position != 7 or position != 8 or position != 9):
        if(position == 1 or position == 2 or position == 3):
            if(first_row[0] == 'NA' or first_row[1] == 'NA' or first_row[2] == 'NA'): #list full check
                if(first_row[position-1] == 'NA'): #position occupied check
                    first_row.pop(position-1)
                    first_row.insert(position-1,symbol)
                    print_board()
                    check_win(player)
                else:
                    print 'Please select a different position, overwrite is not possible'
                    play(player)
            else:
                print 'First row is full, please select a number except 1 , 2 and 3'
                play(player)
        elif (position == 4 or position == 5 or position == 6):
            if(second_row[0] == 'NA' or second_row[1] == 'NA' or second_row[2] == 'NA'): #list full check
                if(second_row[position-4] == 'NA'): #position occupied check
                    second_row.pop(position-4)
                    second_row.insert(position-4,symbol)
                    print_board()
                    check_win(player)
                else:
                    print 'Please select a different position, overwrite is not possible'
                    play(player)
            else:
                print 'Second row is full, please select a number except 4 , 5 and 6'
                play(player)
        else:
            if(third_row[0] == 'NA' or third_row[1] == 'NA' or third_row[2] == 'NA'): #list full check
                if(third_row[position-7] == 'NA'): #position occupied check
                    third_row.pop(position-7)
                    third_row.insert(position-7,symbol)
                    print_board()
                    check_win(player)
                else:
                    print 'Please select a different position, overwrite is not possible'
                    play(player)
            else:
                print 'Third row is full, please select a number except 7 , 8 and 9'
                play(player)
        
    else:
        print 'The user input is not valid, Please try again'
        play(player)
        
def play(player):
    if(player == 1):
        global flag_p1
        print "It is player 1 turn"
        flag_p1 = 1
        p1_input = raw_input("Enter a number between 1 to 9 : ")
        insert_to_board(player,p1_input,'X')
    else:
        print "It is player 2 turn"
        p2_input = raw_input("Enter a number between 1 to 9 : ")
        insert_to_board(player,p2_input,'O')

def game_play():
    print "The game has begun"
    
    player = randint(0,2)
    if(player == 1):
        play(1)
    else:
        play(2)
    
    
def instructions():
    title = " Tic Tac Toe "
    print title.center(60,'*')
    print 'Step 1: The computer will randomly pick the player to play first'
    print "Step 2: First player will play with the symbol 'X'"
    print "Step 3: Second player will play with the symbol 'O'"
    print "Use the number pad to choose the box in which the player wants to enter their symbol"
    print "The play area appears as follows"
    print "\n"
    print "(1) | (2) | (3)"
    print "----------------"
    print "(4) | (5) | (6)"
    print "----------------"
    print "(7) | (8) | (9)"
    print "\n"
    input = raw_input("Enter 'Y' to continue or 'N' to quit:")
    
    if(input == 'Y' or input == 'y' ):
        game_play()
    elif(input == 'N' or input == 'n'):
        exit()
    else:
        print 'unknown input, game restart!'
        instructions()
    
instructions()