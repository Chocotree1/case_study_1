#Developers: Zaytsev A.
#            Sharypov R.
#            Kurasova P.

import local as lc

#TODO ROMAN

citizen = input('Enter 1 if you are 1 subject, 2 if you are married couple, 3 if you are single parent')
income = input('Enter your annual income: ')

#TODO ALEXANDER
# string constants
annual_income = 0
for i in range(12):
    print('Напишите Ваш ежемесячный доход за',i+1,'месяц года')
    income = float(input())
    annual_income = annual_income + income
print(annual_income)

tax10 = 0.1
tax15 = 0.15
tax25 = 0.25
tax28 = 0.28
tax33 = 0.33
tax35 = 0.35
tax396 = 0.396

#TODO ROMAN
#TODO POLINA

