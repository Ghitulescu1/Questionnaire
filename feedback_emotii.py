feedback_emotii1 = "Ai o atitudine sanatoasa fata de emotiile tale. Nu-ti este rusine sa iti arati din cand in cand emotiile, iar aceasta atitudine va contribui negresit la starea ta de sanatate. \nAi sanse sa fii un bun sfatuitor. "

feedback_emotii2 = "Iti exteriorizezi emotiile, insa nu atat de des pe cat ar trebui. Trebuie sa fii pregatit sa mergi mai departe. \nPlange atunci cand esti trist, tipa atunci cand esti furios si zambeste atunci cand esti fericit. \nExteriorizarea emotiilor poate face minuni pentru sanatatea ta fizica si psihica. "

#Functie pentru atribuirea feedback-ului in functie de raspunsuri
def feedback_emotii(score):
    if score <= 30:
        return feedback_emotii1
    elif score > 30:
        return feedback_emotii2