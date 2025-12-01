a, b = map(int, input().split())
# a = int(input())   # limak's weight
# b = int(input())   # bob's weight

count = 1         # year count
while a <= b:                  # run this loop until a is striclty greater than b 
    a = 3 * a                  # increase their weights every year rerspectively
    b = 2 * b
    if a > b:                  # if a > b, break out of the loop 
        break
    count += 1                 # if a < b, go for another year where limak and bob eat and grow bigger, then compare

print(count)