def c_to_f(celsius):
    return celsius * 9/5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("0°C =", c_to_f(0), "°F")       
print("100°F =", f_to_c(100), "°C")   
