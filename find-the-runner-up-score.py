# Find the runner-up score
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Given the participants' score sheet for your University Sports Day, you are required 
# to find the runner-up score. You are given  scores. Store them in a list and 
# find the score of the runner-up.

# Input Format
# The first line contains n. The second line contains an array A[]  of n integers
# each separated by a space.

# Constraints
#2<=n<=10
#0<=A[i]<=100
# Output Format
# Print the runner-up score.

# Sample Input 0
# 5
# 2 3 6 6 5
# Sample Output 0
# 5
# Explanation 0
# Given list is [2 3 6 6 5] . The maximum score is 6, second maximum is 5. 
# Hence, we print  5 as the runner-up score.

# ===== design =============================================
# store the input as a list (str)
# convert it to a list of integer
# sort 
# pop for champ, pop again until runner-up

# ===== implementation =====================================
# get first input as integet
n = int(input())
#n = 5
print(n)

# get second line input and store as a list_str
lst_s = input().split()
#lst_s = ['2', '3', '6', '6', '5']
print(lst_s)

# convert list_str to list_int
lst_i = [int(lst_s.pop())]
while len(lst_s):
    lst_i.insert(0,int(lst_s.pop()))
print(lst_i)

# sort it
lst_i.sort()
print(lst_i)

# find the champ and runner-up
champ = lst_i.pop()
runner = champ
while runner == champ and len(lst_i):
    runner = lst_i.pop()
print('champ: ' + str(champ) + '  runner: ' + str(runner))
