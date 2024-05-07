import secrets
import string

def generate_password(length=12, has_letters=True, has_digits=True, has_special_chars=True):
    selection_list = string.ascii_letters
    if has_digits:
        selection_list += string.digits
    if has_special_chars:
        selection_list += string.punctuation

    password = ''.join(secrets.choice(selection_list) for _ in range(length))
    return password

l=int(input("Enter a length for your password  "))
password = generate_password(l)
print("Generated password:", password)
