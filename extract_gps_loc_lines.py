# input: lines_w_gps.txt
# output: gps.txt
# what to do:
# from extract_gps_loc import extract+gps_loc 
# read lines_w_gps.txt file, line-by-line, until the end of file. 
# create a new file named as gps.txt
# for each line, 
# gps = extract_gps_loc(line)
# write gps to gps.txt

# what’s practiced: 
# how to import a function from another module, and make use it 
from extract_gps_loc import extract_gps_loc  
# how to open a file, 
file_in = open('input.txt')
# how to read line-by-line, until enf of file
# how to check finger print for each line
# how to extract specific contents from each line
# how to use set eliminate duplicates
# how to create a new file, write into the file

gps_finger_print = 'tx: +UULOC:'

#lines = ''
#following code will extract lines with gps finger prints
# for line in file_in:
#     if gps_finger_print in line:
#         lines = lines + line
# print(lines)

# # following code will 
# # extract lines with gps finger prints
# # then extract gps loc only
# from extract_gps_loc import extract_gps_loc  
# for line in file_in:
#     if gps_finger_print in line:
#         lines = lines + extract_gps_loc(line) + '\n'
# print(lines)

# following code will 
# extract lines with gps finger prints
# then extract gps loc only
# and eliminate redudant points with set
# creat an empty set for gps, to store unique gps locations.
gps = set('')
for line in file_in:
    if gps_finger_print in line:
        loc = extract_gps_loc(line)
        gps.add(loc)
#print one loc per line, pop it :)
while len(gps):
    print(gps.pop())
