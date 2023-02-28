# Instructions
# 1. - Run SAGE and output accounts to a channel via webhook
# 2. - Copy and paste all the accounts from the channel into raw.txt
# 3. - Run script

from termcolor import colored

def log(message):
    print(colored("[logs]", "yellow"), message)

try:
    with open('raw.txt', 'r') as f:
        log('Finding Account cluster')
        data = f.read()
        log('reading account cluster')

    lines = data.split('\n')
    usernames = []
    passwords = []

    for i in range(len(lines)):
        if lines[i] == 'Username':
            usernames.append(lines[i+1])
        elif lines[i] == 'Password':
            passwords.append(lines[i+1])

    with open('./output.txt', 'w') as f:
        for i in range(len(usernames)):
            f.write(f'{usernames[i]}:{passwords[i]}\n')
    log('Successfully generated output file')

except Exception as e:
    print(f"Error: {e}")
