str = "I Like Codding"
newstr = ""
for ch in str:
    cnt = 0
    for i in str:
        if ch == i:
            cnt+=1
    if ch not in newstr:
        newstr += ch
        print(f"'{ch}' = '{cnt}' time")
print(newstr)