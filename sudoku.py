# 1. Name:
#      TJ Putnam
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      This assignment is meant to be a sudoku program. It will open a sudoku board from a json file and display it,
#      and then ask the user for their move. The program will then check the validity of the move, asking the user
#      to try again if it is invalid in any way. If the column, row, and number are all valid, and the number can go
#      in the chosen slot, then the program will be able to make the change and save it to the board file.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was arguably the checkValidMove() function. There were so many nested if/else statements to
#      manage, and when I wasn't careful, I often got them confused with each other. In the end, I separated them with
#      some blank space, then deleted the blank space when I was done with them.
# 5. How long did it take for you to complete the assignment?
#      Including the time spent on the rough draft, I spent about 9 hours total on this assignment.

# We'll need this library for the board files
import json
# And this one to quit if we can't find the file
import sys
from turtle import isvisible
from webbrowser import get

# First, we need a main to run the show
def main():
    # First we will get the board from getBoard()
    board = getBoard()
    # After we have the board, we will need to have a game loop
    keepPlaying = True
    while keepPlaying:
        # We'll always want to display the board first. Display will then call functions to ask for the user move and to check
        # The validity of the move, and once the move is determined to be valid, we'll recieve it back so that we can save it
        userMove = display(board)
        # After we get the move back, we have to edit the board, then pass it into saveBoard() to save it to the file.
        # If the user move is "quit" however, we will exit the loop after saving
        if userMove == "quit":
            saveBoard(board)
            keepPlaying = False
        # If the user move is "check", then we can call getUserMove() directly and then pass the move into
        # checkValues()
        elif userMove == "check":
            # This part is not implemented, I had many struggles to implement the check function so I left it out for now.
            pass
            #print("Checking now, please re-enter the coordinate you would like to check.")
            #userMove = getUserMove(board)
            #column = userMove[0]
            #row = userMove[1]
            #possibleValues = checkValues(column, row, board)
            #print(f"The possible values for the selected coordinate are: {possibleValues}")
        else:
            # Now we need to change the board based on the user move
            column = userMove[0]
            row = userMove[1]
            number = userMove[2]
            print(column)
            print(row)
            print(number)
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
            # We want to replace the 0's with empty spaces, so we'll loop through each spot in each row and do that
            currentRow = 0
            currentColumn = 0
            for row in board:
                # Nested loops are bad, I know, but this will only run 81 times, max. 9 rows by 9 columns isn't bad
                for space in row:
                    if space == 0:
                        board[currentRow][currentColumn] = " "
                    # When we're done replacing, we move to the next column
                    currentColumn += 1
                # When we're done with all the columns in that row, we reset the current column and move onto the next row
                currentColumn = 0
                currentRow += 1
            # Once all the replacing is done, we return the board
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
                # Now we need to switch out all the spaces for 0's again, so we need the same loop as in readFile(), but in reverse
                currentRow = 0
                currentColumn = 0
                for row in board:
                    # Nested loops are bad, I know, but this will only run 81 times, max. 9 rows by 9 columns isn't bad
                    for space in row:
                        if space == " ":
                            board[currentRow][currentColumn] = 0
                            # When we're done replacing, we move to the next column
                        currentColumn += 1
                    # When we're done with all the columns in that row, we reset the current column and move onto the next row
                    currentColumn = 0
                    currentRow += 1
                # Once our board has it's 0's again, we set the board to the content and save it
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
    print("   -----+-----+-----")
    print(f"4  {board[3][0]} {board[3][1]} {board[3][2]}|{board[3][3]} {board[3][4]} {board[3][5]}|{board[3][6]} {board[3][7]} {board[3][8]}")
    print(f"5  {board[4][0]} {board[4][1]} {board[4][2]}|{board[4][3]} {board[4][4]} {board[4][5]}|{board[4][6]} {board[4][7]} {board[4][8]}")
    print(f"6  {board[5][0]} {board[5][1]} {board[5][2]}|{board[5][3]} {board[5][4]} {board[5][5]}|{board[5][6]} {board[5][7]} {board[5][8]}")
    print("   -----+-----+-----")
    print(f"7  {board[6][0]} {board[6][1]} {board[6][2]}|{board[6][3]} {board[6][4]} {board[6][5]}|{board[6][6]} {board[6][7]} {board[6][8]}")
    print(f"8  {board[7][0]} {board[7][1]} {board[7][2]}|{board[7][3]} {board[7][4]} {board[7][5]}|{board[7][6]} {board[7][7]} {board[7][8]}")
    print(f"9  {board[8][0]} {board[8][1]} {board[8][2]}|{board[8][3]} {board[8][4]} {board[8][5]}|{board[8][6]} {board[8][7]} {board[8][8]}")
    # Now we can ask what the user wants to do, and getUserMove will call the function to check if it's valid, and only return
    # a move if the move is either "quit", "check", or a valid move.
    userMove = getUserMove(board)
    # We then send it back to main to either quit or make the change to the board
    return userMove

