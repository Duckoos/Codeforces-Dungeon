n = int(input())

lis = []


for i in range(1, n + 1):
        if i % 2 == 0: 
            lis.append("I love")
        else:
            lis.append("I hate")

print(" that ".join(lis) + " it")