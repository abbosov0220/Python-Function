def is_strong_password(password):
    return len(password) >= 8


print(is_strong_password("abc123"))    
print(is_strong_password("abc123456")) 
