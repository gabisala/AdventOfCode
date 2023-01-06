"""
--- Day 4: Camp Cleanup ---
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. 
Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. 
To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:

Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. 
Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully 
contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner 
will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

"""

## First puzzle
# Open the input file and read in the lines
with open('AdventOfCode_2022/Day_4/input.txt', 'r') as file:
    lines = file.readlines()

# Create a list of intervals from the input lines
intervals = [line.strip("\n").split(",") for line in lines]

# Clean up the intervals by converting them to lists of integers
clean_intervals = []
for interval in intervals:
    
    # Create a list of cleaned up intervals for the current interval
    temp_intervals = []
    for interval_string in interval:
        
        # Split the interval string into start and end points
        new_interval = interval_string.split("-")
        
        # Convert the start and end points to integers
        new_interval[0], new_interval[1] = int(new_interval[0]), int(new_interval[1])
        
        # Add the cleaned up interval to the list
        temp_intervals.append(new_interval)
        
    # Add the list of cleaned up intervals to the overall list of intervals
    clean_intervals.append(temp_intervals)


# Counter for the number of intervals where one fully contains the other
contains_counter = 0

# Iterate over the intervals
for interval in clean_intervals:
    
    # Get the first and second intervals
    first_interval = interval[0]
    second_interval = interval[1]
    
    # Check if one interval fully contains the other
    if first_interval[0] <= second_interval[0] and first_interval[1] >= second_interval[1] or first_interval[0] >= second_interval[0] and first_interval[1] <= second_interval[1]:
        # One interval fully contains the other, increment the counter and print the intervals
        contains_counter += 1
        
# Print the number of intervals where one fully contains the other
print(contains_counter)


# Counter for the number of intervals that overlap
overlap_counter = 0

# Iterate over the intervals
for interval in clean_intervals:
    
    # Get the first interval
    first_interval = interval[0]
    first_interval_start = first_interval[0]
    first_interval_end = first_interval[1]
    
    # Create a set of values representing the range of the first interval
    first_interval_set = {i for i in range(first_interval_start, first_interval_end + 1)}
    
    # Get the second interval
    second_interval = interval[1]
    second_interval_start = second_interval[0]
    second_interval_end = second_interval[1]
    
    # Create a set of values representing the range of the second interval
    second_interval_set = {i for i in range(second_interval_start, second_interval_end + 1)}
    
    # Calculate the overlap between the two intervals
    overlap = first_interval_set & second_interval_set
    
    # Check if the overlap is not empty
    if len(overlap) > 0:
        
        # The intervals overlap, increment the counter
        overlap_counter += 1
        
# Print the number of intervals that overlap       
print(overlap_counter)
    

