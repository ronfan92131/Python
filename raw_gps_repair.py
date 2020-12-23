# input: raw.txt
# output: repaired.txt
# what to do:
# read raw.txt file, line-by-line, until the end of file. 
# create a new file named as repaired.txt
# finger_print = ‘tx: +UULOC:’
# for each line, search if finger_print exist
#     if yes, check the line width, if less than the expected, the remaining data is on the next line.  for the next line, slice out the leading 14 bytes and add to the previous line. 

# what’s practiced: 
# how to open a file, 
# how to read line-by-line, until enf of file
# how to check if a word (finger print) exist in a line 
# how to check if repait is needed. 
# how to repair: how to slice two lines and merge into one line. 

file_in = open('raw.txt')
gps_finger_print = 'tx: +UULOC:'

repair_needed = False
finger_print_line = ''

for line in file_in:
    if repair_needed:
        finger_print_line = finger_print_line[:-1] + line[19:]
        print(finger_print_line)
        repair_needed = False

    if gps_finger_print in line:
        finger_print_line = line
        #check how many words seperated by comma,
        words = line.split(',')
        #if less than 12, reaming in the next line, add  
        if len(words) < 12:
            repair_needed = True
        else:
            repair_needed = False    
            print(finger_print_line)


