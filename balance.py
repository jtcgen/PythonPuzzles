'''
Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure - but there's an
obstacle. The door will only open if a challenge is solved correctly. The future of the zombified rabbit population
is at stake, so Beta reads the challenge: There is a scale with an object on the left-hand side, whose mass is given
in some number of units. Predictably, the task is to balance the two sides. But there is a catch: You only have this
peculiar weight set, having masses 1, 3, 9, 27, ... units. That is, one for each power of 3. Being a brilliant
mathematician, Beta Rabbit quickly discovers that any number of units of mass can be balanced exactly using this set.

To help Beta get into the room, write a method called answer(x), which outputs a list of strings representing where
the weights should be placed, in order for the two sides to be balanced, assuming that weight on the left has mass x units.

The first element of the output list should correspond to the 1-unit weight, the second element to the 3-unit weight,
and so on. Each string is one of: 

"L" : put weight on left-hand side 
"R" : put weight on right-hand side 
"-" : do not use weight 

To ensure that the output is the smallest possible, the last element of the list must not be "-".

x will always be a positive integer, no larger than 1000000000.

Test cases
==========

Inputs:
    (int) x = 2
Output:
    (string list) ["L", "R"]

Inputs:
    (int) x = 8
Output:
    (string list) ["L", "-", "R"]
'''

from math import log, ceil, floor
import sys

def answer(x):
    lgx = log(x,3)

    # All powers of 3
    if 3**floor(lgx) == x:
        return ['-' if i != lgx else 'R' for i in range(int(lgx+1))]

    # range of powers of 3 to look at
    up_bnd = ceil(lgx)
    low_bnd = floor(lgx)
    branch = 3**up_bnd - x

    # If diff between upper bnd and x is greater than x, answer will contain up to lower bnd
    if branch > x:
        ans = ['-'] * (low_bnd+1)
        diff = answer(x-(3**low_bnd))
    else:
        # Answer will contain upper bnd
        ans = ['-'] * (low_bnd+2)
        diff = answer((3**up_bnd)-x)

    # Populate result
    for i in range(low_bnd+1):
        if i < len(diff):
            if branch > x:
                ans[i] = '-' if diff[i] == '-' else 'R' if diff[i] == 'R' else 'L'
            else:
                ans[i] = '-' if diff[i] == '-' else 'L' if diff[i] == 'R' else 'R'
        else:
            ans[i] = '-'
    ans[len(ans)-1] = 'R'

    return ans

if __name__ == '__main__':
    print(answer(sys.argv[1]))
