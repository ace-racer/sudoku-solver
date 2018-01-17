from utils import *
import copy
import sys

def solve(grid):
    """
    Solving the sudoku using function in utils.py
    Input: The sudoku in string format of 81 characters
    Output: None
    """
    #converting '.' to possible answers. Values is a dictionary that contains box as key
    #and its possible answers as its value.
    values = grid_values(grid)

    #solving the sudoku
    values = search(values)

    #displaying the answer
    display(values)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Expect the SUDOKU file name as the first input. Please mark empty places with a \'.\'")
    else:
        print("Reading from the file to solve the SUDOKU puzzle")
        try:
            with open(sys.argv[1], 'r') as file:
                grid = file.read()
                solve(grid)
        except Exception as e:
            print("An error occurred while processing the SUDOKU puzzle: " + str(e))
