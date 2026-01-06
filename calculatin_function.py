n  = int(input())
# result = 0
# num = 1

# for i in range(1 ,n + 1):
#     result += ((-1)**i) * i
    # num += 1


# you should know that difference between all even numbers and odd numbers until the range n is always n / 2

if n % 2 == 0:
    result = int(n / 2)
else:
    num = int(n / 2) + 1
    result = num - (2*num)
print(result) 
