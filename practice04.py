def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


print(get_grade(95)) 
print(get_grade(83))  
print(get_grade(72)) 
print(get_grade(60))  
