
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0 ga bo'lish mumkin emas"


a = 10
b = 5

print("Qo'shish:", add(a, b))        
print("Ayirish:", subtract(a, b))    
print("Ko'paytirish:", multiply(a, b)) 
print("Bo'lish:", divide(a, b))      
