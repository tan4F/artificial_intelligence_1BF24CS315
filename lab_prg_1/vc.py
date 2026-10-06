import random

board = [" "] * 9


def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):
            return True

    return False


def board_full():
    return " " not in board


print("TIC-TAC-TOE")
print("You are X. Computer is O.")

while True:

    display_board()

    while True:
        choice = int(input("Enter position (1-9): "))

        if choice < 1 or choice > 9:
            print("Enter a number between 1 and 9.")
        elif board[choice - 1] != " ":
            print("Position already occupied.")
        else:
            board[choice - 1] = "X"
            break

    if check_winner("X"):
        display_board()
        print("Human wins!")
        break

    if board_full():
        display_board()
        print("Draw!")
        break

    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    computer_position = random.choice(empty_positions)
    board[computer_position] = "O"

    print("Computer chose position:", computer_position + 1)

    if check_winner("O"):
        display_board()
        print("Computer wins!")
        break

    if board_full():
        display_board()
        print("Draw!")
        break

state=[0,1]
n=int(input("Enter the no. of rooms"))
rooms=[]
for i in range(n):
    r=input("Enter room name")
    rooms.append(r)

state={}
for i in range(n):
  ch = int(input("Enter the state of room " + rooms[i] + " (0 -> dirty, 1 -> clean): "))
  state[rooms[i]]=ch

for i in range(n):
  if(state[rooms[i]]==0):
    print("Room",rooms[i],"is being cleaned")
    print("Vacuum cleaner moving to",rooms[(i+1)%n])
    state[rooms[i]]=1
  else:
    print("Room",rooms[i],"is clean")
    print("Vacuum cleaner moving to",rooms[(i+1)%n])36
