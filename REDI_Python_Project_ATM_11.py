print('Welcome to Sparkasse! ')
account = [
    ["11","1111"],
    ["22","2222"],
    ["33","3333"]
]                         # account is a table with: [0]=account number, [1]=pin 
balance_01 = int(1000)
balance_02 = int(2000)
balance_03 = int(3000)
trying = 3
enter_your_chois = 'Enter "d" to deposit \nenter "w" to withdraw, \nenter "b" to balance \nenter "e" to exit '
goodbye = "Thank you for using Sparkasse! Don't forget you card. "
while trying != 0:
    accont_number_input = input(str('Enter your account number, 2 numbers '))
    pin_input = input(('Enter your pin, 4 numbers '))
    data_input =[accont_number_input, pin_input]
    if (data_input not in account):
        trying = trying - 1
        print('invalid pin or account number! You have {} tries left. ' .format(trying) )
    else:
        user_choise = input(enter_your_chois)
        if user_choise == 'd':
            deposit = int(input('Enter the Amount, put the money and press Enter '))
            if data_input == account[0] :
                balance_01 = balance_01 + deposit
                print('Here please, your amount deposited is: {} €. Your balance is {} € now. ' .format(deposit, balance_01))
                print(goodbye)
            elif data_input == account[1] :
                balance_02 = balance_02 + deposit
                print('Here please, your amount deposited is: {} €. Your balance is {} € now. ' .format(deposit, balance_02))
                print(goodbye)
            else:
                balance_03 = balance_03 + deposit
                print('Here please, your amount deposited is: {} €. Your balance is {} € now. ' .format(deposit, balance_03))
                print(goodbye)
        elif user_choise == 'w':
            withdraw = int(input('Enter the Amount: '))
            if data_input == account[0] and withdraw < balance_01:
                balance_01 = balance_01 - withdraw
                print('Here please, your amount withdrawn is: {} €. Your balance is {} € now. '.format(withdraw, balance_01))
                print(goodbye)
            elif data_input == account[1] and withdraw < balance_02:
                balance_02 = balance_02 - withdraw
                print('Here please, your amount withdrawn is: {} €. Your balance is {} € now. '.format(withdraw, balance_02))
                print(goodbye)
            elif data_input == account[2] and withdraw < balance_03:
                balance_03 = balance_03 - withdraw
                print('Here please, your amount withdrawn is: {} €. Your balance is {} € now. '.format(withdraw, balance_03))
                print(goodbye)
            elif (data_input == account[0] and withdraw > balance_01) or (data_input == account[1] and withdraw > balance_02) or (data_input == account[2] and withdraw > balance_03):
                print("you don't have enough money in your account.")
                print(goodbye)   
        elif user_choise == 'e':
                print(goodbye)
        elif user_choise == 'b':
            if data_input == account[0]:
                print("Your balance is {} € " .format(balance_01))
                print(goodbye)
            elif data_input == account[1]:
                print("Your balance is {} € " .format(balance_02))
                print(goodbye)
            else:
                print("Your balance is {} € " .format(balance_03))
                print(goodbye)
        else:
            print(goodbye)
        
