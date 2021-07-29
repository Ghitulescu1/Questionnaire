feedback_eq1 = "Cuvinte cheie: pragmatic, energic, ferm.\nPotrivit scorului la acest test, esti - cel putin aparent - o persoana dura, insa este posibil ca dedesubt sa se ascunda o fire sensibila. \nIn cazul multor persoane aceasta aparenta dura ascunde ceea ce poate fi perceputa ca slabiciune.\nDesi nu pari a fi un romantic sau un sentimentalist, acest lucru nu te impiedica sa ai o relatie si o casnicie fericita si totodata nu inseamna ca persoanele care te accepta asa cum esti nu te pot admira sincer.\nEste important - nu doar pentru tine, ci si pentru cei din jur - \nsa iti amintesti mereu de sentimentele pe care le ai pentru ceilalti si sa le dovedesti ca tii la ei.\nDaca reusesti sa ai compasiune fata de ceilalti si sa le meriti respectul, inseamna ca detii calitatile unei persoane cu taria interioara necesara pentru a avea succes, atat in cariera, cat si in viata in general."

feedback_eq2 = "Cuvinte cheie: intelegator, ingrijorat, grijuliu.\nPari a fi o persoana buna, care niciodata nu ar rani cu intentie sentimentele cuiva.  Se poate insa ca aceste calitati ale tale sa fie mai putin evidente, deoarece te straduiesti sa le ascunzi.\n Avantajul este ca esti destul de dur pentru a-t iurma ambitiile, \nin timp ce pastrezi latura iubitoare a personalitatii tale.\nIn interactiunile cu oamenii dai dovada de tact, insa ocazional nu te poti abtine sa nu spui adevaruri care dor sau lucruri pe care le poti regreta mai tarziu. \nDin fericire pentru ceilalti, in general stii cand trebuie sa taci."

feedback_eq3 = "Cuvinte cheie: grijuliu, darnic, bun la inima, idealist, romantic.\nRezultatele testului indica faptul ca esti o persoana deosebit de sensibila la sentimentele celorlalti si esti deseori afectata de tragediile si necazurile celor de langa tine. \nAcest lucru inseamna totodata ca dai dovada de mult tact si diplomatie, fiind in stare de orice pentru a nu rani sentimentele altcuiva.\nFirea ta te impinge mereu sa ii ajuti pe cei aflati in suferinta, iar acest lucrute face respectat de catre apropiati. \nDin pacate exista si un dezavantaj: este posibil sa nu ai taria interioara necesara pentru a avea succes si cateodata iti este imposibil sa spui nu."


#Functie pentru atribuirea feedback-ului in functie de raspunsuri
def feedback_eq(score):
    if score < 75:
        return feedback_eq1
    elif (score >= 75) & (score < 100):
        return feedback_eq2
    elif score >= 100:
        return feedback_eq3