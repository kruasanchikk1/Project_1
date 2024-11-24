# password_generator/main.py

from password_generator import generate_password
import sys


def main():
    length = int(input("Введите длину пароля (6-32): "))
    include_upper = input("Включить заглавные буквы? (yes/no): ").lower() == 'yes'
    include_lower = input("Включить строчные буквы? (yes/no): ").lower() == 'yes'
    include_digits = input("Включить цифры? (yes/no): ").lower() == 'yes'
    include_special = input("Включить специальные символы? (yes/no): ").lower() == 'yes'

    password = generate_password(length, include_upper, include_lower, include_digits, include_special)
    print(f"Сгенерированный пароль: {password}")


if __name__ == "__main__":
    main()
