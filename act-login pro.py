#password
pswd_lis = ['*#*#','12345']
def act_log():
    tries = 3
    while tries > 0:
        pswd = input('Password:')
        pswd_cor = pswd == pswd_lis[-1]
        pswd_reset = pswd == pswd_lis[0]
        if pswd_cor:
            print('suc')
        elif pswd_reset:
                new_pswd = input('enter a new passsword :')
                pswd_lis.append(new_pswd)
                print('reset suc')
                act_log()
        else:
                print('wrong password!')
                tries -= 1
                print('times left', tries)
    else:print('your accout has been suspended')
act_log()
