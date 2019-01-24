##### STATS404
##### WEEK 2 LAB

import random
import numpy as np


## define theBoard
theBoard = {'top-L': ' ',
          'top-M': ' ',
          'top-R': ' ',
          'mid-L': ' ',
          'mid-M': ' ',
          'mid-R': ' ',
          'low-L': ' ',
          'low-M': ' ',
          'low-R': ' '
         }

## index numbers for the dictionary
index = [0,1,2,3,4,5,6,7,8]

## shuffle index numbers
random.shuffle(index)   # randomly put index into order for placing x's and o's

## populate the board in order of shuffled index
for i in range(9):
    #print(index[i])
    if i % 2 == 0:
        theBoard[list(theBoard)[index[i]]] = 'X'
    else:
        theBoard[list(theBoard)[index[i]]] = 'O'


#print(random.sample(index, k=9))
#print(theBoard)


## initiate X and O's points to keep track
x_pts = 0
o_pts = 0


## put theBoard values into 3X3 numpy array
values = np.array(list(theBoard.values())).reshape(3,3)
#print(values)

## go through different rows and columns to check for wins
for i in range(3):
    combo = values[i,:].copy()
    unique = list(np.unique(combo, return_counts=False))
    #print(unique)
    if len(unique) == 1:
        if unique[0] == 'X':
            x_pts = x_pts + 1
        if unique[0] == ')':
            o_pts = o_pts + 1

## go through two diagonals to check for wins
diag1 = np.diag(values, k=0).copy()
unique1 = list(np.unique(combo, return_counts=False))
if len(unique1) == 1:
    if unique1[0] == 'X':
        x_pts = x_pts + 1
    if unique1[0] == ')':
        o_pts = o_pts + 1

diag2 = np.diag(np.fliplr(values), k=0).copy()
unique2 = list(np.unique(combo, return_counts=False))
if len(unique2) == 1:
    if unique2[0] == 'X':
        x_pts = x_pts + 1
    if unique2[0] == ')':
        o_pts = o_pts + 1


## printing final output
print('Final Output')
print(values)
print('X''s points:' + str(x_pts))
print('O''s points:' + str(o_pts))
if x_pts == o_pts:
    print ('It''s a tie.')
elif x_pts > o_pts:
    print ('X is the winner.')
elif o_pts > x_pts:
    print('O is the winner.')
