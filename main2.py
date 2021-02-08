from Classes import intrebari
import question_list

afisaje = [
        intrebari(1,question_list.list[0], "is reading"),
        intrebari(2,question_list.list[1], "is cooking"),
        intrebari(3,question_list.list[2], "is snowing"),
        intrebari(4,question_list.list[3], "is watching"),
        intrebari(5,question_list.list[4], "aren't playing"),
        intrebari(6,question_list.list[5], "is sleeping"),
        intrebari(7,question_list.list[6], "is playing"),
        intrebari(8,question_list.list[7], "is doing"),
        intrebari(9,question_list.list[8], "am going"),
        intrebari(10,question_list.list[9], "are swimming")
]

def incepe_testul(afisaje):
        punctaj = 0
        for intrebari in afisaje:
                raspuns = input(intrebari.intrebare)
                if raspuns == intrebari.raspuns:
                        punctaj += 1
        print("Felicitari! Ai raspuns corect la " + str(punctaj) + " din " + str(len(afisaje)) + " intrebari!" )

incepe_testul(afisaje)
