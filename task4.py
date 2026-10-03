
# =============================================================================
# SEP300 - Workshop 03 - Task 4 (0.50 marks)
#
# Instructions:
#   Create two new classes, called Monster, and Item, that inherit from the
#   Card class and introduce the following new attributes and methods:
#
#   Monster
#     - An attribute called lives to store an integer
#     - An attribute called attack that describes the monster attack
#     - A constructor that initializes objects of this class with the
#       appropriate attributes
#     - A new display function that overrides the Card display function and
#       prints all attributes of the monster
#     - Getters and setters for these two new attributes
#
#   Item
#     - An attribute called factor to store an integer
#     - A constructor that initializes objects of this class with the
#       appropriate attributes
#     - A new display function that overrides the Card display function and
#       prints all attributes of the item
#     - Getters and setters for this new attribute
#
# Explanation:
#   - Monster(Card) / Item(Card) means they inherit everything from Card.
#   - super().__init__(name, description) calls Card's constructor so the
#     name and description are set up by the parent class.
#   - The child classes can't use self.__name directly, because Card's
#     private attribute is stored as _Card__name. Instead, they use the
#     public properties self.name and self.description from Task 3.
# =============================================================================

class Card3:
    # Constructor --init--

    def __init__(self, name, descrip):
        self.__name = name
        self.__descrip = descrip

    @property
    def name(self):
        return self.__name

    @property
    def descrip(self):
        return self.__descrip


    @name.setter
    def name(self, new_n):
        self.__name= new_n

        return print("new name")

    @descrip.setter
    def descrip(self, new_d):
        self.__descrip = new_d
        return print("new desciption")


    def display(self):
        print(self.__name)
        print(self.__descrip)


class Monster(Card3): 
    def __init__(self, name, descrip, lives, attack):
        super().__init__(name, descrip)
        self.__lives = lives
        self.__attack = attack

    @property
    def lives(self):
        return self.__lives

    @property
    def attack(self):
        return self.__attack

    @lives.setter
    def lives(self, update_lives):
        if isinstance(update_lives, int) and update_lives >= 0: # checking is int isinstance && live >=0 
            self.__lives = update_lives
            return 1
        else:
            return 0

    @attack.setter
    def attack(self, update_attack):
        self.__attack = update_attack  # can be less than 0
        return 1

    def display(self):
        super().display()
        print(self.__lives) # could add some text
        print(self.__attack)


cycllog = Monster("Cycllog", " this card gives taunt attribue when use ", 5, 10)
cycllog.display()

class Item(Card3):
    def __init__(self, name, descrip, factor):
        super().__init__(name, descrip)
        self.__factor = factor

    @property
    def factor(self):
        return self.__factor

    @factor.setter
    def factor(self, set_factor):
        self.factor = int(set_factor)
        return 1

    def display(self):
        super().display()
        print(self.__factor)

health_potion = Item("Health Potion", " this card gives health when use ", 5)
health_potion.display()




