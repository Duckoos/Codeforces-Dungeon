g, c, l = map(int, input().split())
# maxx = max(g, c, l)
# minn = min(g, c, l)
lis = sorted([g, c, l])
if lis[-1] - lis[0] < 10:
    print(f"final {lis[1]}")
else:
    print("check again")