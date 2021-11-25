'''
for number in range (10,21):
    #print(number)
    
sumNum=0
for evenNum in range (10,21,2):
    print( evenNum, '+', sumNum, '=', evenNum + sumNum)
    sumNum= evenNum+ sumNum
'''
sumNum=0
for evenNum in range (10,21):
    if evenNum % 2 == 0:
        print (evenNum)
        sumNum= evenNum+ sumNum
print("answer is : ",sumNum)

