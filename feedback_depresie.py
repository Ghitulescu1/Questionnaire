feedback_depresie1 = "Depresie improbabila.\nPunctajul tau la acest test sugereaza faptul ca este putin probabil sa suferi de o tulburare depresiva in acest moment. \nSe pare ca treci prin momente mai bune si mai putin bune, obisnuite pentru o viata psihosociala normala."

feedback_depresie2 = "Posibil depresie usoara.\nPrezinti simptome depresive usoare, multe dintre acestea fiind in general prezente si la ceilalti oameni. \nNu este clar daca problemele pe care le aisunt suficient de grave pentru a necesita diagnostic si tratament specializat."

feedback_depresie3 = "Depresie moderata - severa.\nPrezinti simptome de depresie moderate pana la severe, asociate de obicei cu tulburarile depresive majore, cum ar fi distimiile sau tulburarile bipolare. \nSe pare ca aceste simptome sunt motivul pentru care activitatea ta zilnica este grav tulburata si nu reusesti sa functionezi ca o persoana normala. \nCel mai probabil vei avea multiple beneficii in urma unei terapii organizate de catre un medic psiholog sau \npsihiatru, acesta fiind singurul in masura sa stabileasca un diagnostic corect si un tratament "

feedback_depresie4 = "Depresie severa.\nPrezinti simptome severe de depresie, asociate de obicei cu tulburarile depresive majore, cum ar fi distimiile sau tulburarile bipolare. \nSe pare ca aceste simptome sunt motivul pentru care activitatea ta zilnica este grav tulburata si nu reusesti sa functionezi ca o persoana normala. \nCel mai probabil vei avea multiple beneficii in urma unei terapii organizate de catre un medic psiholog sau psihiatru, acesta fiind singurul \nin masura sa stabileasca un diagnostic corect si un tratament adecvat."

#Functie pentru atribuirea feedback-ului in functie de raspunsuri
def feedback_depresie(score):
    if score <= 18:
        return feedback_depresie1
    elif (score > 18) & (score < 33):
        return feedback_depresie2
    elif (score > 32) & (score < 55):
        return feedback_depresie3
    elif score > 54:
        return feedback_depresie4