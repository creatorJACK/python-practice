#Calculator

def addition():
    print("Addition")
    n = float(input("Enter the number : "))
    t = 0 #Total number enter
    ans = 0
    while n!=0:
        ans = ans + n
        t += 1
    n = float(input("Enter the number : "))
    return [ans,t]