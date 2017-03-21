# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *Student should provide answer here*
First step:
Select a unit of unit list,the index of unit is A,
and 0 is initial with A.

Second step:
if there has two squares in the same unit,
and that both have the same two possible digits,
then can eliminate this two possible digits from every other square in the unit.

Third step:
If A is not equal count of unit list ,
then A plus one ,and loop to first step,
otherwise return solution.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: *Student should provide answer here*
First step:
check how many boxes have a determined value.
and get a number A. 

Second step:
use eliminate strategy and only choise strategy to solve problem.

Third step:
check how many boxes have a determined values after use strategy,
and get a number B.
 
Fourth step:
if B is not equal A then loop to first step,
otherwise stop loop and return solution.




### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

