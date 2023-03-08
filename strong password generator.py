#strong password generator

password = input('Enter a password you would like to use: ')

remove = ['i', 'a', 'c', 'Y', '&', 's', 'S', 'z', 'Z']

char = input('Add any one characters you want replaced: ')

remove.append(char)

for i in remove:
    if 'i' in password:
        password = password.replace(i,'1')
    elif 'a' in password:
        password = password.replace(i,'@')
    elif 'c' in password:
        password = password.replace(i,'M')
    elif 'Y' in password:
        password = password.replace(i,'8')
    elif 's' in password:
        password = password.replace(i,'$')
    elif 'S' in password:
        password = password.replace(i,'$')
    elif 'z' in password:
        password = password.replace(i,'}')
    elif 'Z' in password:
        password = password.replace(i,'}')
    elif char in password:
        password = password.replace(i,'00')

print('Your new password is:',password)