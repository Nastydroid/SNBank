import random
import string


def home():
    print('welcome to SN bank')
    print('press 1 to login , press 2 to quit')
    log =int(input(':'))
    if log == 1:
        login()
    elif login ==2:
        exit()


def login():
    staff_login= int(input('please press 1 login press 2 to quit:'))
    while staff_login == 1:
        username= input('username:')
        password = input('password:')
        f = open('staff.txt', 'r')
        for row in f:
            staff_list=row.split(',')
            username1=str(staff_list[0])
            password1= str(staff_list[1])
            if username == username1 and password ==password1:
                print('login successful')
                f.close()
                    break
                print(f'what do you want to do today {username} ? ')
                create=int(input('press 1 to create account, press 2 to check account:'))
                if create == 1:
                    create_account()
                
                elif create == 2:
                    check_account()
                
                elif create ==3 :
                    print('have a nice day')
                    exit()
                else:
                    print('invalid')
                    
            else:
                print('invalid')
    
    if staff_login == 2:
        exit()


def create_account():
    print('account creation')
    account_name =input('enter account name:')
    opening_balance =input('opening balance:')
    account_type =input('acccount type:')
    account_email =input('account email:')
    print('generating account number...please hold...')
    pick_up= "1234567890"
    number_lenght= 10
    ac_num=(random.sample(pick_up,number_lenght))
    account_number="".join(ac_num)
    customer_file = open('customer.txt', 'a')
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
    exit()


def check_account():
    det=input('accoint name:')
    customer =open('customer.txt','r')
    file_txt=customer.read()
    print(file_txt)

    '''with open('customer.txt', 'w+') as file:
        for line in file:
            print(line)'''

home()