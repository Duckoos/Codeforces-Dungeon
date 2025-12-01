target = int(input())

count = 0
if target > 5:
    count = target // 5
    if target % 5 != 0:
        count += 1
else:
    count = 1

print(count)