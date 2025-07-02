def calculate_bmi(weight, height):
    return weight / (height ** 2)

def bmi_status(bmi):
    if bmi < 18.5:
        return "Kam vazn"
    elif bmi < 25:
        return "Normal"
    else:
        return "Ortiqcha vazn"

bmi = calculate_bmi(65, 1.75) 
print("BMI:", bmi)
print("Status:", bmi_status(bmi)) 
