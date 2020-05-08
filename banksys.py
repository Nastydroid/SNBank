import random
import string 
import os

print('welcome to SNBank')
staff_login= int(input('press 1 to login or press 2 to quit:'))
while staff_login == 1:
    username = input('enter username:').lower()
    password = input('enter password:').lower()
    f = open('staff.txt', 'r')
    for row in f:
        staff_list=row.split(',')
        username1=str(staff_list[0])
        password1= str(staff_list[1])
        if username == username1 and password ==password1:
            print('login successful')
            new_session='session.txt'
            session=open(new_session,'a+')
            session.write('you are logged in')
            session.write('\n')
            session.write(f'username:{username}')
            session.write('\n')
            session.write('password:{password}')
            session.close()
            f.close()
            success = True
            while success == True:
                print(f'what do you want to do today {username} ? ')
                print('press 1 for account creation, press 2 to check account, press 3 to logout')
                user_input=int(input(':'))
                if user_input == 1:
                    print('account creation')
                    account_name =input('enter account name:')
                    opening_balance =input('opening balance:')
                    account_type =input('acccount type:')
                    account_email =input('account email:')
                    print('generating account number...please hold...')
                    pick_up= "1234567890"
                    number_lenght= 10
                    ac_num=(random.sample(pick_up,number_lenght))
                    pre_number="".join(ac_num)
                    account_number =  pre_number
                    customer_file = open('customer.txt', 'w+')
                    customer_file.write(account_name)
                    customer_file.write('\n')
                    customer_file.write(opening_balance)
                    customer_file.write('\n')
                    customer_file.write(account_type)
                    customer_file.write('\n')
                    customer_file.write(account_number)
                    customer_file.write('\n')
                    customer_file.write(account_email)
                    customer_file.close()
                    print(f'{account_name} account number is {account_number}')
                
                if user_input == 2:
                    acct_details =input('enter account name or number:')
                    customer =open('customer.txt','r')
                    file_txt=customer.read()
                    print(file_txt)
                
                elif user_input == 3:
                    os.remove('session.txt')
                    print('session deleted')
                    print('have a nice day')
                    exit()
                else:
                    print('invalid')
                    
            
                        
        else:
            print('invalid details')

            




else:
    exit()


                  
