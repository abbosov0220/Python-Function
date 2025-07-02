def calculate_tax(salary):
    if salary > 5000000:
        return salary * 0.20
    else:
        return salary * 0.13

def calculate_net_salary(salary):
    return salary - calculate_tax(salary)

salary = 6000000
print("Soliq:", calculate_tax(salary))        
print("Sof maosh:", calculate_net_salary(salary)) 
