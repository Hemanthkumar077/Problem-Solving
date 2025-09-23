def non_repeating(str1):
    dict1 = {}
    for i in str1 :
        if i not in dict1 :
            dict1[i] = 1
        else :
            dict1[i] += 1
    emp_list = []
    for key , value in dict1.items():
        if value == 1 :
            emp_list.append(key)
    return emp_list[0]
    
result = non_repeating("swiss")
print(result)