n = int(input())

lis = []
if n == 1:
    print("I hate it")
# elif n == 2:
#     print("I love it")
else:
    for i in range(1, n + 1):
        if i == n:
            if i % 2 == 0: 
                lis.append("I love it")
                break
            else:
                lis.append("I hate it")
                break
        
        if i % 2 == 0: 
            lis.append("I love")
        else:
            lis.append("I hate")
    print(" that ".join(lis))