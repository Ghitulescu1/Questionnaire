feedback_stres1 = "Vulnerabilitatea scazuta la stres\nComportamentul tau iti permite sa fii mai putin vulnerabil la stres decat celelalte persoane. \nAstfel ar trebui sa fim cu totii, desi majoritatea nu suntem.\nRecomandari:\nContinua sa ai un stil de viata pozitiv, insa sa nu te crezi invincibil. Stresul pandeste la colt, asa ca fii pregatit."

feedback_stres2 = "Vulnerabilitatea moderata la stres\nUnele comportamente si interactiuni iti reduc capacitatea de a face fata factorilor de stres. \nAi putea fi predispus efectele negative ale stresului, precum surmenaj la serviciu, frustrare, furie, probleme in relatie.\nRecomandari:\nDesi esti mai putin vulnerabil decat ceilalti, exista cateva elemente din viata ta pe care le-ai putea schimba in bine. \nConcentreaza-te pe pastrarea comportamentului pozitiv si pe schimbarea celui care te face vulnerabil la stres."

feedback_stres3 = "Vulnerabilitatea ridicata la stres\nExista multe componente ale comportamentului tau si relatiilor cu ceilalti care iti reduc capacitatea de a rezista la stres. \nAi putea fi predispus efectele negative ale stresului, precum surmenaj la serviciu, frustrare, furie, probleme in relatie.\nRecomandari:\nDesi esti mai putin vulnerabil decat ceilalti, exista cateva elemente din viata ta pe care le-ai putea schimba in bine. Concentreaza-te pe pastrarea comportamentului pozitiv si pe schimbarea celui \ncare te face vulnerabil la stres."

feedback_stres4 = "Vulnerabilitatea extrema la stres\nCircumstantele din viata ta, modul in care interactionezi cu ceilalti si comportamentul pe care il ai, toate acestea au ca rezultat o capacitate foarte scazuta de a face fata stresului. \nDin aceasta cauza esti predispus la aparitia efectelor negative ale stresului si a afectiunilor fizice. \nRiscul surmenajului la locul de munca, frustrarii, furiei si dramatismului excesiv in viata ta este foarte ridicat.\nRecomandari:\nschimba ce poti din comportamentul tau si incearca sa reduci anxietatea si stresul din viata ta. "


#Functie pentru atribuirea feedback-ului in functie de raspunsuri
def feedback_stres(score):
    if score < 8:
        return feedback_stres1
    elif (score > 7) & (score < 16):
        return feedback_stres2
    elif (score > 15) & (score < 24):
        return feedback_stres3
    elif score > 23:
        return feedback_stres4