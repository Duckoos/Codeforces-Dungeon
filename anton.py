inp = int(input())
str = input()
a, b = str.count("A"), str.count("B")

if a > b:
    print("Anton")
elif b > a:
    print("Danik")
else:
    print("Friendship")

