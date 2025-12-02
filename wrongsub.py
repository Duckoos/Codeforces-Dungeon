num, k = map(int, input().split())

for i in range(k):
    string = str(num)
    # print(string[-1])
    if string[-1] != "0":
        num -= 1
        string = str(num)
    elif string[-1] == "0":
        string = string[:len(string) - 1]
        num = int(string)
print(num)
    # print(string)
