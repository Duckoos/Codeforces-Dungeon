
n = int(input())
props = map(int, input().split())

result = (sum(props) / n)
print(format(f"{result:.12f}"))