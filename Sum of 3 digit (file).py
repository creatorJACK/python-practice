num = int(input('Enter any Number : '))
sum = int(input('How much sum U want to Find : '))
cnt=0
myfile = open("myfile.txt","w")
for i in range(1,num+1):
    n=i
    s=0
    while(n>0):
        r=int(n%10)
        s+=r
        n=n/10
    if(s==sum):
        myfile.write(str(i))
        myfile.write("\n")
        # print(i)
        cnt+=1
myfile.close()
print("Total Count of digits having sum", sum, ":is :" ,cnt)