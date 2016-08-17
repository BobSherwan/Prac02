MIN_LENGTH = 4
MAX_LENGTH = 10
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]\<>?{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(len(password)) + " character password is valid: " + password)



def is_valid_password(password):

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    if len(password) <= MIN_LENGTH or len(password) >= MAX_LENGTH:
        return False

    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isnumeric():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0 or (count_special == 0 and SPECIAL_CHARS_REQUIRED):
        return False

    return True


main()