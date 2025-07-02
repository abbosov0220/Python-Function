def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    if age >= 18:
        print(f"Siz {age} yoshdasiz. Balog'atga yetgansiz.")
    else:
        print(f"Siz {age} yoshdasiz. Balog'atga yetmagansiz.")

calculate_age(2010, 2025)  
calculate_age(2000, 2025) 
