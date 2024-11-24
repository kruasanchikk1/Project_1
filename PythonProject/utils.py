# password_generator/utils.py

def save_password(password, filename='passwords.txt'):
    with open(filename, 'a') as f:
        f.write(password + '\n')
