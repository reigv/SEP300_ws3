
# =============================================================================
# SEP300 - Workshop 03 - Task 3 (0.25 marks)
#
# Instructions:
#   Use the @property decorators to create controlled methods for getting and
#   setting attribute values in the Card class.
#
# Explanation:
#   The attributes are still name-mangled (private), but @property lets us
#   expose them in a controlled way:
#     - @property           -> the "getter", runs when you read power.name
#     - @name.setter        -> the "setter", runs when you write power.name = ...
#   So from outside, it looks like a normal attribute, but the class decides
#   how the value is read and changed.
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

taunt_up3 = Card3("Taunt up", " this card gives taunt attribue when use ")

print(taunt_up3.name)
print(taunt_up3.descrip)



taunt_up3.name = "Taunt up 2"
# taunt_up3.description = " this card gives taunt attribue when use 2"    #should be same name?
taunt_up3.descrip = " this card gives taunt attribue when use 2"


print(taunt_up3.name)
print(taunt_up3.descrip)


