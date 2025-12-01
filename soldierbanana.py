k, n, w = map(int, input().split())

lis = [i * k for i in range(1, w + 1)]
# print(lis)

total_needed = sum(lis)
if n > total_needed:
    print(0)
else:
    cash_to_borrow = total_needed - n
    print(cash_to_borrow)