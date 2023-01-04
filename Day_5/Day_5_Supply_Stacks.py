"""
--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded 
from the ships. Supplies are stored in stacks of marked crates, but because 
the needed supplies are buried under many other crates, the crates need to
be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. 
To ensure none of the crates get crushed or fall over, the crane operator 
will rearrange them in a series of carefully-planned steps. After the 
crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate
procedure, but they forgot to ask her which crate will end up where, and 
they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the 
rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two 
crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains 
three crates; from bottom to top, they are crates M, C, and D. Finally, 
stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, 
a quantity of crates is moved from one stack to a different stack. In the 
first step of the above rearrangement procedure, one crate is moved from 
stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
 
In the second step, three crates are moved from stack 1 to stack 3. Crates 
are moved one at a time, so the first crate to be moved (D) ends up below 
the second and third crates:

        [Z]
        [N]--- Day 5: Supply Stacks ---
The expedition can depart as soon as the final supplies have been unloaded 
from the ships. Supplies are stored in stacks of marked crates, but because 
the needed supplies are buried under many other crates, the crates need to
be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. 
To ensure none of the crates get crushed or fall over, the crane operator 
will rearrange them in a series of carefully-planned steps. After the 
crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate
procedure, but they forgot to ask her which crate will end up where, and 
they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the 
rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two 
crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains 
three crates; from bottom to top, they are crates M, C, and D. Finally, 
stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, 
a quantity of crates is moved from one stack to a different stack. In the 
first step of the above rearrangement procedure, one crate is moved from 
stack 2 to stack 1, resulting in this configuration:
rom stack 2 to stack 1. Again, because crates 
are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
 
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
 
The Elves just need to know which crate will end up on top of each stack; 
in this example, the top crates are C in stack 1, M in stack 2, and Z in 
stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?

--- Part Two ---
As you watch the crane operator expertly rearrange the crates, you notice the process
isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. 
The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, 
leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
 
However, the action of moving three crates from stack 1 to stack 3 means that those three 
moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
 
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
 
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C 
that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
 
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know 
where they should stand to be ready to unload the final supplies. After the rearrangement 
procedure completes, what crate ends up on top of each stack?
"""


import string
from collections import deque
import copy

def simulate_in_console(puzzle_state):
    """
    This is a helper function. it prints the visual represetation for puzzle states
    The origina states, before the crates are moved from one stack to another stack
    The first puzzle, final state
    The second puzzle, final state
    """
    
    print("")
    
    # Add padding using the filler pattern
    width = 100
    filler = '.'
    
    # Original state
    if puzzle_state == 'original':
        
        print(f'{"  Original state":{filler}>{width}}\n')
        stacks = crates_stacks

    # After the first puzzle  
    elif puzzle_state == 'first':
        
        print(f'{"  First puzzle":{filler}>{width}}\n')    
        stacks = crates_stacks_first_puzzle

    # After the second puzzle 
    elif puzzle_state == 'second':
        
        print(f'{"  Second puzzle":{filler}>{width}}\n')
        stacks = crates_stacks_second_puzzle

    # Show all staks  
    for dq in stacks:
            print(dq)
            
    # Show top crates
    top_of_each_stack = []
    for dq in stacks:
        top_of_each_stack.append(dq.pop())
        
    top_crates = ''.join(top_of_each_stack)
    print(f'\nThe crates at the top of each stack are: {top_crates}')
    

# Read the input file and store the lines in a list
with open('AdventOfCode/Day_5/input.txt', 'r') as file:
    lines = file.readlines()
    
# Strip the newline characters from the lines
raw_data = [line.strip("\n") for line in lines]


# Store the lines that contain the initial state of the crates and the moves in separate lists 
crates_stack_raw = []
crane_moves_raw = []

