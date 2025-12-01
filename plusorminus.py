testcase = int(input())

lis = []
for i in range(testcase):
    a, b, c = map(int, input().split())
    lis.append([a, b, c])
# print(lis)
for input in lis:
    if input[0] + input[1] == input[2]:
        print("+")
    elif input[0] - input[1] == input[2]:
        print("-")