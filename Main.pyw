from intrebari_depresie import intrebari_depresie
from intrebari_bipolar import intrebari_bipolar
from intrebari_stres import intrebari_stres
from intrebari_emotii import intrebari_emotii
from intrebari_eq import intrebari_eq
from intrebari_cumtesimti import intrebari_cumtesimti

from feedback_depresie import feedback_depresie
from feedback_bipolar import feedback_bipolar
from feedback_stres import feedback_stres
from feedback_cumtesimti import feedback_cumtesimti
from feedback_emotii import feedback_emotii
from feedback_eq import feedback_eq

def compute_answers(values, key): #Functie pentru a calcula suma care va fi folosita pentru feedback
    answer_sum = 0 #Suma
    index = 1
    last_found = False

    # Ma uit dupa numarul de intrebari
    while not last_found:
        qvalue = key + "-" + str(index) + "-1"
        if qvalue in values.keys():
            print("found: " + str(index))
            index = index + 1
        else:
            last_found = True
        
    # Bucla pentru a trece prin intrebari si a adauga valoarea de la fiecare raspuns la suma
    for ind in range(1, index):
        rindex = 1
        last_found = False
        while not last_found:
            avalue = key + "-" + str(ind) + "-" + str(rindex)
            if avalue in values.keys():
                if values[avalue] == True:
                    answer_sum = answer_sum + rindex
                rindex += 1
            else:
                last_found = True
    return answer_sum

def check_all_answers(values, key): #Functie pentru a verifica daca a fost bifat raspunsul la fiecare intrebare
    index = 1
    last_found = False

    # Ma uit dupa numarul de intrebari
    while not last_found:
        qvalue = key + "-" + str(index) + "-1"
        if qvalue in values.keys():
            print("found: " + str(index))
            index = index + 1
        else:
            last_found = True
        
    # Bucla pentru a trece prin intrebari si a adauga valoarea de la fiecare raspuns la suma
    for ind in range(1, index):
        rindex = 1
        last_found = False
        at_least_one = False
        while not last_found:
            avalue = key + "-" + str(ind) + "-" + str(rindex)
            if avalue in values.keys():
                if values[avalue] == True:
                    at_least_one = True
                rindex += 1
            else:
                last_found = True
        if at_least_one == False:
            return False
    return True

