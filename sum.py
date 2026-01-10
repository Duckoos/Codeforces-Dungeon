t = int(input())
lis = []
for i in range(t):
    a, b, c = map(int, input().split())
    if a + b == c or b + c == a or c + a == b:
        lis.append("YES")
    else:
        lis.append("NO")

for result in lis:
    print(result)
