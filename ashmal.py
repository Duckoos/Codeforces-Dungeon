t = int(input())

for _ in range(t):
    n = int(input())
    words = input().split()

    # find the lexicographically smallest word
    smallest = min(words)

    # build result: smallest first, rest in original order
    result = [smallest]
    used = False
    for w in words:
        if w == smallest and not used:
            used = True
        else:
            result.append(w)

    print("".join(result))
