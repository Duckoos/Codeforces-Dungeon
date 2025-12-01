no_of_stones = int(input())
stone_color = list(input())
# print(stone_color)
count = 0
if len(set(stone_color)) == 1:
    print(len(list(stone_color)) - 1)
else:
    for i in range(1, len(stone_color)):
        if i < len(stone_color) - 1:
            if stone_color[i - 1] == stone_color[i] or stone_color[i + 1] == stone_color[i]:
                stone_color.remove(stone_color[i])
                count += 1
            else:
                continue
    print(count)
