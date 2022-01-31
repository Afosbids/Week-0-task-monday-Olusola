def is_a_leap_year(y):
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 400 == 0 or y % 100 != 0:
        return True  
    else:
        return False
    
print(is_a_leap_year(200))