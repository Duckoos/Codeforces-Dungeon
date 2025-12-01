testcase = int(input())
arr = []
b = []

for i in range(testcase):
    a = []
    size = int(input())
    for j in range(size):
        # a = list(map(int, input().split()))[:size]
        val = int(input())
        a.append(val)
    arr.append(a)
    
    for j in arr:
        for k in range(max(j)):
            
            for l in range(size - 1):
                b.append()
