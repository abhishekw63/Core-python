#find user id and domain name from email address

emailid=input('enter the emailID:')
separator=emailid.find('@') #try index
username=emailid[0:separator:]
domain_name=emailid[separator+1::]
print('username is:',username)
print('domain name is:',domain_name)