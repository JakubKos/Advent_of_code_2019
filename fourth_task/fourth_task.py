

def is_non_decreasing(number: int) -> bool:
    string_representation = str(number)
    if string_representation[0] <= string_representation[1] <= string_representation[2] <= string_representation[3] \
            <= string_representation[4] <= string_representation[5]:
        return True

    return False


def has_same_adjacent_digits(number: int) -> bool:
    string_representation = str(number)
    if string_representation[0] == string_representation[1] or string_representation[1] == string_representation[2] or \
       string_representation[2] == string_representation[3] or string_representation[3] == string_representation[4] or \
       string_representation[4] == string_representation[5]:
        return True

    return False


def has_same_adjacent_digits_advanced(number: int) -> bool:
    string_representation = str(number)
    if (string_representation[0] == string_representation[1] and string_representation[1] != string_representation[2]) or \
       (string_representation[1] == string_representation[2] and string_representation[2] != string_representation[3]
        and string_representation[2] != string_representation[0]) or \
       (string_representation[2] == string_representation[3] and string_representation[3] != string_representation[4]
        and string_representation[3] != string_representation[1]) or \
       (string_representation[3] == string_representation[4] and string_representation[4] != string_representation[5]
        and string_representation[4] != string_representation[2]) or \
       (string_representation[4] == string_representation[5] and string_representation[5] != string_representation[3]):
        return True

    return False


def is_potential_password(number: int) -> bool:
    if is_non_decreasing(number) and has_same_adjacent_digits(number):
        return True

    return False


def is_potential_advanced_password(number: int) -> bool:
    if is_non_decreasing(number) and has_same_adjacent_digits_advanced(number):
        return True

    return False


def count_potential_passwords(from_number: int, to_number: int) -> int:
    total = 0
    for number in range(from_number, to_number):
        if is_potential_password(number):
            total += 1

    return total


def count_potential_advanced_passwords(from_number: int, to_number: int) -> int:
    total = 0
    for number in range(from_number, to_number):
        if is_potential_advanced_password(number):
            total += 1

    return total


if __name__ == '__main__':
    print(f'There are {count_potential_passwords(172930, 683082)} potential passwords in  range <172930, 683082>')
    print(f'There are {count_potential_advanced_passwords(172930, 683082)} potential advanced passwords in  range <172930, 683082>')
