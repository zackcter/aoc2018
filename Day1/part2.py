"""Take a sequence of "Frequencies" (integers) as input and sum them up.
loop through the list given until you find the first repeat frequency.
They will be marked positive or negative."""

class Frequency_Store(object):
    def __init__(self):
        self.history = []
        self.current_cumsum = 0

    def increment(self, delta):
        self.current_cumsum += delta

    def repeat_check(self):
        if self.current_cumsum in self.history:
            return True
        else:
            return False

    def store(self):
        self.history.append(self.current_cumsum)

def process_sequence(filename, freqs):

    while True:
        with open(filename, 'r') as f:
            for line in f:
                freqs.increment(int(line.strip('+')))
                
                if freqs.repeat_check():
                    return freqs.current_cumsum

                freqs.store()

file_path = 'day1\\challenge_input.txt'

bucket = Frequency_Store()

print(process_sequence(file_path, bucket))