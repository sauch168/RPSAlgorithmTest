# Data extraction here: extract the data from the txt file to python input
# your input can be of any format, one suggestion is using integers 0,1,2 for rock paper scissor

import csv
import random

def pullFromFile(filename):
    file = open(filename)
    reader = csv.reader(file)
    _ = next(reader)
    computer_history = ""
    me_history = ""
    for row in reader:
        me_history += row[0]
        computer_history += row[1]
        #in each row, first entry is my choice, second entry is computer's choice
    cutoff = computer_history.find("Win") - len(computer_history)
    computer_history = computer_history[:cutoff]
    cutoff = me_history.find("Draw") - len(me_history)
    me_history = me_history[:cutoff]
    return (me_history, computer_history)

def winning_response(move):
    return (move + 1) % 3

def losing_response(move):
    return (move + 2) % 3

def highest_count(counts):
    max = 0
    max_index = -1
    for x in range(0, 3):
        if (counts[x] > max):
            max = counts[x]
            max_index = x
    return max_index

def probableNextMove(me_history, computer_history, recent_length, history_length):
    begin_index = 0
    recent_history = me_history[history_length - recent_length:]
    count = [0, 0, 0]
    weighted_add = 1
    bound = 10
    start_bound = 0
    while (begin_index <= history_length - recent_length):
        if (start_bound >= bound):
            weighted_add += 0.2
            start_bound = 0
        substring_index = me_history.find(recent_history, begin_index)
        #history_snippet = computer_history[substring_index:substring_index + recent_length]
        if (substring_index + recent_length < history_length):
            count[(int)(computer_history[substring_index + recent_length:substring_index + recent_length + 1])] += weighted_add
        begin_index = substring_index + 1
        start_bound += 1
    return highest_count(count)

#Define your algorithm here or define your own functions and procedure
def rock_paper_scissor(history=None):
    history = pullFromFile("Rock Paper Scissors Formatted.txt")
    me_history = history[0]
    computer_history = history[1]
    
    #0 for rock,  1 for paper, 2 for scissors
    #in each row, first entry is my choice, second entry is computer's choice

    maxSameStreak = 3

    recent_history_length = 6
    sameStreak = 0
    response = ""
    starting = ["Rock", "Paper", "Scissors"]
    moveIndex = random.randint(0, 2)
    yourMove = starting[moveIndex]
    while (response != "exit"):
        print("Use: " + yourMove)
        response = input("Enter the computer's response (\"R\", \"P\", \"S\", or \"exit\"): ")
        moveInt = -1
        while (response != "R" and response != "P" and response != "S" and response != "exit"):
            response = input("Enter the computer's response (\"R\", \"P\", \"S\", or \"exit\"): ")
        if response == "R":
            moveInt = 0
        elif response == "P":
            moveInt = 1
        elif response == "S":
            moveInt = 2
        else:
            break
        if (str(moveIndex) == me_history[-1]):
            sameStreak += 1
        else:
            sameStreak = 0
        computer_history = computer_history + (str)(moveInt)
        me_history = me_history + (str)(moveIndex)
        if (sameStreak >= maxSameStreak):
            moveIndex = winning_response(moveInt)
            yourMove = starting[moveIndex]
        else:
            #look at the last 500 moves
            history_length = len(computer_history)
            if (len(me_history) > 500):
                me_history = me_history[1:]
                computer_history = computer_history[1:]
            moveIndex = -1
            decreaseHistory = -1
            while (moveIndex == -1 and decreaseHistory < recent_history_length):
                decreaseHistory += 1
                moveIndex = probableNextMove(me_history, computer_history, recent_history_length - decreaseHistory, history_length)
            moveIndex = winning_response(moveIndex)
            yourMove = starting[moveIndex]


rock_paper_scissor()