password = input("Enter a password ")

def number_of_digits(password):
    numbers = 0
    for character in password:
        if "0"<= character <= "9":
            numbers += 1
    return numbers

def has_upper(password):
    for character in password:
        if character.isupper():
            return True

    return False

def has_lower(password):
    for character in password:
        if character.islower():
            return True

    return False

if len(password) >= 8 and number_of_digits(password)>0 and has_upper(password) and has_lower(password):
    print("Strong password")
    print(f"Number of digits is {number_of_digits(password)}")
else:
    print("Weak password")
