word = input()
word2 = input()

word_reversed = word[::-1]

if word_reversed == word2:
    print("YES")
else:
    print("NO")