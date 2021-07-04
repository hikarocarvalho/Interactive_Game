from classes.player import Player
from classes.hunter import Hunter
# from classes.fantasma import Fantasma
# from classes.mercenario import Mercenario
# from classes.soldado import Soldier
# from classes.nephilim import Nephilim
#from classes.clock import Clock
from time import sleep
import os
def valid_choice(option):
    try:
        int(option)
        return True
    except:
        return False
def create_player(option):
    if option == 1:
        return Hunter()
    # elif play == 2:
    #     return Soldier()   
    # elif play == 3:
    #     return Mercenary()
    # elif play == 4:
    #     return Nephilim()
    # elif play == 5:
    #     return Ghost()
    else:
        return "Valor incorreto"
again = True
while again:
    player = Player()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(player.history0())
    choice = input("1 - Caçador. \n2 - Soldado. \n3 - Mercenário. \n4 - Nephilim. \n5 - Fantasma.\nEscolha um personagem: ")
    player.wait(3)
    if valid_choice(choice) == True:
        player = create_player(int(choice))
        sleep(5)
    else:
        continue
    sequence = list(["",1])
    valid = True
    while valid:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(player.sequence_History(sequence[1]))
        sleep(6)
        choice = input(player.sequence_choices(sequence[1]))
        if valid_choice(choice) == True:
            choice = int(choice)
            if sequence[1] == 1:
                sequence = list(player.choices_History1(choice))
            elif sequence[1] == 2:
                sequence = list(player.choices_History2(choice))
            elif sequence[1] == 3:
                sequence = list(player.choices_History3(choice))
            elif sequence[1] == 4:
                sequence = list(player.choices_History4(choice))
            elif sequence[1] == 5:
                sequence = list(player.choices_History5(choice))
            else:
                valid = False
        player.wait(6)
        if sequence[1]==6:
            print(player.history6())
            sleep(6)
            valid = False
            player.wait(3)   
        
    if input("Deseja jogar novamente?").strip(" ").lower().startswith("n"):
        again = False


