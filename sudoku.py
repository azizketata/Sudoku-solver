from pprint import pprint
def print_grid(puzzle):
    j=0
    for row in [puzzle[i:(i+1)][0] for i in range(9)]:
        input = [str(i) for i in row]
        print('| '+ ' | '.join(input) + ' |')

    print()
def find_next_empty(puzzle):
    # finds the next row, col on puzzle that's not filled yet --> we represent these with -1
    # returns a row, col tuple (or (None, None) if there is none)
    for row in range(9):
        for column in range(9):
            if puzzle[row][column] == -1:
                return (row,column)
    return (None,None)
    pass

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    #check whether the number is in the row
    for j in range(9):
        # if it is the same row and column we don't check
        if puzzle[row][j] == guess:
            return False

    #check whether the number is in the column
    for i in range(9):
        if puzzle[i][col]==guess:
            return False
    # two coordinates that will represent where is the cell compared to the 3*3 square
    x = (row//3)*3
    y = (col//3)*3
    for i in range(3):
        for j in range(3):
            if puzzle[x+i][y+j] == guess:
                return False
    return True




def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    # if we are at the end and there are no more unknown Cases then return True (solved sudoku board)
    if row is None or col is None:
        return True


    for guess in range(1, 10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle): # if the children of this function return true then itself can return true
                return True
        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1 # if the guess is not valid then we put it back to -1
    return False

if __name__ == '__main__':
    input2= [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(input2))
    pprint(input2)
input=\
[[3, -1, 6, 5, -1, 8, 4, -1, -1],
[5, 2, -1, -1, -1, -1, -1, -1, -1],
[-1, 8, 7, -1, -1, -1, -1, 3, 1],
[-1, -1, 3, -1, 1, -1, -1, 8, -1],
[9, -1, -1, 8, 6, 3, -1, -1, 5],
[-1, 5, -1, -1, 9, -1, 6, -1, -1],
[1, 3, -1, -1, -1, -1, 2, 5, -1],
[-1, -1, -1, -1, -1, -1, -1, 7, 4],
[-1, -1, 5, 2, -1, 6, 3, -1, -1] ]

print(solve_sudoku(input))
print_grid(input)
