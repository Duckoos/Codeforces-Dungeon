# matrix = []

# for i in range(1, 6):    
#     row = []                                   
#     for j in range(1, 6):
#         val = int(input())
#         row.append(val)
#         if val == 1:
#             m = i
#             n = j
#     matrix.append(row)

# result = abs(3 - m) + abs(3 - n)
# print(result)

# above code gives a runtime error 
# middle element in the 5 * 5 matrix is matrix[3][3]
# the single one in the matrix should be moved to this position to make the matrix beautiful
# if the position of 1 in the matrix 2, 5 -> minimal amount of tranformation should be (3 - 2) row tranformations and (5 - 3) tranformations. total = 3

matrix = []
for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            m = i
            n = j
            break
    matrix.append(row)

# print(m , n)
result = abs(2 - m) + abs(2 - n)
print(result)

# can get the values of m and n using enumerate function as well
