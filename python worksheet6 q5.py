'''for i in range (0,11):
# # nested loop – for each value of i in the outer loop,​
# 
#     # j will iterate through all the values from 1 to 10​
# 
    for j in range (0,11):
        print(i * j, end=' ')
    print("")
# 
#     print() # An empty print statement prints a new line​
'''

numRows=int(input('enter number of rows: '))

for i in range (1,numRows+1):
# # nested loop – for each value of i in the outer loop,​
# 
#     # j will iterate through all the values from 1 to 10​
# 
    for j in range (0,i):
        print("*",end=' ')
    print("")
    
