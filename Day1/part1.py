"""Take a sequence of numbers as input and sum them up.
They will be marked positive or negative."""

def process_sequence(filename):

    partial_sum = 0
    _entry = 0

    with open(filename, 'r') as f:
        for line in f:
            partial_sum += int(line.strip('+'))

    return partial_sum


file_path = 'challenge_input_2.txt'

print(process_sequence(file_path))
