
# n = int(input('Enter n for array size'))
# print(f"Enter {n} array elements : ")
# li = list()
# for i in range(0,n):
#     i=int(input(f"{i} : "))
#     li[i].append(i)
li = [44,34,370]
len =len(li)
# print(len)
s=0
for i in range(0,len):
    no=li[i]
    r = no%10
    s = (s*10)+r
if(s % 10 == 0):
    print('yes')
else:
    print('no')
