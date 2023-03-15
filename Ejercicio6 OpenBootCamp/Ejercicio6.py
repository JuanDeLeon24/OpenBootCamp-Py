import random
import string

def generate_password():
    while True:
        password = input("Ingresa una contraseña entre 6 y 12 caracteres: ")
        if len(password) < 6 or len(password) > 12:
            print("La contraseña debe tener entre 6 y 12 caracteres.")
        else:
            break
    
    random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=32))
    password_dict = dict(zip(random.sample(range(len(random_string)), len(password)), password))
    final_password = ''.join([password_dict.get(i, random_char) for i, random_char in enumerate(random_string)])
    return final_password

print(generate_password())

