# n = int(input())
# k = int(input)
# scores = []
# for i in range(n):
#     score = int(input())
#     scores.append(score)

# count = 0
# for i in range(len(scores)):
#     if scores[i] > 0 and scores[i] >= scores[k]:
#         count += 1

# print(count)

n, k = map(int, input().split())
scores = list(map(int, input().split()))

count = 0
for i in range(len(scores)):
    if scores[i] > 0 and scores[i] >= scores[k - 1]:
        count += 1

print(count)

