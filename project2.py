#screening system

age = int(input('How old are you?: '))
if (age > 18) and (age < 65):
    gender = input('Your gender?: ')
    male = 'male'
    female = 'female'
    if female == gender.lower() and (age < 30):
        print('Failure')
    else:
        income = int(input('What is your monthly income?: '))
        if (income > 30000):
            kids = int(input('how many children below 18 do you have?: '))
            if (kids > 2):
                print('Failure')
            else:
                debt = input('Do you have another credits?: ')
                yes = 'yes'
                no = 'no'
                if no == debt.lower():
                    print('Accept')
                else:
                    print('Failure')
        else:
            print('Failure')
else:
    print('Failure')
