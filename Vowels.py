a_str = input("Enter String ")
lowercase = a_str.lower()

vowel_cnt = {}
for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_cnt[vowel] = count 

counts = vowel_cnt.values()
total_vowels = sum(counts)
print("Total Vowels in string" ,total_vowels)
