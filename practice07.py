def ask_question(question, correct_answer):
    user_answer = input(question + " ") 
    return check_answer(user_answer, correct_answer)

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

savol = "O'zbekiston poytaxti nima?"
togri_javob = "Toshkent"

natija = ask_question(savol, togri_javob)

if natija:
    print(" To'g'ri javob!")
else:
    print(" Noto'g'ri javob.")
