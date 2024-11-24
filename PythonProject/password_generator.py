# password_generator/password_generator.py

import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_special):
    if length < 6 or length > 32:
        raise ValueError("Длина пароля должна быть от 6 до 32 символов.")

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Должен быть выбран хотя бы один набор символов.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
