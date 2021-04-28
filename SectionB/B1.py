# This is based on the idea that 
# if number of 1s is odd, minimum moves will be made when the 1 in the middle stays idle
# if number of 1s is even, either of the two 1s in the middle stay idle (or approach each other) 
# whereas all other '1's approach the 1 in the middle 

import numpy as np

# Input should only contain 1 and 0. Eg: 011001001
text_input = input("Enter 0s and 1s in order without punctuations:")
# Input in text is converted to list of 1s and 0s
list_input = np.array([int(digit) for digit in text_input])

# Returns list of positions of '1's
initial_pos = np.where(list_input == 1)[0]
n1 = len(initial_pos)
# Final position is such that all '1's come around the 1 in the middle
# Eg: if initial_pos = [2,5,7] => final_pos = [4,5,6]
final_pos = np.arange(n1) + (initial_pos[n1 // 2] - n1 // 2)

# Total number of moves is the sum of the moves made by each 1s
# i.e., sum of absolute values of difference of final and initial positions
min_moves = sum(abs(final_pos - initial_pos))

print(min_moves)