# We also need to get the move the user wants
def getUserMove(board):
    # First we ask the coordinate of the move, but we want to loop until the move is approved by checkValidMove()
    isValid = False
    while not isValid:
        desiredCoordinate = input("Please specify a coordinate to edit (ie: 'A1'), or type 'quit' to save and quit: ")
        # If they want to quit, then we can stop before asking anything else
        if desiredCoordinate == "quit":
            return desiredCoordinate
        else:
            # We can ask what they want in the spot
            number = int(input(f"Please enter the integer from 1-9 you would like to go in {desiredCoordinate}: "))
            # First we'll check if it's valid by splitting the coordinate into the column and row and passing them into checkValidMove()
            coordinate = list(desiredCoordinate)
            validMove = checkValidMove(coordinate, number, board)
            # If the move isn't valid, we ask to try again and loop back around
            if not validMove:
                print("Please try again.")
            # If it is valid, we can convert the move into numbers and return it
            else:
                row = validMove[1]
                column = validMove[2]
                # Now we can return what we got
                userMove = (column, row, number)
                return userMove

# We also will need to check the validity of the move
def checkValidMove(coordinate, number, board):
    # We initiate each of the valid variables as false, and row and column as none
    isValidColumn = False
    isValidRow = False
    isValidNumber = False
    isValidMove = False
    moveRow = 0
    moveColumn = 0
    # Then we can check if the column is valid first by checking it against a list of possible columns
    validColumns = ["A","B","C","D","E","F","G","H","I"]
    # We can also convert the column into a number while we're at it
    i = 0
    for column in validColumns:
        # We can check either coordinate position for the column
        if str(coordinate[0]).upper() == column or str(coordinate[1]).upper() == column:
            isValidColumn = True
            moveColumn = i
        # If it didn't match, we increase our column counter and check the next one
        i += 1
    # If after going through the columns it still doesn't match a valid column, then we say as much and stop the checking process here
    if not isValidColumn:
        print("Not a valid column, please select a column from 'A' to 'I'.")
        # isValidMove is still false at this point, so we can return it and getUserMove can ask again for a move
        return isValidMove
    # If the column is valid, we can move onto the row
    validRows = [1,2,3,4,5,6,7,8,9]
    # We can also convert the row into a number we can work with (just subtracting one from the number that matches)
    for row in validRows:
        if str(coordinate[0]).isdigit():
            if int(coordinate[0]) == row:
                # If it matches, the row is valid and the board index we can use will be row - 1
                isValidRow = True
                moveRow = int(coordinate[0]) - 1
        elif str(coordinate[1]).isdigit():
            if int(coordinate[1]) == row:
                # Same down here, we can set the row correctly
                isValidRow = True
                moveRow = int(coordinate[1]) - 1
    # If the row still isn't valid, we return isValidMove as false and ask again
    if not isValidRow:
        print("Not a valid row, please select a row from 1 to 9.")
        return isValidMove
    # If we're still checking at this point, then we have a valid row and column, and now we need to check the number
    # First we can eliminate any moves that aren't between 1 and 9
    if number < 1 or number > 9:
        print("Invalid move, desired number must be between 1 and 9.")
        return isValidMove
    # Next we can check if the number is already there
    elif number == board[moveRow][moveColumn]:
        print("Invalid move, that number is already in that coordinate.")
        return isValidMove
    # Next we can check if the spot is filled in general
    elif board[moveRow][moveColumn] != " ":
        print("Invalid move, that coordinate is already filled.")
        return isValidMove
    # Now comes the hard part, checking if it's in the row and column
    else:
        # First let's check the row
        for space in board[moveRow]:
            if number == space:
                # If it matches a number already in the row, it's not a valid move
                print("Invalid move, that number already exists in this row.")
                return isValidMove
        # If we go through the whole row and the number doesn't match any, we can move onto the column, which is harder
        for boardRow in board:
            if number == boardRow[moveColumn]:
                # If it matches a number in the column, it's not a valid move
                print("Invalid move, that number already exists in this column.")
                return isValidMove
        # If we go through all the numbers in the column and none match, then we can say it is a valid number
        isValidNumber = True
    # Now that we've checked the validity of the column, row, and number, we can finally say it's a valid move
    if isValidColumn and isValidRow and isValidNumber:
        # We also want to return the row and column, since we calculated those out anyways
        return (isValidMove, moveRow, moveColumn)

# This function will check the possible values that can go into the coordinate
#
#         NOT IMPLEMENTED YET
#
# This code is only here as a reference for my future progress on it
def checkValues(column, row, board):
    # First we need to initiate empty lists where we'll put the possible values
    possibleRowValues = []
    inRow = False
    possibleValues = []
    # Next we want to check the row for possible values
    for number in range(1, 10):
        # I know, ew, nested loops, but calm down. This will check each spot for a number, with a max of 9 spots and 9 numbers
        # It's small range will not have a significant impact on effeciency.
        for value in board[row]:
            if value == number:
                inRow = True
        # Once we've gone through the spots in the row, we can add the number to our possible row values
        possibleRowValues.append(number)
        # We gotta set inRow to false again for the next number
        inRow = False


# we need this to run the program automatically
if __name__ == "__main__":
  main()