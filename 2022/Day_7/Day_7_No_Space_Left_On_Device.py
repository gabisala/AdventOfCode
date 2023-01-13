"""
--- Day 7: No Space Left On Device ---
You can hear birds chirping and raindrops hitting leaves as the expedition 
proceeds. Occasionally, you can even hear much louder sounds in the 
distance; how big do the animals get out here, anyway?

The device the Elves gave you has problems with more than just its 
communication system. You try to run a system update:

$ system-update --please --pretty-please-with-sugar-on-top
Error: No space left on device
Perhaps you can delete some files to make space for the update?

You browse around the filesystem to assess the situation and save the 
resulting terminal output (your puzzle input). For example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

1182909

The filesystem consists of a tree of files (plain data) and directories 
(which can contain other directories or files). The outermost directory is 
called /. You can navigate around the filesystem, moving into or out of 
directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you 
executed, very much like some modern computers:

    - cd means change directory. This changes which directory is the current 
      directory, but the specific result depends on the argument:
        - cd x moves in one level: it looks in the current directory for the 
        directory named x and makes it the current directory.
        - cd .. moves out one level: it finds the directory that contains the 
        current directory, then makes that directory the current directory.
        - cd / switches the current directory to the outermost directory, /.
    - ls means list. It prints out all of the files and directories immediately 
      contained by the current directory:
        - 123 abc means that the current directory contains a file named abc 
        with size 123.
        - dir xyz means that the current directory contains a directory 
        named xyz.
        
Given the commands and output in the example above, you can determine that the 
filesystem looks visually like this:

- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296)
    
Here, there are four directories: / (the outermost directory), a and d 
(which are in /), and e (which is in a). These directories also contain 
files of various sizes.

Since the disk is full, your first step should probably be to find 
directories that are good candidates for deletion. To do this, you need 
to determine the total size of each directory. The total size of a directory 
is the sum of the sizes of the files it contains, directly or indirectly. 
(Directories themselves do not count as having any intrinsic size.)

The total sizes of the directories above can be found as follows:

    - The total size of directory e is 584 because it contains a single file 
      i of size 584 and no other directories.
    - The directory a has total size 94853 because it contains files f (size 
      29116), g (size 2557), and h.lst (size 62596), plus file i indirectly 
      (a contains e which contains i).
    - Directory d has total size 24933642.
    - As the outermost directory, / contains every file. Its total size is 
      48381165, the sum of the size of every file.
      
To begin, find all of the directories with a total size of at most 100000, 
then calculate the sum of their total sizes. In the example above, these 
directories are a and e; the sum of their total sizes is 95437 (94853 + 
584). (As in this example, this process can count files more than once!)

Find all of the directories with a total size of at most 100000. What is 
the sum of the total sizes of those directories?

"""
from collections import deque
from collections import defaultdict
from collections import OrderedDict

with open('AdventOfCode/2022/Day_7/input.txt', 'r') as file:
    lines = file.readlines()
    
raw_data = [line.strip("\n") for line in lines]
folders = []
current_path = deque()
current_dir = None
file_system = OrderedDict()
paths_subdirs = []
sub_dir_size = defaultdict(lambda: 0)


for line in raw_data:
    
    parse_line = line.split(" ")
    
    if line.startswith("$ cd"):
        
        prompt, command, folder = parse_line
            
        if folder == '..':
            current_path.pop()
            
        else:
            current_path.append(folder)

        
    elif line.startswith("$ ls"):

        current_dir = current_path[-1]
        
        if current_dir in file_system.keys():
            print(f'{current_dir} aleready in.')
        else:
            print(f'Added {current_dir}')
            file_system[current_dir] = {'Sub_directories': [], 'Files': [], 'Files_Size': 0, 'Sub_dirs_Size': 0, 'Total_Size': 0}
        # file_system[current_dir] = {'Sub_directories': [], 'Files': [], 'Files_Size': 0, 'Sub_dirs_Size':0, 'Total_Size': 0}

    else:
        
        if parse_line[0] == 'dir':
            file_system[current_dir]['Sub_directories'].append(parse_line[1])
        else:

            file_size = int(parse_line[0])
            file_name = parse_line[1]
            file_system[current_dir]['Files'].append((file_name, file_size))
            file_system[current_dir]['Files_Size'] += file_size
            
print(len(file_system.keys()))           
for key, value in file_system.items():
    print(key, value)


for key, value in file_system.items():
    print(key)
    for sub_dir in file_system[key]['Sub_directories']:
        print(f'    + {sub_dir}')
    
    for file in file_system[key]['Files']:
        print(f'    - {file[0]} - {file[1]}')


sub_dir_size = defaultdict(int) 
       
def calculate_directories_size(key, file_system, sub_dir_size):
     
    if file_system[key]['Sub_directories'] == []:
        # print(key, value)
        
        file_system[key]['Total_Size'] = file_system[key]['Files_Size']
        sub_dir_size[key] = file_system[key]['Total_Size']
        return sub_dir_size[key]
    
    else:
        # print(key, value)
        sub_dirs_size = 0
        for sub_dir in file_system[key]['Sub_directories']:
            
            if sub_dir in sub_dir_size.keys():
                print(f'Found {sub_dir}: {sub_dir_size[sub_dir]}')
                sub_dirs_size += sub_dir_size[sub_dir]
                
            else:
                sub_dir_size += calculate_directories_size(key, file_system, sub_dir_size)
        
        file_system[key]['Sub_dirs_Size'] = sub_dirs_size
        file_system[key]['Total_Size'] = file_system[key]['Files_Size'] + file_system[key]['Sub_dirs_Size']
        sub_dir_size[key] = file_system[key]['Total_Size']
        
        return sub_dir_size[key]
                

for key, value in reversed(file_system.items()):
    calculate_directories_size(key, file_system, sub_dir_size)   
# for key, value in sub_dir_size.items():
#     print(key, value)

        
        
        
# sub_dir_size = defaultdict(int) 
         
# for key, value in reversed(file_system.items()):
#     print(key)
    
#     if file_system[key]['Sub_directories'] == []:
        
#         if key not in sub_dir_size.keys():
#             files_size = file_system[key]['Files_Size']
#             print(key, files_size)

#             file_system[key]['Total_Size'] += files_size

#             sub_dir_size[key] += files_size

#     else:
#         print(file_system[key]['Sub_directories'])
#         for sub_dir in file_system[key]['Sub_directories']:
#             print(sub_dir)
#             if sub_dir in sub_dir_size.keys():
#                 print(f'Found                     {sub_dir}, {sub_dir_size[sub_dir]}')
#                 file_system[key]['Sub_dirs_Size'] += sub_dir_size[sub_dir]
                
#             else:
#                 print("I don't know this key")
                
#         file_system[key]['Total_Size'] += file_system[key]['Sub_dirs_Size'] + file_system[key]['Files_Size']
                
                
# print(sub_dir_size.keys())            

# for key in file_system.keys():
#     if key not in sub_dir_size.keys():
#         print(f'{key} not in sizes')

# for key, value in sub_dir_size.items():
#     print(key, value)


# target_directories_sum = 0
# for key, value in sub_dir_size.items():
    
#     print(key, value)
#     if sub_dir_size[key] <= 100000:
        
#         print(f"Smaller {key}, {sub_dir_size[key]}")
#         target_directories_sum += sub_dir_size[key]
     
#     else:
#         print(f"bigger {key}, {sub_dir_size[key]}")
         

# print(f"Solution {target_directories_sum}")

