# module 3:  extract_gps_loc.py
# input: a string / line with gps loc, such as 
# [11:31:50.971] tx: +UULOC: 15/12/2020,19:31:19.000,32.9398982,-117.1106165,0,341,0,0,0,2,0,0,0
# output: print gps latitude and longitude only
# 32.9398982,-117.1106165
# what’s practiced: 
# how to define a function, specify input and output
# for a given string, how to strip “white space”, “comma” and save to an array of words. 
# how to return only interested words. 
# how to call a function
 
# pseudo codes: 
# #def a function, 
# def extract_gps_loc(line)
#     gps=’’
#     //write your code here

#     return gps

# #call the function.
# line = ‘[11:31:50.971] tx: +UULOC: 15/12/2020,19:31:19.000,32.9398982,-117.1106165,0,341,0,0,0,2,0,0,0’
# 	extract_gps_loc(line)

#def a function, 
def extract_gps_loc(line):
    gps = ''
    #write your code here
    words = line.split(',')
    gps = words[2] + ',' + words[3]
    return gps

#call the function.
line = '[11:31:50.971] tx: +UULOC: 15/12/2020,19:31:19.000,32.9398982,-117.1106165,0,341,0,0,0,2,0,0,0'
print(extract_gps_loc(line))
