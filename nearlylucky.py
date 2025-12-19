num = int(input())
word = str(num)
count = 0

for i in word:
    if i == "4" or i == "7":
        count += 1
    else:
        continue

if count == 4 or count == 7:
    print("YES")
else:
    print("NO")
