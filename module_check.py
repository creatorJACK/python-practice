# n=5
# for i in range(n):
#     for j in range(i,5):
#         print(' ',end='  ')
    
#     for j in range(i+1):
#         print('*',end='  ')
#     print()


# # n=20
# # for i in range(0,10):
# #     cnt=0
# #     for j in range(0,n):
# #         if cnt<i*2 and (i+j>=(n/2)):
# #             print(' ',end=' ')
# #             cnt+=1
# #         else:
# #             print('*',end=' ')
# #     print()
# # n=8
# # ct=1
# # for r in range(0,4):
# #     print(ct)
# #     for k in range(0,ct):
# #             print(str(r)+str(k),end='  ')
# #             ct+=1
# #     print()
# #     print()
# n=4
# for i in range(n):
#         for j in range(n-i):
#                 print('*',end='  ')
#         for j in range(i):
#                 print(' ',end='  ')
#         for j in range(i):
#                 print(' ',end='  ')    
#         for j in range(i,n):
#                 print('*',end='  ')
#         print() 
# for r in range(n):
#         for c in range(r+1):
#                 print('*',end='  ')
#         for c in range(r+1,n):
#                 print(' ',end='  ')
#         for c in range(n-r-1):
#                 print(' ',end='  ')
#         for c in range(r+1):
#                 print('*',end='  ')
#         print()
n=5
for i in range(n-1):
    for j in range(i,n):
        print(' ',end='  ')
    for j in range(i):
        print('*',end='  ')
    for j in range(i+1):
        print('*',end='  ')
    print()

for k in range(n):
    for m in range(k+1):
        print(' ',end='  ')
    for m in range(k,n-1):
        print('*',end='  ')
    for m in range(k,n):
        print('*',end='  ')
    print()