year = int(input())
flag = True
check_year = year

while flag:
    check_year += 1
    # print(check_year)
    if len(set(str(check_year))) == 4:
        result = check_year
        flag = False
        break
    
    
        
    

print(result)