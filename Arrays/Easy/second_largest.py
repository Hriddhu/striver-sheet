def second_largest_element(num):
    largest= 0
    second_largest= 0
    for i in num:
        if i>largest:
            second_largest=largest
            largest=i
        elif i>second_largest:
            second_largest=i
        
            
    