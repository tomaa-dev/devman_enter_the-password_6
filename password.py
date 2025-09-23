def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not symbol.isalpha() and not symbol.isdigit() for symbol in password)


def main():
    lst_of_functions = [
        has_digit,
        is_very_long,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    
    password = input("Введите пароль: ")
    score = 0
    
    for function in lst_of_functions:
        if function(password):
            score += 2

    print("Рейтинг пароля:", score)


if __name__ == '__main__':
    main()