#Developers: Zaytsev A.
#            Sharypov R.
#            Kurasova P.

import local as lc
tax10 = 0.1
tax15 = 0.15
tax25 = 0.25
tax28 = 0.28
tax33 = 0.33
tax35 = 0.35
tax396 = 0.396
#TODO ROMAN

citizen = input('Enter 1 if you are 1 subject, 2 if you are married couple, 3 if you are single parent')

#TODO ALEXANDER
# string constants
annual_income = 0
for i in range(12):
    print('Напишите Ваш ежемесячный доход за',i+1,'месяц года')
    income = float(input())
    annual_income = annual_income + income
print(annual_income)

if citizen == 2:
    if annual_income > 0 and annual_income <= 18150:
        tax = tax10*(annual_income - 0)
    elif annual_income > 18150 and annual_income <= 73800:
        tax = tax10*(18150-0)+tax15*(annual_income - 18150)
    elif annual_income > 73800 and annual_income <= 148850:
        tax = tax10*(18150-0)+tax15*(73800 - 18150)+tax25*(annual_income - 73800)
    elif annual_income > 148850 and annual_income <= 226850:
        tax = tax10 * (18150 - 0) + tax15 * (73800 - 18150) + tax25 * (148850 - 73800) + tax28*(annual_income - 148850)
    elif annual_income > 226850 and annual_income <= 405100:
        tax = tax10 * (18150 - 0) + tax15 * (73800 - 18150) + tax25 * (148850 - 73800) + tax28*(226850-148850)+tax33*(annual_income-226850)
    elif annual_income > 405100 and annual_income <= 457600:
        tax = tax10 * (18150 - 0) + tax15 * (73800 - 18150) + tax25 * (148850 - 73800) + tax28 * (226850 - 148850) + tax33 * (405100 - 226850)+tax35*(annual_income-405100)
    elif annual_income > 457600:
        tax = tax10 * (18150 - 0) + tax15 * (73800 - 18150) + tax25 * (148850 - 73800) + tax28 * (226850 - 148850) + tax33 * (405100 - 226850) + tax35 * (457600-405100)+tax396*(annual_income-457600)

#TODO ROMAN
#TODO POLINA

