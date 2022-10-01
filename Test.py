# Find Count of Palindrome words from Sentence
sen = "Hello madam my name is nitin"

resen = sen[ : :-1]
cnt =0
if sen == resen:
    print("Full sentense is palindrome")
    cnt+=1
li = sen.split(' ')
print(li)
for i in range(0,6):
    if li[i] == (li[i][ : :-1]):
        print(li[i])
        cnt+=1
print(f"Total Count is {cnt}")


#Multiply 2 no without *
n1 = 7
n2 = 10
res = 0
for i in range(0,n2):
    res = res+n1
print(f"Multiplication of {n1} and {n2} is{res}")

