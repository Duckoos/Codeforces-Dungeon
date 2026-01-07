num = int(input())

votes = input().split()

if votes.count("1") >= 1:
    print("HARD")
else:
    print("EASY")