no_of_rooms = int(input())
count = 0

for i in range(no_of_rooms):
    students_in_room, room_size = map(int, input().split())
    if students_in_room <= room_size - 2:
        count += 1

print(count)