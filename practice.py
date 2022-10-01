
# def isDigitPresent(x,d):
#     while(x>0):
#         if(x%10 == d):
#             break
#         x = x/10
#     return (x>0)

# def printNumbers(n,d):
#     for i in range(0,n+1):
#         if(i==d or isDigitPresent(i,d)):
#             if(i == d or isDigitPresent(i,d)):
#                 print(i,end =' ')

# n = 20
# d = 1
# print('The no of values are')
# printNumbers(n,d)


#Find Digit in particular range of numbers
ranj = int(input("Enter Range for digit : "))
dig = int(input("Enter Digit to Find : "))
cnt = 0
for i in range(1,ranj+1):
    no = i
    while(no>0):
        #Type casting is very important in this code
        r = int(no % 10) #This line Screw my Technical round might be job also
        if(r==dig):
            print(i)
            cnt+=1
            break
        else:
            no = no /10
print(f"Total Count of {dig} is : {cnt}")



