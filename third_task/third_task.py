from typing import Set, Tuple, List, Dict
import sys


def decide_next_instruction(current_instruction: Tuple[int, int], instruction_code: str) -> Tuple[int, int]:
    if instruction_code == 'U':
        current_instruction_y = current_instruction[1] + 1
        current_instruction = (current_instruction[0], current_instruction_y)
    elif instruction_code == 'D':
        current_instruction_y = current_instruction[1] - 1
        current_instruction = (current_instruction[0], current_instruction_y)
    elif instruction_code == 'R':
        current_instruction_x = current_instruction[0] + 1
        current_instruction = (current_instruction_x, current_instruction[1])
    elif instruction_code == 'L':
        current_instruction_x = current_instruction[0] - 1
        current_instruction = (current_instruction_x, current_instruction[1])
    else:
        raise ValueError("Unexpected instruction appeared, turn instruction")

    return current_instruction


def parse_wire_instruction(instruction: str, instruction_dict: Dict, current_instruction: Tuple[int, int],
                           current_step: int) -> Tuple[Dict, Tuple[int, int], int]:
    instruction_code = instruction[0]
    try:
        instruction_iterations = int(instruction[1:])
    except ValueError:
        raise ValueError("Unexpected instruction appeared, number instruction")

    for iterations in range(instruction_iterations):
        current_instruction = decide_next_instruction(current_instruction, instruction_code)
        current_step += 1
        if current_instruction not in instruction_dict:
            instruction_dict[current_instruction] = current_step

    return instruction_dict, current_instruction, current_step


def check_wire_intersections(first_wire_dict: Dict, intersection_dict: Dict, instructions_raw: List) -> Dict:
    current_instruction = (0, 0)
    current_step = 0

    for instruction in instructions_raw:
        instruction_code = instruction[0]
        try:
            instruction_iterations = int(instruction[1:])
        except ValueError:
            raise ValueError("Unexpected instruction appeared, number instruction")

        for iterations in range(instruction_iterations):
            current_instruction = decide_next_instruction(current_instruction, instruction_code)
            current_step += 1
            if current_instruction in first_wire_dict:
                intersection_dict[current_instruction] = current_step + first_wire_dict.get(current_instruction)

    return intersection_dict


def compute_first_wire_dict(filepath: str) -> Dict:
    first_wire_dict = dict()
    starting_position = (0, 0)
    current_step = 0

    with open(filepath) as instructions_file:
        instructions_raw = instructions_file.readline().split(",")
        for instruction in instructions_raw:
            first_wire_dict, starting_position, current_step = \
                parse_wire_instruction(instruction, first_wire_dict, starting_position, current_step)

    return first_wire_dict


def compute_intersections(filepath: str) -> Dict:

    intersections_dict = dict()
    first_wire_dict = compute_first_wire_dict(filepath)

    with open(filepath) as instructions_file:
        instructions_file.readline()  # skip first line
        instructions_raw = instructions_file.readline().split(",")
        intersections_dict = check_wire_intersections(first_wire_dict, intersections_dict, instructions_raw)

    return intersections_dict


def compute_closest_intersection_manhattan_distance(filepath: str) -> int:
    intersections_dict = compute_intersections(filepath)
    smallest_distance = sys.maxsize

    for intersection in intersections_dict.keys():
        if abs(intersection[0]) + abs(intersection[1]) < smallest_distance:
            smallest_distance = abs(intersection[0]) + abs(intersection[1])

    return smallest_distance


def compute_minimized_signal_delay(filepath: str) -> int:
    intersections_dict = compute_intersections(filepath)
    smallest_signal_delay = sys.maxsize
    for intersection in intersections_dict.values():
        if intersection < smallest_signal_delay:
            smallest_signal_delay = intersection

    return smallest_signal_delay


if __name__ == '__main__':
    print(f'Manhattan distance from central port to closest intersection is '
          f'{compute_closest_intersection_manhattan_distance("input.txt")}')
    print(f'Smallest signal distance is {compute_minimized_signal_delay("input.txt")}')
