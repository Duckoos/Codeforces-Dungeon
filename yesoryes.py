t = int(input())

lis = []
for i in range(t):
    string = input()
    if string.lower() == "yes":
        lis.append("YES")
    else:
        lis.append("NO")

for result in lis:
    print(result)
