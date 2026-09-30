
# =============================================================================
# SEP300 - Workshop 03 - Task 2 (0.25 marks)
#
# Instructions:
#   Use name mangling to prevent an easy access to Card attributes from
#   outside of the class. After name mangling, you should see error messages
#   when attempting to access the Card attributes. You can test your code with
#   the same excerpt from Task 1.
#
#   Note: You should get error messages even when trying to match the
#   attribute names in the code excerpt to the new ones in your class.
#   For example, both print(kirby.name) and print(kirby.__name) should
#   result in errors.
#
# Explanation:
#   Adding two underscores in front of an attribute name (e.g. __name) makes
#   Python "mangle" it. Inside the class it is still written as self.__name,
#   but Python actually stores it as _Card__name. Because of that:
#     - kirby.name   -> error (no attribute called "name" anymore)
#     - kirby.__name -> error (outside the class, Python doesn't rename it,
#                               so it looks for "__name" and can't find it)
# =============================================================================

class Card2:
    # Constructor --init--

    def __init__(self, name, descrip):
        self.__name = name
        self.__descrip = descrip

    def display(self):
        print(self.__name)
        print(self.__descrip)

taunt_up2 = Card2("Taunt up", " this card gives taunt attribue when use ")
taunt_up2.display()

try: 
    print(taunt_up.name)
except AttributeError as err:
    print(f"Errorr: { err }")
try: 
    print(taunt_up.__name)
except AttributeError as err:
    print(f"Errorr: { err }")
try: 
    print(taunt_up._Card2.__name)
except AttributeError as err:
    print(f"Errorr: { err }")
try: 
    print(taunt_up._Card2__name)
except AttributeError as err:
    print(f"Errorr: { err }")
try: 
    print(taunt_up._Card2__descrip)
except AttributeError as err:
    print(f"Errorr: { err }")


