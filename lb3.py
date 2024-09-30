import math

# Функції корисності для обох студентів
def utility_student_1(x):
    return 1.3 * x

def utility_student_2(x):
    return 1.4 * math.sqrt(x)

def expected_utility(utility_function, x_win, prob_win, x_lose, prob_lose):
    return prob_win * utility_function(x_win) + prob_lose * utility_function(x_lose)

# Аналіз ставлення до ризику
def risk_preference(U_M_X, M_U_X):
    if U_M_X > M_U_X:
        return "несхильний до ризику"
    elif U_M_X < M_U_X:
        return "схильний до ризику"
    else:
        return "нейтральний до ризику"

initial_money = 50
win_amount = 150
lose_amount = 0
probability_win = 0.5
probability_lose = 0.5

# Сподіваний виграш
expected_win = probability_win * win_amount + probability_lose * lose_amount

# Корисність, якщо не робити ставку
utility_no_bet_1 = utility_student_1(initial_money)
utility_no_bet_2 = utility_student_2(initial_money)

# Очікувана корисність, якщо робити ставку
expected_utility_bet_1 = expected_utility(utility_student_1, win_amount, probability_win, lose_amount, probability_lose)
expected_utility_bet_2 = expected_utility(utility_student_2, win_amount, probability_win, lose_amount, probability_lose)

# Характеристики студентів
# Для першого студента
U1_M_X = utility_student_1(expected_win)
M_U1_X = expected_utility_bet_1
student_1_preference = risk_preference(U1_M_X, M_U1_X)

# Для другого студента
U2_M_X = utility_student_2(expected_win)
M_U2_X = expected_utility_bet_2
student_2_preference = risk_preference(U2_M_X, M_U2_X)

print("Перший студент:")
print(f"Корисність без ставки: {utility_no_bet_1}")
print(f"Очікувана корисність зі ставкою: {expected_utility_bet_1}")
print("Рішення: " + ("робити ставку" if expected_utility_bet_1 > utility_no_bet_1 else "не робити ставку"))
print(f"Студент є {student_1_preference}")

print("\nДругий студент:")
print(f"Корисність без ставки: {utility_no_bet_2}")
print(f"Очікувана корисність зі ставкою: {expected_utility_bet_2}")
print("Рішення: " + ("робити ставку" if expected_utility_bet_2 > utility_no_bet_2 else "не робити ставку"))
print(f"Студент є {student_2_preference}")
