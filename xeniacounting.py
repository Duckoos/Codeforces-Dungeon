string = input()
if len(string) > 1:
    sorted_string = sorted(string.split("+"))    # split the string wherever + occurs and the sort the list returned by the split function
    print('+'.join(sorted_string))               # join the sorted list with + between the elements
else:
    print(string)                                # print the string


# 2nd approach, same but more caveman thinking
# lis = []                                         # empty list to store the elements
# result = ""                                      # empty string to store the result
# for i in string:
#     if i != "+":                                 # parse through the input string and put the elements other than "+" in the empty list
#     lis.append(i)

# lis.sort()                                       # sort it
# for i in range(len(lis)):
#     if i < len(lis) - 1:
#         result += f"{int(lis[i])}+"              # repeaet this process until last but one element, cuz it;ll add a + after the last element if we dont
#     elif i == len(lis) - 1:
#         result += lis[i]
# print(result)