print('Welcome to Sparkasse! ')
sum_account_1 = 500
sum_account_2 = 200
sum_account_3 = 300
trying = 3
true_pin_account_1 = 5555
true_pin_account_2 = 2222
true_pin_account_3 = 3333
enter_your_chois = 'Enter "d" to deposit, enter "w" to withdraw, enter "e" to exit '
goodbye = "Thank you for using Sparkasse! Don't forget you card. "
while trying != 0:
    pin = int(input('Enter your Password: '))
    if pin != true_pin_account_1 and pin != true_pin_account_2 and pin != true_pin_account_3:
        trying = trying - 1
        print('invalid password! You have {} tries left. ' .format(trying) )
    else:
        user_choise = input(enter_your_chois)
        if user_choise == 'd':
            deposit = input('Enter the Amount, put the money and press Enter ')
            print('Here please, your amount deposited is: {} €' .format(deposit))
            print(goodbye)
        elif user_choise == 'w':
            withdraw = input('Enter the Amount: ')
            print('Here please, your amount withdrawn is: {} €'.format(withdraw))
            print(goodbye)
        elif user_choise == 'e':
                print(goodbye)
        else:
            print(goodbye)
    break
