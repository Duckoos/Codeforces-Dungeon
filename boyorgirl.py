usrnm = input().lower()
no_of_unique = len(set(usrnm))
# print(no_of_unique)

if no_of_unique % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")