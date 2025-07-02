def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To'g'ri!")
    else:
        print("Xato.")

sirli_son = 7
foydalanuvchi_taxmini = 5
natija = check_guess(sirli_son, foydalanuvchi_taxmini)
print_result(natija)  

foydalanuvchi_taxmini = 7
print_result(check_guess(sirli_son, foydalanuvchi_taxmini)) 