# Find the lines that start with "move" and add tham to the crane moves list. 
# Esle add them to crates stack list
for line in raw_data:
    
    if line.startswith('move'):
        crane_moves_raw.append(line)
    else:
        crates_stack_raw.append(line)
       
# Remove the last element of the crates stack list, which is an empty line
crates_stack_raw = crates_stack_raw[:-1]

# Separate the crates into different lists based on their position in the stacks
crates_stack_str_to_list = []
crates_stack_numbers = [[] for lst in range(39)] # 39 is the maximum number of characters in a line

for line in crates_stack_raw:

    temp_list = []
    for i, char in enumerate(line):
        crates_stack_numbers[i].append(char)
        

# Try and find the list containing numbers, those are the list that have the stack represetation
crates_stack_almost_clean = []

for lst in crates_stack_numbers:
    
    try:
        # If the last element of the list is a number, it means it is a crates list and we should 
        # be included in the almost clean list
        num = int(lst[-1])
        crates_stack_almost_clean.append(lst[:-1])
    except:
        pass

# Reverse the order of the crates in each list, becouse we will transfor it in a deque soon 
# and we want to keep the order, buttom to top.
crates_stacks_reversed = []
uppercase_chars = list(string.ascii_uppercase) # Create a list of uppercase characters to identify the crates

for lst in crates_stack_almost_clean:
    temp_lst = []
    for char in lst:
        if char in uppercase_chars:
            temp_lst.append(char)
    crates_stacks_reversed.append(temp_lst)

# Convert the lists of crates into deques (double-ended queues)
crates_stacks = [deque(reversed(lst))for lst in crates_stacks_reversed]

# Print the original state of the crates
simulate_in_console('original')

# Convert the moves strings into lists of integers and representing the creane operations
crane_moves = []
for mv in crane_moves_raw:
    
    temp_lst = []
    for string in mv.split(' '):
        try:
            num = int(string)
            temp_lst.append(num)
        except:
            pass
    crane_moves.append(temp_lst)
 
 
## First puzzle
# Create a copy of the crates stacks for the first puzzle
crates_stacks_first_puzzle = copy.deepcopy(crates_stacks)

# Perform the moves on the crates for the first puzzle
# The rearrangement procedure is given. In each step of the procedure, 
# a quantity of crates is moved from one stack to a different stack.
for moves in crane_moves:
  
    number_of_crates, from_stack, to_stack = moves
    take_from_stack = crates_stacks_first_puzzle[from_stack - 1]
    put_to_stack = crates_stacks_first_puzzle[to_stack - 1]

    # Remove a crate from the source stack and append it to the destination stack
    for crate in range(number_of_crates):
        try:
            put_to_stack.append(take_from_stack.pop())

        # If the source stack is empty, do nothing
        except IndexError:
            pass
        
# Print the final state of the crates for the first puzzle 
simulate_in_console('first')         


## Second puzzle
# Create a copy of the crates stacks for the second puzzle
crates_stacks_second_puzzle = copy.deepcopy(crates_stacks)

# Perform the moves on the crates for the second puzzle
# The rearrangement procedure is given. In each step of the procedure, 
# a quantity of crates is moved from one stack to a different stack.
for moves in crane_moves:

    number_of_crates, from_stack, to_stack = moves
    take_from_stack = crates_stacks_second_puzzle[from_stack - 1]
    put_to_stack = crates_stacks_second_puzzle[to_stack - 1]
    
    # Create a temporary deque 
    temp_stack = deque()

    # Move the required number of crates to a temporary stack
    for crate in range(number_of_crates):
        
        try:
            element = take_from_stack.pop()
            temp_stack.append(element)

        except IndexError:
            pass
    # Reverse the temporary stack so that the moved crates stay in the same order
    # as they had in the take from stack (previous state)
    reverse_stack = deque(reversed(temp_stack))
    
    # Move the crates to the new stack (new state)
    put_to_stack.extend(reverse_stack)

# Print the final state of the crates for the second puzzle 
simulate_in_console('second')









