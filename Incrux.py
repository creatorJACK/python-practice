str1 = input("Enter First word : ")
str2 = input("Enter Second word : ")
sstr1 = sorted(str1)
print(sstr1)
sstr2 = sorted(str2)
print(sstr2)

if sstr1 == sstr2:
    print("Anagram")
else:
    print("Not Anagram")