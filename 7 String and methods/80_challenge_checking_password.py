pass1=input('enter the password:')
pass2=input('confirm your password:')

if pass1==pass2:
    print('Password matches!')
else:
    if pass1.lower()==pass2.lower():        #can try withcasefold too.
        print('almost there but check your cases')
    else:
        print('Password is incorrect please try again.')