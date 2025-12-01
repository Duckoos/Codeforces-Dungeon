testcase = int(input())
lis = []
out = []
count = 0
for i in range(testcase):
    val = int(input())
    lis.append(val)

for val in lis:
    count = 0
    if val == 2:
        count = 1
    if val % 2 == 0:
        for j in range((val // 2) + 1):
            if val > 2 and (val - (2 * j)) % 4 == 0:
                count += 1 
    else:
        count = 0
    out.append(count)

for i in out:
    print(i)
