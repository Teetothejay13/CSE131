# 1. Name:
#      TJ Putnam
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This assignment is meant to be a draft of the sudoku program. For the draft, I
#      will only display the board and save changes, I will not check the validity of
#      the move.
# 4. What was the hardest part? Be as specific as possible.
#      
# 5. How long did it take for you to complete the assignment?
#      

# We'll need this library for the board files
import json
# And this one to quit if we can't find the file
import sys
from turtle import isvisible

# First, we need a main to run the show
def main():
    # First we will get the board from getBoard()
    board = getBoard()
    # After we have the board, we will need to have a game loop
    keepPlaying = True
    while keepPlaying:
        # We'll always want to display the board first. Display will then call functions to ask for the user move and to check
        # The validity of the move, and once the move is determined to be valid, we'll recieve it back so that6 we can save it
        userMove = display(board)
        # After we get the move back, we have to edit the board, then pass it into saveBoard() to save it to the file.
        # If the user move is "quit" however, we will exit the loop after saving
        if userMove == "quit":
            saveBoard(board)
            keepPlaying = False
        else:
            # Now we need to change the board based on the user move, which comes back as a string and a number
            # We'll split the coordinate into the column and row
            coordinate = list(userMove[0])
            # And then, we need to convert it to numbers. The row is easy
            row = int(coordinate[1]) - 1
            # But the column needs some extra logic
            if coordinate[0] == "A":
                column = 0
            elif coordinate[0] == "B":
                column = 1
            elif coordinate[0] == "C":
                column = 2
            elif coordinate[0] == "D":
                column = 3
            elif coordinate[0] == "E":
                column = 4
            elif coordinate[0] == "F":
                column = 5
            elif coordinate[0] == "G":
                column = 6
            elif coordinate[0] == "H":
                column = 7
            elif coordinate[0] == "I":
                column = 8
            # We can't forget the number
            number = userMove[1]
            # Now that we have that sorted out, we can edit the board
            board[row][column] = number
    # If we're done playing, we display a message and are done
    print("Thank you for playing!")

# Let's get the board first
def getBoard():
    # First we need to have an input loop until we get a workable file
    validFile = False
    while not validFile:
        fileName = getFileName()
        # Now we call the readFile function. if it reads sucessfully, we'll get the board returned.
        # if it was unsucessful, we'll get False returned
        board = readFile(fileName)
        # After we get the result, we either return the board to main or ask for a different file
        if board == False:
            # If the file couldn't be found or read, we ask them to try again or to quit.
            wantToQuit = input("Unfortunately, your file could not be found. To try again, type 'try again'.\nAlternatively, if you would like to quit, type 'quit':")
            if wantToQuit == "quit":
                sys.exit()
        # If everything worked, we return the board
        else:
            return board

# We need to get the file name where the board is
def getFileName():
    # This is pretty simple, we just get the file name as a string
    fileName = input("Please enter the name of the file you'd like to access: ")
    return fileName

# Then we need to read the file
def readFile(fileName):
    # For this, we need a try except, where we try to read it, except for errors, where we will return False
    try:
        with open(fileName, "r") as json_file:
            content = json.load(json_file)
            board = content["board"]
            return board
    except IOError:
        return False

# We also need to save changes to the board
def saveBoard(board):
    # We will need a while loop going until we succesfully save
    saved = False
    while not saved:
        # Here we will ask what file they would like to save to, and then we will try to save
        fileName = getFileName()
        try:
            with open(fileName, "w") as json_file:
                content = {
                    "board": board
                }
                json.dump(content, json_file)
                print(f"Board saved to {fileName}.")
                json_file.close()
                saved = True
        except IOError:
            print("Failed to save. Please check the file name or choose a different file.")

# Obviously we need to display the board
def display(board):
    # Now we have to display the board, but that will take some complicated logic
    print("   A B C D E F G H I")
    # We need to make sure that the 0's turn into spaces, so we have to go through every element and change it
    # We have to cycle through each row
    for row in board:
        # And each number in each row
        for column in row:
            # If it is 0, we change it to " "
            if column == 0:
                column = " "
    # Now we should be able to display the edited board
    print(f"1  {board[0][0]} {board[0][1]} {board[0][2]}|{board[0][3]} {board[0][4]} {board[0][5]}|{board[0][6]} {board[0][7]} {board[0][8]}")
    print(f"2  {board[1][0]} {board[1][1]} {board[1][2]}|{board[1][3]} {board[1][4]} {board[1][5]}|{board[1][6]} {board[1][7]} {board[1][8]}")
    print(f"3  {board[2][0]} {board[2][1]} {board[2][2]}|{board[2][3]} {board[2][4]} {board[2][5]}|{board[2][6]} {board[2][7]} {board[2][8]}")
    print("   -----+----+-----")
    print(f"4  {board[3][0]} {board[3][1]} {board[3][2]}|{board[3][3]} {board[3][4]} {board[3][5]}|{board[3][6]} {board[3][7]} {board[3][8]}")
    print(f"5  {board[4][0]} {board[4][1]} {board[4][2]}|{board[4][3]} {board[4][4]} {board[4][5]}|{board[4][6]} {board[4][7]} {board[4][8]}")
    print(f"6  {board[5][0]} {board[5][1]} {board[5][2]}|{board[5][3]} {board[5][4]} {board[5][5]}|{board[5][6]} {board[5][7]} {board[5][8]}")
    print("   -----+----+-----")
    print(f"7  {board[6][0]} {board[6][1]} {board[6][2]}|{board[6][3]} {board[6][4]} {board[6][5]}|{board[6][6]} {board[6][7]} {board[6][8]}")
    print(f"8  {board[7][0]} {board[7][1]} {board[7][2]}|{board[7][3]} {board[7][4]} {board[7][5]}|{board[7][6]} {board[7][7]} {board[7][8]}")
    print(f"9  {board[8][0]} {board[8][1]} {board[8][2]}|{board[8][3]} {board[8][4]} {board[8][5]}|{board[8][6]} {board[8][7]} {board[8][8]}")
    # Now we can ask what the user wants to do, in a loop of course until it's comfirmed a valid move
    isValidMove = False
    while not isValidMove:
        userMove = getUserMove()
        # If the user wants to quit, we'll just exit the loop and return the "quit" move
        if userMove == "quit":
            isValidMove = True
        # Otherwise, we'll want to check that the user can do that
        else:
            isValidMove = checkValidMove(userMove)
    # If the move is valid or "quit", then the loop will end and the move will be passed back to main
    return userMove

# We also need to get the move the user wants
def getUserMove():
    # First we ask the coordinate of the move
    coordinate = input("Please specify a coordinate to edit (for example, 'A3'), or type 'quit' to save and quit: ")
    # If they want to quit, then we can stop before asking anything else
    if coordinate == "quit":
        return coordinate
    # If not, we can ask what number they want in that spot
    number = int(input(f"Please enter the integer from 1-9 you would like to go in {coordinate}: "))
    # Now we can return what we got
    userMove = (coordinate, number)
    return userMove

# We also will need to check the validity of the move
def checkValidMove(userMove):
    # For now, we will only return true. We will add the validity logic in the next draft
    isValidMove = True
    return isValidMove


# we need this to run the program automatically
if __name__ == "__main__":
  main()