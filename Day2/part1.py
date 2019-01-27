"""Read a list of strings. record the number of strings that have exactly 2 of any letter, and exactly 3 of any letter.
return a checksum that is the product of those two numbers."""

from collections import Counter

class Inventory_manager(object):
    def __init__(self):
        # initialize counters for tracking the number of strings that have exactly 2 or 3 of any letter
        self.two_letter_count = 0
        self.three_letter_count = 0
        self.inventory = []
        self.checksum = 0

    def populate_inv(self, filepath):
        # read strings from a file, store the number of strings that contain exactly 2 or 3 of a letter
        with open(filepath, 'r') as f:
            for line in f:
                self.inventory.append(line.strip('\n'))
                _line = Counter(line) # make a counter object of the string
                _line_dict = dict(_line.items()) # make a dictionary of the item, number pairs in the Counter object

                if 2 in _line_dict.values(): # add counter if 2 shows up in dictionary values
                    self.two_letter_count += 1
                
                if 3 in _line_dict.values(): # add counter if 3 shows up in dictionary values
                    self.three_letter_count += 1
        
        self.checksum = self.three_letter_count * self.two_letter_count
                
    

input_file = 'challenge_input_2.txt'

im = Inventory_manager()

im.populate_inv(input_file)

print(im.checksum)