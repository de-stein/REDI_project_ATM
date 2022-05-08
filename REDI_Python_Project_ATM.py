print('Welcome to Srarkasse')
trying = 3
true_pin = 5555
while trying != 0:
    pin = int(input('Enter your Password'))
    if pin != true_pin:
        trying = trying - 1 
        print('invalid password! You have {}  tries left.' .format(trying) )
    else:
        user_choise = input('enter "d" to deposit, enter "w" to whithdraw, enter "e" to exit')
        if user_choise == 'd':
            deposit = input('Enter the Amount')
            print('Here please, your {} €' .format(deposit))
        elif user_choise == 'w':
            withdraw = input('Enter the Amount, put the money and press Enter')
            print('Here please, your {} €' .format(withdraw))    
        elif user_choise == 'e': 
                print("thank you for using Sparkasse!")
        else:  
            print("thank you for using Sparkasse!")       
        break
else:
        continue
