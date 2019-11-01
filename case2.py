#Developers: Zaytsev A. 50%
#            Sharypov R. 50%
#            Kurasova P. 0%

import local as lc
tax10 = 0.1
tax15 = 0.15
tax25 = 0.25
tax28 = 0.28
tax33 = 0.33
tax35 = 0.35
tax396 = 0.396
#TODO ROMAN

citizen = input('Enter 1 if you are 1 subject, 2 if you are married couple, 3 if you are single parent: ')

#TODO ALEXANDER
# string constants
annual_income = 0
for i in range(12):
    print('Write your income for',i+1,'month of the year:')
    income = float(input())
    annual_income = annual_income + income
print('annual_income = ',annual_income)

if citizen == '2':
    if annual_income >= 0 and annual_income <= 18150:
        tax = tax10*(annual_income - 0)
        print('tax = ',tax)
    elif annual_income > 18150 and annual_income <= 73800:
        tax = tax10*(18150-0)+tax15*(annual_income - 18150)
        print('tax = ',tax)
    elif annual_income > 73800 and annual_income <= 148850:
        tax = tax10*(18150-0)+tax15*(73800 - 18150)+tax25*(annual_income - 73800)
        print('tax = ',tax)
    elif annual_income > 148850 and annual_income <= 226850:
        tax = tax10 * (18150 - 0) + tax15 * (73800 - 18150) + tax25 * (148850 - 73800) + tax28*(annual_income - 148850)
        print('tax = ',tax)
    elif annual_income > 226850 and annual_income <= 405100:
        tax = tax10 * (18150 - 0) + tax15 * (73800 - 18150) + tax25 * (148850 - 73800) + tax28*(226850-148850)+tax33*(annual_income-226850)
        print('tax = ',tax)
    elif annual_income > 405100 and annual_income <= 457600:
        tax = tax10 * (18150 - 0) + tax15 * (73800 - 18150) + tax25 * (148850 - 73800) + tax28 * (226850 - 148850) + tax33 * (405100 - 226850)+tax35*(annual_income-405100)
        print('tax = ',tax)
    elif annual_income > 457600:
        tax = tax10 * (18150 - 0) + tax15 * (73800 - 18150) + tax25 * (148850 - 73800) + tax28 * (226850 - 148850) + tax33 * (405100 - 226850) + tax35 * (457600-405100)+tax396*(annual_income-457600)
        print('tax = ',tax)

#TODO ROMAN

if citizen == '3':
    if annual_income >= 0 and annual_income <= 12950:
        tax = tax10*(annual_income - 0)
        print('tax = ',tax)
    elif annual_income > 12950 and annual_income <= 49400:
        tax = tax10*(12950-0)+tax15*(annual_income - 12950)
        print('tax = ',tax)
    elif annual_income > 49400 and annual_income <= 127550:
        tax = tax10*(12950-0)+tax15*(49400 - 12950)+tax25*(annual_income - 49400)
        print('tax = ',tax)
    elif annual_income > 127750 and annual_income <= 206600:
        tax = tax10 * (12950-0) + tax15 * (49400 - 12950) + tax25 * (127550 - 49400) + tax28*(annual_income - 127550)
        print('tax = ',tax)
    elif annual_income > 206600 and annual_income <= 405100:
        tax = tax10 * (12950-0) + tax15 * (49400 - 12950) + tax25 * (127550 - 49400) + tax28*(206600 - 127750)+tax33*(annual_income - 206600)
        print('tax = ',tax)
    elif annual_income > 405100 and annual_income <= 432200:
        tax = tax10 * (12950-0) + tax15 * (49400 - 12950) + tax25 * (127550 - 49400) + tax28 * (206600 - 127750) + tax33 * (405100 - 206600)+tax35*(annual_income - 405100)
        print('tax = ',tax)
    elif annual_income > 432200:
        tax = tax10 * (12950-0) + tax15 * (49400 - 12950) + tax25 * (127550 - 49400) + tax28 * (206600 - 127750) + tax33 * (405100 - 206600) + tax35 * (432200 - 405100)+tax396*(annual_income - 432200)
        print('tax = ',tax)

if citizen == '1':
    if annual_income >= 0 and annual_income <= 9075:
        tax = tax10*(annual_income - 0)
        print('tax = ',tax)
    elif annual_income > 9075 and annual_income <= 36900:
        tax = tax10*(9075-0)+tax15*(annual_income - 9075)
        print('tax = ',tax)
    elif annual_income > 36900 and annual_income <= 89350:
        tax = tax10*(9075-0)+tax15*(36900 - 9075)+tax25*(annual_income - 89350)
        print('tax = ',tax)
    elif annual_income > 89350 and annual_income <= 186350:
        tax = tax10 * (9075 - 0) + tax15 * (36900 - 9075) + tax25 * (89350 - 36900) + tax28*(annual_income - 89350)
        print('tax = ',tax)
    elif annual_income > 186350 and annual_income <= 405100:
        tax = tax10 * (9075 - 0) + tax15 * (36900 - 9075) + tax25 * (89350 - 36900) + tax28*(186350 - 89350)+tax33*(annual_income - 89350)
        print('tax = ',tax)
    elif annual_income > 405100 and annual_income <= 406750:
        tax = tax10 * (9075 - 0) + tax15 * (36900 - 9075) + tax25 * (89350 - 36900) + tax28 * (186350 - 89350) + tax33 * (405100 - 186350)+tax35*(annual_income - 405100)
        print('tax = ',tax)
    elif annual_income > 406750:
        tax = tax10 * (9075 - 0) + tax15 * (36900 - 9075) + tax25 * (89350 - 36900) + tax28 * (186350 - 89350) + tax33 * (405100 - 186350) + tax35 * (406750 - 405100)+tax396*(annual_income - 406750)
        print('tax = ',tax)

#TODO POLINA

