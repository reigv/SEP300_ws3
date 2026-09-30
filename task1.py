
# =============================================================================
# SEP300 - Workshop 03 - Task 1 (0.50 marks)
#
# Instructions:
#   Write a class called Card with the following attributes and methods:
#     - An attribute called name
#     - Another attribute called description
#     - A constructor that initializes objects of this class with the
#       appropriate attributes
#     - A method called display that prints both the name, as well as the
#       description of the card
# =============================================================================

class Card:
    # Constructor --init--

    def __init__(self, name, descrip):
        self.name = name
        self.descrip = descrip

    def display(self):
        print(self.name)
        print(self.descrip)


taunt_up = Card("Taunt up", " this card gives taunt attribue when use ")
taunt_up.display()

try:
    print(taunt_up.name)
except AttributeError as er1:
    print(er1)
try:
    print(taunt_up.descrip)
except AttributeError as er1:
    print(er1)
