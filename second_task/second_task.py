from typing import List


def prepare_instructions_array(filepath: str) -> List[int]:
    instructions = []

    # save instructions
    with open(filepath) as instructions_file:
        instructions_raw = instructions_file.readline().split(",")
        # retype instructions
        for position in range(len(instructions_raw)):
            instructions.append(int(instructions_raw[position]))

    return instructions


def program_alarm(instructions: List[int]) -> int:
    position = 0

    while position <= len(instructions):
        if instructions[position] == 1:
            instructions[instructions[position + 3]] = instructions[instructions[position + 1]] \
                                                       + instructions[instructions[position + 2]]
        elif instructions[position] == 2:
            instructions[instructions[position + 3]] = instructions[instructions[position + 1]] \
                                                       * instructions[instructions[position + 2]]
        elif instructions[position] == 99:
            return instructions[0]
        else:
            raise ValueError("Unexpected instruction appeared")
        position += 4


def find_noun_and_verb(filepath: str) -> (int, int):
    for noun in range(100):
        for verb in range(100):
            instructions = prepare_instructions_array(filepath)
            instructions[1] = noun
            instructions[2] = verb
            if program_alarm(instructions) == 19690720:
                return noun, verb


if __name__ == '__main__':
    print(f'Value at position 0 after halt is: {program_alarm(prepare_instructions_array("input.txt"))}')
    print(f'For output 19690720, value of noun and verb is: {find_noun_and_verb("input.txt")}')
    print(f'Finel result for second subtask is {100 * 59 + 36}')
