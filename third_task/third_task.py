from typing import Set, Tuple, List
import sys


def parse_wire_instruction(instruction: str, instruction_set: Set, current_instruction: Tuple[int, int]) \
        -> Tuple[Set, Tuple[int, int]]:
    instruction_code = instruction[0]
    try:
        instruction_iterations = int(instruction[1:])
    except ValueError:
        raise ValueError("Unexpected instruction appeared, number instruction")

    if instruction_code == 'U':
        for iterations in range(instruction_iterations):  # changing Y coordinate
            current_instruction_y = current_instruction[1] + 1
            current_instruction = (current_instruction[0], current_instruction_y)
            instruction_set.add(current_instruction)
    elif instruction_code == 'D':
        for iterations in range(instruction_iterations):  # changing Y coordinate
            current_instruction_y = current_instruction[1] - 1
            current_instruction = (current_instruction[0], current_instruction_y)
            instruction_set.add(current_instruction)
    elif instruction_code == 'R':
        for iterations in range(instruction_iterations):  # changing Y coordinate
            current_instruction_x = current_instruction[0] + 1
            current_instruction = (current_instruction_x, current_instruction[1])
            instruction_set.add(current_instruction)
    elif instruction_code == 'L':
        for iterations in range(instruction_iterations):  # changing Y coordinate
            current_instruction_x = current_instruction[0] - 1
            current_instruction = (current_instruction_x, current_instruction[1])
            instruction_set.add(current_instruction)
    else:
        raise ValueError("Unexpected instruction appeared, turn instruction")

    return instruction_set, current_instruction


def check_wire_intersections(first_wire_set: Set, intersection_set: Set, instructions_raw: List) -> Set:
    current_instruction = (0, 0)

    for instruction in instructions_raw:
        instruction_code = instruction[0]
        try:
            instruction_iterations = int(instruction[1:])
        except ValueError:
            raise ValueError("Unexpected instruction appeared, number instruction")

        if instruction_code == 'U':
            for iterations in range(instruction_iterations):  # changing Y coordinate
                current_instruction_y = current_instruction[1] + 1
                current_instruction = (current_instruction[0], current_instruction_y)
                if current_instruction in first_wire_set:
                    intersection_set.add(current_instruction)
        elif instruction_code == 'D':
            for iterations in range(instruction_iterations):  # changing Y coordinate
                current_instruction_y = current_instruction[1] - 1
                current_instruction = (current_instruction[0], current_instruction_y)
                if current_instruction in first_wire_set:
                    intersection_set.add(current_instruction)
        elif instruction_code == 'R':
            for iterations in range(instruction_iterations):  # changing Y coordinate
                current_instruction_x = current_instruction[0] + 1
                current_instruction = (current_instruction_x, current_instruction[1])
                if current_instruction in first_wire_set:
                    intersection_set.add(current_instruction)
        elif instruction_code == 'L':
            for iterations in range(instruction_iterations):  # changing Y coordinate
                current_instruction_x = current_instruction[0] - 1
                current_instruction = (current_instruction_x, current_instruction[1])
                if current_instruction in first_wire_set:
                    intersection_set.add(current_instruction)
        else:
            raise ValueError("Unexpected instruction appeared, turn instruction")

    return intersection_set


def compute_first_wire_set(filepath: str) -> Set:
    first_wire_set = set()
    starting_position = (0, 0)

    with open(filepath) as instructions_file:
        instructions_raw = instructions_file.readline().split(",")
        for instruction in instructions_raw:
            first_wire_set, starting_position = parse_wire_instruction(instruction, first_wire_set, starting_position)

    return first_wire_set


def compute_intersections(filepath: str) -> Set:

    intersections_set = set()
    first_wire_set = compute_first_wire_set(filepath)

    with open(filepath) as instructions_file:
        instructions_file.readline()  # skip first line
        instructions_raw = instructions_file.readline().split(",")
        intersections_set = check_wire_intersections(first_wire_set, intersections_set, instructions_raw)

    return intersections_set


def compute_closest_intersection_manhattan_distance(filepath: str) -> int:
    intersections_set = compute_intersections(filepath)
    smallest_distance = sys.maxsize

    for intersection in intersections_set:
        if abs(intersection[0]) + abs(intersection[1]) < smallest_distance:
            smallest_distance = abs(intersection[0]) + abs(intersection[1])

    return smallest_distance


if __name__ == '__main__':
    print(f'Manhattan distance from central port to closest intersection is {compute_closest_intersection_manhattan_distance("input.txt")}')
