# REDI_project_ATM
print('Welcome to Srarkasse')
trying = 3
realpassword = 5555
while trying !=0:
password = int(input('Enter your Password'))
if password != realpassword:
    trying = trying - 1 
    print('invalid password! You have {}  tries left.' .format(trying) )
        else:
            user_choise = input('pay out cash? y/n')
        if user_choise == 'y':
            user_sum = input('Enter the Amount')
        print('Here please, your {} €' .format(user_sum))    
         if user_choise == 'n': 
             user_exit = input('would you like to exit? y/n')
             print("thank you for using Sparkasse!")
        break 
    else:
        continue
