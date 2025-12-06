# my solution 
import string
lis = list(string.ascii_lowercase)
# print(lis)

def check(word):
    for i in lis:
        if i not in word:
            return False
        else:
            continue
    return True
        
n = int(input())
word = input().lower()

if check(word):
    print("YES")
else:
    print("NO")
    

# another solution - common sense
# n = int(input())
# word = input().lower()

# if len(set(word)) == 26:
#     print("YES")
# else:
#     print("NO")