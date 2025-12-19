word = input()

u_count = 0 # uppercase letters count
l_count = 0 # number of lowercase letters

for i in word:
    if 65 <= ord(i) <= 90:
        u_count += 1
    elif 97 <= ord(i) <= 122:
        l_count += 1

if u_count > l_count:
    print(word.upper())
else:
    print(word.lower())