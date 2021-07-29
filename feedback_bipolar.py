feedback_bipolar1 = "Manie sau tulburare bipolara improbabila\nRaspunsurile la test sugereaza absenta simptomelor de tulburare bipolara sau depresie maniacala. \nSunt prezenta suisurile si coborasurile normale asociate unei vieti implinite."

feedback_bipolar2 = "Manie sau tulburare bipolara la limita\nRezultatul testului confirma prezenta unor simptome asociate in mod normal cu mania sau hipomania, \ninsa aceste simptome se regasesc si la restul oamenilor, in general. \nAceste simptome prezinta posibilitatea unor episoade maniacale si pot sa produca perturbari ale functionarii zilnice. \nCel mai probabil veti avea beneficii in urma unui diagnostic si a unui tratament specializat."

#Functie pentru atribuirea feedback-ului in functie de raspunsuri
def feedback_bipolar(score):
    if score <= 54:
        return feedback_bipolar1
    elif score > 54:
        return feedback_bipolar2