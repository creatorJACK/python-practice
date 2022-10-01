def bubble(li):
    print('HI')
    l = len(li)
    cnt=0
    for i in range(0,l):
        for j in range(i,l):
            if li[i] > li[j]:
                temp  = li[i]
                li[i] = li[j]
                li[j] = temp
        cnt+=1
    print('Itteration no : ',cnt)
                
li = [99,123,12435,2,23,34]
print('List Before',li)
bubble(li)
print(li)
