import numpy as np

numbers = [83,5,71,61,88,55,95,6,0,97,20,16,27,7,79,25,81,29,22,52,43,21,53,59,99,18,35,96,51,93,14,77,15,3,57,28,58,17,50,32,74,63,76,84,65,9,62,67,48,12,8,68,31,19,36,85,98,30,91,89,66,80,75,47,4,23,60,70,87,90,13,38,56,34,46,24,41,92,37,49,73,10,94,26,42,40,33,54,86,82,72,39,2,45,78,11,1,44,69,64]

def read_input():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
    
    # Creates a list of matrixes (boards)
    data = [list(filter(None, line.split(" "))) for line in data if len(line) != 0]
    data = [data[n:n+5] for n in range(0, len(data), 5)]
    return data

def update_boards(boards, number, boards_left):
    losing_board = None
    for i in range(len(boards)):
        if i not in boards_left:
            continue

        board = boards[i]
        lines_left = len(board)
        for j in range(len(board)):
            board[j] = [n for n in board[j] if n != str(number)]

            if len(board[j]) == 0:
                if len(boards_left) == 1:
                    losing_board = boards[boards_left[0]]

                boards_left.remove(i)
                break
    
    return losing_board

def main():
    data = read_input()

    boards   = data
    boards_t = [np.array(matrix).T.tolist() for matrix in data]
    boards_left = [i for i in range(len(boards))]
    for number in numbers:
        for set_boards in [boards, boards_t]:
            losing_board = update_boards(set_boards, number, boards_left)
            if losing_board:
                break
        
        if losing_board:
            break

    leftover = 0
    for line in losing_board:
        leftover += sum([int(n) for n in line])

    print(leftover * number)
        
if __name__ == "__main__":
    main()