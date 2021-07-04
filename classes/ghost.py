from classes.player import Player
class Ghost(Player):
    def __init__(self,part1="",part2="",part3="",part4="",part5="",part6="",choice1="",choice2="",choice3="",choice4="",choice5=""):
        part1 = """
           """
        part2 = """
            """
        part3 = """
            """
        part4 = """
           """
        part5 = """
            """
        part6 = """
            """
        
        choice1 = "\n"
        choice2 = ""
        choice3 = ""
        choice4 = ""
        choice5 = ""
        super().__init__(part1,part2,part3,part4,part5,part6,choice1,choice2,choice3,choice4,choice5)
    def __str__(self):
        return ""
    def choices_History1(self,choice):
        try:
            int(choice)

            if choice == 1:
                choice = list()
                choice.extend(["",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",2])
                return choice
            else:
                choice = list()
                choice.extend(["",3])
                return choice
        except:
            return self
    def choices_History2(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",6])
                return choice
            else:
                choice = list()
                choice.extend(["",3])
                return choice
        except:
            return self
    def choices_History3(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["",4])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",6])
                return choice
            else:
                choice = list()
                choice.extend(["",6])
                return choice
        except:
            return self
    def choices_History4(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",5])
                return choice
            else:
                choice = list()
                choice.extend(["",6])
                return choice
        except:
            return self
    def choices_History5(self,choice):
        try:
            int(choice)
            if choice == 1:
                choice = list()
                choice.extend(["",6])
                return choice
            elif choice == 2:
                choice = list()
                choice.extend(["",6])
                return choice
            else:
                choice = list()
                choice.extend(["",6])
                return choice
        except:
            return self
  