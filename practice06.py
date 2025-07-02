def is_valid_phone_number(phone):
    return len(phone) == 9 and phone.isdigit()


print(is_valid_phone_number("998991234")) 
print(is_valid_phone_number("99899abc"))  
