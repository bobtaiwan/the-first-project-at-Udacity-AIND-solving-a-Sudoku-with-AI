assignments = []

# ----------------------------------utility---------------------------------------
rows = 'ABCDEFGHI'
cols = '123456789'
diagonal_1= ['A1','B2','C3','D4','E5','F6','G7','H8','I9']
diagonal_2= ['A9','B8','C7','D6','E5','F4','G3','H2','I1']
def cross(A, B):
	return [s+t for s in A for t in B]
   
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units=[diagonal_1,diagonal_2]

unitlist = row_units + column_units + square_units+diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

empty_grid = '.................................................................................'

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, 
            then the value will be '123456789'.
    """
    values=[]    
    allPosibleDigits='123456789'

    for c in grid:
        if c=='.':
            values.append(allPosibleDigits)
        else:
            values.append(c)
    assert len(values)==81, "Input grid must be a string of length 81 (9x9)"

    return dict(zip(boxes,values))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
    
def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

# --------------------------------utility--------------------------------------

# --------------------------------algorithm------------------------------------
"""Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
def naked_twins(values): 
    dictValues=grid_values(empty_grid)	
    for solved_box in values:
        dictValues[solved_box]=values[solved_box]
    
    
    for unit in unitlist:
        for compareBox_1 in unit:
            compareDigit=dictValues[compareBox_1]
            if len(compareDigit)==2:
                sameDigitCnt=0
                for compareBox_2 in unit:
                    if compareDigit==dictValues[compareBox_2]:
                        sameDigitCnt+=1
                         #if sameDigitCnt==2 
                         #it means this unit's naked_twins condition is Ture
                        if sameDigitCnt==2:
                             #check all the box's value of unit 
                            for box in unit:
                                #if the len of box's value>2 
                                #it means maybe can eliminate the possible values of box       
                                if len(dictValues[box])>2:                      
                                    value=dictValues[box].replace(compareDigit[0],'')
                                    value=value.replace(compareDigit[1],'')
                                    assign_value(dictValues,box,value)
            
              
                    
    return dictValues
  
    
	
def eliminate(values):
    solved_boxes = [box for box in values.keys() if len(values[box]) == 1]
    for solved_box in solved_boxes:
        digit = values[solved_box]
        for peer in peers[solved_box]:
            #values[peer] = values[peer].replace(digit,'')
            values=assign_value(values,peer,values[peer].replace(digit,''))
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            digitPlaces = [box for box in unit if digit in values[box]]
            if len(digitPlaces) == 1:
                onlyChoiceBox=digitPlaces[0]
                #values[onlyChoiceBox] = digit
                values=assign_value(values,onlyChoiceBox,digit)
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
       
        values=eliminate(values)
        
        values=only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

# --------------------------------algorithm------------------------------------------			

"""
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4.
            ...8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no 
        solution exists.
    """
def solve(grid):
    dictValues=grid_values(grid)
    dictValues=search(dictValues)
    return dictValues
    
	
	
	

if __name__ == '__main__':
   
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
   
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
