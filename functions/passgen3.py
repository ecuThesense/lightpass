import string, secret

letters = string.ascii_letters + string.digits + '!@#$%^&*()'

while True:
    try:
        passw_type = int(input("Which type of Password do you want to create? (1)Nummeric (2)Phrase - "))

        if passw_type in [1,2]:
            break

        else:
            continue

    except ValueError: 
        print("Please enter a valid number.")


while True:
    try:
        passw_lenght = int(input("How big your password should be: "))

        if passw_lenght <= 0: 
            print("Please enter a number greater than 0.")
            continue

        break

    except ValueError: 
        print("Please enter a valid number.")

with open('words.txt') as f:
    if passw_type == 1: 
        passw = ''.join(secrets.choice(letters) for _ in range(passw_lenght))
    
    elif passw_type == 2:
        words = [word.strip() for word in f]
        passw = '-'.join(secrets.choice(words) for _ in range(passw_lenght))

    else:
        print("Wrong Type.")

print(passw)
