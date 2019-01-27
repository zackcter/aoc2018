"""Read a list of strings. record the number of strings that have exactly 2 of any letter, and exactly 3 of any letter.
return a checksum that is the product of those two numbers.

part 2 is to return the letters in common between two strings that only differ by 1 letter in 1 place"""

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

    def find_adjecent(self):
        # runs through the inventory looking for two lines with exactly 1 character different in the same place.
        # compare first item to second - end of inventory, 2nd item to 3rd - end....
        # assume all items have the same length 

        match_list = []

        for idx1, item1 in enumerate(self.inventory): # outermost loop, picking a first string to compare
            for item2 in self.inventory[idx1+1:]: # second loop, picking second string to compare
                match_list = []

                for idx2, character in enumerate(item1):
                    if character == item2[idx2]:
                        match_list.append(character)
                
                if len(match_list) == len(item1)-1:
                    return ''.join(match_list)

        return 0


input_file = 'challenge_input_2.txt'

im = Inventory_manager()

im.populate_inv(input_file)

print(im.find_adjecent())