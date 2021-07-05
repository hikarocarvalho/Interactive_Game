from time import sleep
import os
class Player:
    def __init__(self,part1="",part2="",part3="",part4="",part5="",part6="",choice1="",choice2="",choice3="",choice4="",choice5=""):
        #here are all historys parts
        #aqui estão todas as partes das histórias
        self._part0_history = """
            ###################
            #       ####      #
            ###   ########  ###
            ###   ########  ###
            ###   ########  ###
            ###.  .######. ####
            #####:       !#####
            ################ma guerra sovietica iniciou-se durante um período de fome
                            e miséria nos paises de Tadjiquistão e quirguistão pois os
                            mesmos sofriam com saquiamentos continuos por saqueadores
                            dos paises bálticos, o que pode -se levar como o estopin da
                            guerra em questão. Uma guerra que permeou pelo tempo até os
                            dias de hoje."""
        self._part1_history = part1
        self._part2_history = part2
        self._part3_history = part3
        self._part4_history = part4
        self._part5_history = part5
        self._part6_history = part6
        # here are all choices
        # aqui estão as escolhas
        self._choice1 = choice1
        self._choice2 = choice2
        self._choice3 = choice3
        self._choice4 = choice4
        self._choice5 = choice5

    def __str__(self):
        return "Valor incorreto!!"
        #wait method
    def wait(self,timewait):
        waiting = ""
        for i in range(timewait):    
            waiting += "● "
            print(waiting)
            sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
    def sequence_History(self,sequence):
        try:
            int(sequence)
            historys = list([self._part1_history,self._part2_history,self._part3_history,self._part4_history,self._part5_history,self._part6_history])
            historys = historys[sequence-1]
            return historys
        except:
            return self
    def sequence_choices(self,sequence):
        try:
            int(sequence)
            choices = list([self._choice1,self._choice2,self._choice3,self._choice4,self._choice5])
            choices = choices[sequence-1]
            return choices
        except:
            return self
    @property
    def history0(self):
        return self._part0_history
    @property
    def history6(self):
        return self._part6_history