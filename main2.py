from Classes import intrebari
import question_list

print("I. Pune verbele din paranteza la prezent continuu:\n\n")

raspunsuri_unu = [
        intrebari(question_list.prima_cerinta[0], "is reading"),
        intrebari(question_list.prima_cerinta[1], "is cooking"),
        intrebari(question_list.prima_cerinta[2], "is snowing"),
        intrebari(question_list.prima_cerinta[3], "is watching"),
        intrebari(question_list.prima_cerinta[4], "aren't playing"),
        intrebari(question_list.prima_cerinta[5], "is sleeping"),
        intrebari(question_list.prima_cerinta[6], "is playing"),
        intrebari(question_list.prima_cerinta[7], "is doing"),
        intrebari(question_list.prima_cerinta[8], "am going"),
        intrebari(question_list.prima_cerinta[9], "are swimming")
]

def cerinta_unu(raspunsuri_unu):
        punctaj_unu = 0
        for intrebari in raspunsuri_unu:
                raspuns = input(intrebari.intrebare)
                if raspuns == intrebari.raspuns:
                        punctaj_unu += 1

        print("Felicitari! Ai raspuns corect la " + str(punctaj_unu) + " din " + str(len(raspunsuri_unu)) + " intrebari!")

cerinta_unu(raspunsuri_unu)

print("\n\nII. Pune propozitiile urmatoare la forma negativa:\n")

raspunsuri_doi = [
        intrebari(question_list.cerinta_doi[0],"Mrs. Smith is not cooking now."),
        intrebari(question_list.cerinta_doi[1],"My grandmother is not working in the garden every day."),
        intrebari(question_list.cerinta_doi[2],"Jack is not getting a new camera next week."),
        intrebari(question_list.cerinta_doi[3],"The children are not having a shower now."),
        intrebari(question_list.cerinta_doi[4],"Jennie cannot speak Italian.")
]

def cerinta_doi(raspunsuri_doi):
        punctaj_doi = 0
        for intrebari in raspunsuri_doi:
                raspuns = input(intrebari.intrebare)
                if raspuns == intrebari.raspuns:
                        punctaj_doi += 2
        print(" Felicitari! Ai obtinut " + str(punctaj_doi) + " din " + str(len(raspunsuri_doi) * 2) + "!")
#erinta_doi(raspunsuri_doi)

print("Alege forma corecta: \n")

raspunsuri_trei = [
        intrebari(question_list.cerinta_trei[0],"mice"),
        intrebari(question_list.cerinta_trei[1],"teeth"),
        intrebari(question_list.cerinta_trei[2],"knives"),
        intrebari(question_list.cerinta_trei[3],"tomatoes"),
        intrebari(question_list.cerinta_trei[4],"wolves")
]

def cerinta_trei(raspunsuri_trei):
        punctaj_trei = 0
        for intrebari in raspunsuri_trei:
                raspuns = input(intrebari.intrebare)
                if raspuns == intrebari.raspuns:
                        punctaj_trei += 2
        print("Felicitari! Ai obtinut " + str(punctaj_trei) + " puncte din " + str(len(raspunsuri_trei) * 2) + "!")
cerinta_trei(raspunsuri_trei)
print("Corecteaza greselile:\n")
raspunsuri_patru = [
        intrebari(question_list.cerinta_patru[0], "There is a glass on the table."),
        intrebari(question_list.cerinta_patru[1], "I have got a tooth brush in the bathroom."),
        intrebari(question_list.cerinta_patru[2], "Jack and Jill are playing tennis."),
        intrebari(question_list.cerinta_patru[3], "Does your friend know English?"),
        intrebari(question_list.cerinta_patru[4], "My sister is a nice girl."),
]

def cerinta_patru(raspunsuri_patru):
        punctaj_patru = 0
        for intrebari in raspunsuri_patru:
                raspuns = input(intrebari.intrebare)
                if raspuns == intrebari.raspuns:
                        punctaj_patru += 2
        print("Felicitari! Ai obinut " + str(punctaj_patru) + " din " + str(len(raspunsuri_patru) * 2) + " puncte!")
cerinta_patru(raspunsuri_patru)


