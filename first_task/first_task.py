def fuel_mass(filepath: str) -> int:
    total_fuel = 0

    with open(filepath) as source_file:
        for line in source_file:
            try:
                current_fuel = int(line)
                total_fuel += (current_fuel // 3) - 2
            except ValueError as e:
                print(f'{line} cannot be converted to int, skipping this value. {e}')

    return total_fuel


def fuel_mass_advanced(filepath: str) -> int:
    total_fuel = 0

    with open(filepath) as source_file:
        for line in source_file:
            try:
                current_fuel = int(line)
                recursive_fuel = (current_fuel // 3) - 2
                while recursive_fuel > 0:
                    total_fuel += recursive_fuel
                    recursive_fuel = (recursive_fuel // 3) - 2
            except ValueError as e:
                print(f'{line} cannot be converted to int, skipping this value. {e}')

    return total_fuel


if __name__ == '__main__':
    print(f'Basic fuel requirement is {fuel_mass("input.txt")}')
    print(f'Advanced fuel requirement is {fuel_mass_advanced("input.txt")}')