should_be_open = True
while should_be_open:
    import PySimpleGUIQt as sg

    layout_depresie = [
        [sg.Text('Cu ajutorul acestui test poti afla in ce masura simptomele de depresie fac parte din viata ta ')], 
        [sg.Text('si ce efecte au. Intrebarile de mai jos se refera la starea de spirit si comportamentul avut in')],
        [sg.Text('ultima saptamana.\n')],
        [sg.Text('Rezultatele acestui test nu pot inlocui un diagnostic stabilit de catre medic. Consulta un ')],
        [sg.Text('specialist ori de cate ori ai sentimente depresive care te impiedica sa functionezi normal sau')],
        [sg.Text('iti creeaza stari de anxietate si ingrijorare.\n\n')],
    ]

    layout_bipolar = [
        [sg.Text('Testul screening pentru manie, tulburare bipolara sau depresie bipolara va ajuta sa va monitorizati')], 
        [sg.Text('starea de spirit si sa stabiliti daca puteti beneficia in urma unui diagnostic sau tratament de ')],
        [sg.Text('specialitate pentru aceasta afectiune. \n')],
        [sg.Text('Cele 18 intrebari de mai jos se refera la comportamentul avut in ultima saptamana. \n\n')],
    ]

    layout_stres = [
        [sg.Text('Legatura dintre stresul psihologic si afectiunile fizice a fost evidentiata in numeroase cercetari in ')], 
        [sg.Text('domeniu. In perioadele de stres multe boli se agraveaza, productivitatea scade, iar efectele negative ')],
        [sg.Text('ale instabilitatii emotionale devin tot mai pronuntate. Pentru a afla cat de vulnerabil esti in fata ')],
        [sg.Text('stresului, completeaza raspunsul la urmatoarele afirmatii:\n\n')]
    ]

    layout_cumtesimti = [
        [sg.Text('Cat de confortabil te simti in propriul corp? Iti apreciezi calitatile si in acelasi timp iti accepti ')], 
        [sg.Text('defectele? Ai o imagine reala despre tine insati? Acest test te va ajuta sa afli ce nivel de stima de')],
        [sg.Text('sine ai. \n \n')],
    ]

    layout_emotii = [
        [sg.Text('Testul emotiilor iti dezvaluie daca ai o atitudine sanatoasa vis-a-vis de propriile emotii.\n\n')],
    ]

    layout_eq = [
        [sg.Text('Desi simpla la prima vedere, apartenenta la unul din cele doua tipuri de temperament poate releva ')], 
        [sg.Text('cateva informatii interesante privind personalitatea ta. Alege raspunsurile care ti se potrivesc cel')],
        [sg.Text('mai bine si afla interpretarea noastra.\n\n')],
    ]

    
    #Bucla pentru adaugarea intrebarilor si raspunsurilor la layout
    index = 1
    for intrebari in intrebari_depresie: #Adauga intrebarea
        layout_depresie.append([sg.Text(intrebari["intrebare"])])
        index2 = 1
        for raspuns in intrebari["raspuns"]: #Adauga raspunsurile pentru fiecare intrebare
            layout_depresie.append([sg.Radio(raspuns, enable_events=True, default = False, group_id= index, key="dep-" + str(index) + "-" + str(index2))])
            index2 += 1
        index += 1
    
    #Bucla pentru adaugarea intrebarilor si raspunsurilor la layout
    index = 1
    for intrebari in intrebari_bipolar: #Adauga intrebarea
        layout_bipolar.append([sg.Text(intrebari["intrebare"])])
        index2 = 1
        for raspuns in intrebari["raspuns"]: #Adauga raspunsurile pentru fiecare intrebare
            layout_bipolar.append([sg.Radio(raspuns, enable_events=True, default = False, group_id= index, key="bip-" + str(index) + "-" + str(index2))])
            index2 += 1
        index += 1
    
    #Bucla pentru adaugarea intrebarilor si raspunsurilor la layout
    index = 1
    for intrebari in intrebari_stres: #Adauga intrebarea
        layout_stres.append([sg.Text(intrebari["intrebare"])])
        index2 = 1
        for raspuns in intrebari["raspuns"]: #Adauga raspunsurile pentru fiecare intrebare
            layout_stres.append([sg.Radio(raspuns, enable_events=True, default = False, group_id= index, key="stres-" + str(index) + "-" + str(index2))])
            index2 += 1
        index += 1

    #Bucla pentru adaugarea intrebarilor si raspunsurilor la layout
    index = 1
    for intrebari in intrebari_cumtesimti: #Adauga intrebarea
        layout_cumtesimti.append([sg.Text(intrebari["intrebare"])])
        index2 = 1
        for raspuns in intrebari["raspuns"]: #Adauga raspunsurile pentru fiecare intrebare
            layout_cumtesimti.append([sg.Radio(raspuns, enable_events=True, key="cumte-" + str(index) + "-" + str(index2), default = False, group_id= index)])
            index2 += 1
        index += 1

    #Bucla pentru adaugarea intrebarilor si raspunsurilor la layout
    index = 1
    for intrebari in intrebari_emotii: #Adauga intrebarea
        layout_emotii.append([sg.Text(intrebari["intrebare"])])
        index2 = 1
        for raspuns in intrebari["raspuns"]: #Adauga raspunsurile pentru fiecare intrebare
            layout_emotii.append([sg.Radio(raspuns, enable_events=True, default = False, group_id= index, key="emot-" + str(index) + "-" + str(index2))])
            index2 += 1
        index += 1

    #Bucla pentru adaugarea intrebarilor si raspunsurilor la layout
    index = 1
    for intrebari in intrebari_eq: #Adauga intrebarea
        layout_eq.append([sg.Text(intrebari["intrebare"])])
        index2 = 1
        for raspuns in intrebari["raspuns"]: #Adauga raspunsurile pentru fiecare intrebare
            layout_eq.append([sg.Radio(raspuns, enable_events=True, default = False, group_id= index, key="eq-" + str(index) + "-" + str(index2))])
            index2 += 1
        index += 1
    
    #Layout-ul pentru fereastra principala
    main_layout = [
        [sg.Text("Acest program vă pune la dispoziție o serie de teste psihologice.")],
        [sg.Text("Fiecare test este compus dintr-o listă de întrebari și o interpretare a \nrăspunsurilor dumneavoastra.\n")],
        [sg.Text('Selecteaza chestionarul\n', justification= "c")],
        [sg.Stretch(), sg.Button('Test screening pentru depresie', size= (260,35)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Test screening pentru tulburare bipolara sau manie', size= (410,35)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Cat de vulnerabil esti la la stres', size= (275,35)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Cum te simti in pielea ta', size= (210,35)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Testarea emotiilor', size= (165,35)), sg.Stretch()],
        [sg.Stretch(), sg.Button('Test EQ - dur <-> sensibil', size= (225,35)), sg.Stretch()],
        [sg.Text(' ')],
        [sg.Stretch(), sg.Exit('Inchide', size = (75, 35)), sg.Stretch()]
    ]

    main_window = sg.Window('Chestionare', main_layout, size=(400, 380)) #Creaza fereastra

    #Layout-ul pentru chestionarul Depresie
    depresie_layout = [
        [sg.Column(layout_depresie, size = (800, 500), scrollable = True)], 
        [sg.Stretch(), sg.Button('Finalizeaza test', size = (150, 35)), sg.Stretch()]
    ]
    
    #Layout-ul pentru chestionarul Bipolar
    bipolar_layout = [
        [sg.Column(layout_bipolar, size = (800, 500), scrollable = True)], 
        [sg.Stretch(), sg.Button('Finalizeaza test', size = (150, 35)), sg.Stretch()]
    ]

    #Layout-ul pentru chestionarul Stres
    stres_layout = [
        [sg.Column(layout_stres, size = (800, 500), scrollable = True)], 
        [sg.Stretch(), sg.Button('Finalizeaza test', size = (150, 35)), sg.Stretch()]
    ]

    #Layout-ul pentru chestionarul Cu te simti
    cumtesimti_layout = [
        [sg.Column(layout_cumtesimti, size = (800, 500), scrollable = True)], 
        [sg.Stretch(), sg.Button('Finalizeaza test', size = (150, 35)), sg.Stretch()]
    ]

    #Layout-ul pentru chestionarul Emotii
    emotii_layout = [
        [sg.Column(layout_emotii, size = (800, 500), scrollable = True)], 
        [sg.Stretch(), sg.Button('Finalizeaza test', size = (150, 35)), sg.Stretch()]
    ]

    #Layout-ul pentru chestionarul EQ
    eq_layout = [
        [sg.Column(layout_eq, size = (800, 500), scrollable = True)], 
        [sg.Stretch(), sg.Button('Finalizeaza test', size = (150, 35)), sg.Stretch()]
    ]

    #Layout-ul pentru fereastra de eroare
    error_layout =  [
        [sg.Text('Nu ati completat toate campurile', justification = 'c')],
        [sg.Stretch(), sg.Exit('Inchide', size = (80, 35)), sg.Stretch()]
    ]

    window_depresie = sg.Window('Test screening pentru depresie', depresie_layout , finalize= True) #Creaza fereastra
    window_depresie.Hide() #Ascunde fereastra

    window_bipolar = sg.Window('Test screening pentru tulburare bipolara sau manie', bipolar_layout , finalize= True) #Creaza fereastra
    window_bipolar.Hide() #Ascunde fereastra

    window_stres = sg.Window('Cat de vulnerabil esti la la stres', stres_layout , finalize= True) #Creaza fereastra
    window_stres.Hide() #Ascunde fereastra

    window_cumtesimti = sg.Window('Cum te simti in pielea ta', cumtesimti_layout , finalize= True) #Creaza fereastra
    window_cumtesimti.Hide() #Ascunde fereastra

    window_emotii = sg.Window('Testarea emotiilor', emotii_layout , finalize= True) #Creaza fereastra
    window_emotii.Hide() #Ascunde fereastra

    window_eq = sg.Window('Test EQ - dur <-> sensibil', eq_layout , finalize= True) #Creaza fereastra
    window_eq.Hide() #Ascunde fereastra

    error_window = sg.Window('Eroare!', error_layout, size=(265, 80), finalize= True) #Creaza fereastra
    error_window.Hide() #Ascunde fereastra

    #Hashtable folosit pentru evenimente
    new_list = {
        "Test screening pentru depresie": {
            "window": window_depresie,
            "id": "dep",
            "answer": feedback_depresie
        },
        "Test screening pentru tulburare bipolara sau manie": {
            "window": window_bipolar,
            "id": "bip",
            "answer": feedback_bipolar
        },
        "Cat de vulnerabil esti la la stres": {
            "window": window_stres,
            "id": "stres",
            "answer": feedback_stres
        },
        "Cum te simti in pielea ta": {
            "window": window_cumtesimti,
            "id": "cumte",
            "answer": feedback_cumtesimti
        },
        "Testarea emotiilor": {
            "window": window_emotii,
            "id": "emot",
            "answer": feedback_emotii
        },
        "Test EQ - dur <-> sensibil": {
            "window": window_eq,
            "id": "eq",
            "answer": feedback_eq
        }
    }

    while True:
        event, values = main_window.read()
        if event in new_list.keys():
            new_list[event]["window"].UnHide()
            while True:
                new_event, new_values = new_list[event]["window"].read()
                if new_event == "Finalizeaza test": #Eveniment pentru afisarea feedback-ului
                    answer_score = compute_answers(new_values, new_list[event]["id"])
                    is_all = check_all_answers(new_values, new_list[event]["id"])
                    if not is_all: #Afiseaza fereastra de eroare daca nu a fost completat unul sau mai multe raspunsuri
                        error_window.UnHide() #Afiseaza fereastra
                        while True:
                            error_event, error_values = error_window.read()
                            if error_event == sg.WIN_CLOSED or error_event == "Inchide":
                                error_window.Hide() #Ascunde fereastra
                                break
                        continue
                    message = new_list[event]["window"].Hide()
                    #Layout pentru fereastra de feedback
                    layout_feedback = [
                        [sg.Text("Interpretare:\n", justification= 'c')],
                    ]
                    layout_feedback.append([sg.Text(new_list[event]["answer"](answer_score), justification = 'c')]) #Adauga feedbackul
                    layout_feedback.append([sg.Stretch(), sg.Exit('Inchide', size = (80, 35)), sg.Stretch()]) #Adauga buton de inchidere
                    feedback_window = sg.Window('Feedback', layout_feedback , finalize= True) #Creaza fereastra
                    while True:
                            feed_event, feed_values = feedback_window.read()
                            if feed_event == sg.WIN_CLOSED or feed_event == "Inchide":
                                feedback_window.Close()
                                break
                    break
        elif event == sg.WIN_CLOSED or event == "Inchide": #Inchide programul
            should_be_open = False
            break