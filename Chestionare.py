


from typing import Sized
from PySimpleGUIQt.PySimpleGUIQt import ScrolledTextBox


shoud_be_open = True
while shoud_be_open:
    import PySimpleGUIQt as sg

    sg.theme('DarkBlue')

    layout = [
        [sg.Text('Selecteaza chestionarul')],
        [sg.Button('Test screening pentru depresie')],
        [sg.Button('Test screening pentru tulburare bipolara sau manie')],
        [sg.Button('Cat de vulnerabil esti la la stres?')],
        [sg.Button('Cum te simti in pielea ta')],
        [sg.Button('Testarea emotiilor')],
        [sg.Button('Test EQ - dur <-> sensibil')],
        [sg.Stretch(), sg.Exit('Inchide', size = (75, 35)), sg.Stretch()]
    ]

    layout_one = [
        [sg.Text('Cu ajutorul acestui test poti afla in ce masura simptomele de depresie fac parte din viata ta ')], 
        [sg.Text('si ce efecte au. Intrebarile de mai jos se refera la starea de spirit si comportamentul avut in')],
        [sg.Text('ultima saptamana.')],
        [sg.Text('')],
        [sg.Text('Rezultatele acestui test nu pot inlocui un diagnostic stabilit de catre medic. Consulta un ')],
        [sg.Text('specialist ori de cate ori ai sentimente depresive care te impiedica sa functionezi normal sau')],
        [sg.Text('iti creeaza stari de anxietate si ingrijorare.')],
        [sg.Text('')],
        [sg.Text('')],
        [sg.Text('1. Obisnuiesc sa fac lucrurile foarte incet.')],
        [sg.Radio('Deloc.', default = False, group_id= '1')],
        [sg.Radio('Putin.', default = False, group_id= '1')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '1')],
        [sg.Radio('Moderat.', default = False, group_id= '1')],
        [sg.Radio('Mult.', default = False, group_id= '1')],
        [sg.Radio('Foarte mult.', default = False, group_id= '1')],
        [sg.Text('2. Viitorul meu pare a fi lipsit de speranta.')],
        [sg.Radio('Deloc.', default = False, group_id= '2')],
        [sg.Radio('Putin.', default = False, group_id= '2')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '2')],
        [sg.Radio('Moderat.', default = False, group_id= '2')],
        [sg.Radio('Mult.', default = False, group_id= '2')],
        [sg.Radio('Foarte mult.', default = False, group_id= '2')],
        [sg.Text('3. Imi este greu sa ma concentrez atunci cand citesc.')],
        [sg.Radio('Deloc.', default = False, group_id= '3')],
        [sg.Radio('Putin.', default = False, group_id= '3')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '3')],
        [sg.Radio('Moderat.', default = False, group_id= '3')],
        [sg.Radio('Mult.', default = False, group_id= '3')],
        [sg.Radio('Foarte mult.', default = False, group_id= '3')],
        [sg.Text('4. Placerea si bucuria au disparut din viata mea.')],
        [sg.Radio('Deloc.', default = False, group_id= '4')],
        [sg.Radio('Putin.', default = False, group_id= '4')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '4')],
        [sg.Radio('Moderat.', default = False, group_id= '4')],
        [sg.Radio('Mult.', default = False, group_id= '4')],
        [sg.Radio('Foarte mult.', default = False, group_id= '4')],
        [sg.Text('5. Imi este greu sa iau decizii.')],
        [sg.Radio('Deloc.', default = False, group_id= '5')],
        [sg.Radio('Putin.', default = False, group_id= '5')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '5')],
        [sg.Radio('Moderat.', default = False, group_id= '5')],
        [sg.Radio('Mult.', default = False, group_id= '5')],
        [sg.Radio('Foarte mult.', default = False, group_id= '5')],
        [sg.Text('6. Mi-am pierdut interesul in lucrurile care imi placeau odata.')],
        [sg.Radio('Deloc.', default = False, group_id= '6')],
        [sg.Radio('Putin.', default = False, group_id= '6')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '6')],
        [sg.Radio('Moderat.', default = False, group_id= '6')],
        [sg.Radio('Mult.', default = False, group_id= '6')],
        [sg.Radio('Foarte mult.', default = False, group_id= '6')],
        [sg.Text('7. Ma simt trist si nefericit.')],
        [sg.Radio('Deloc.', default = False, group_id= '7')],
        [sg.Radio('Putin.', default = False, group_id= '7')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '7')],
        [sg.Radio('Moderat.', default = False, group_id= '7')],
        [sg.Radio('Mult.', default = False, group_id= '7')],
        [sg.Radio('Foarte mult.', default = False, group_id= '7')],
        [sg.Text('8. Sunt agitat si nu pot sta locului.')],
        [sg.Radio('Deloc.', default = False, group_id= '8')],
        [sg.Radio('Putin.', default = False, group_id= '8')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '8')],
        [sg.Radio('Moderat.', default = False, group_id= '8')],
        [sg.Radio('Mult.', default = False, group_id= '8')],
        [sg.Radio('Foarte mult.', default = False, group_id= '8')],
        [sg.Text('9. Ma simt obosit.')],
        [sg.Radio('Deloc.', default = False, group_id= '9')],
        [sg.Radio('Putin.', default = False, group_id= '9')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '9')],
        [sg.Radio('Moderat.', default = False, group_id= '9')],
        [sg.Radio('Mult.', default = False, group_id= '9')],
        [sg.Radio('Foarte mult.', default = False, group_id= '9')],
        [sg.Text('10. Este un efort pentru mine sa fac lucruri simple.')],
        [sg.Radio('Deloc.', default = False, group_id= '10')],
        [sg.Radio('Putin.', default = False, group_id= '10')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '10')],
        [sg.Radio('Moderat.', default = False, group_id= '10')],
        [sg.Radio('Mult.', default = False, group_id= '10')],
        [sg.Radio('Foarte mult.', default = False, group_id= '10')],
        [sg.Text('11. Ma simt vinovata si cred ca merit sa fiu pedepsit.')],
        [sg.Radio('Deloc.', default = False, group_id= '11')],
        [sg.Radio('Putin.', default = False, group_id= '11')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '11')],
        [sg.Radio('Moderat.', default = False, group_id= '11')],
        [sg.Radio('Mult.', default = False, group_id= '11')],
        [sg.Radio('Foarte mult.', default = False, group_id= '11')],
        [sg.Text('12. Ma simt ca un ratat.')],
        [sg.Radio('Deloc.', default = False, group_id= '12')],
        [sg.Radio('Putin.', default = False, group_id= '12')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '12')],
        [sg.Radio('Moderat.', default = False, group_id= '12')],
        [sg.Radio('Mult.', default = False, group_id= '12')],
        [sg.Radio('Foarte mult.', default = False, group_id= '12')],
        [sg.Text('13. Ma simt lipsit de viata - mai mult mort decat viu.')],
        [sg.Radio('Deloc.', default = False, group_id= '13')],
        [sg.Radio('Putin.', default = False, group_id= '13')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '13')],
        [sg.Radio('Moderat.', default = False, group_id= '13')],
        [sg.Radio('Mult.', default = False, group_id= '13')],
        [sg.Radio('Foarte mult.', default = False, group_id= '13')],
        [sg.Text('14. Am tulburari de somn - dorm prea putin, prea mult, sau ma trezesc deseori.')],
        [sg.Radio('Deloc.', default = False, group_id= '14')],
        [sg.Radio('Putin.', default = False, group_id= '14')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '14')],
        [sg.Radio('Moderat.', default = False, group_id= '14')],
        [sg.Radio('Mult.', default = False, group_id= '14')],
        [sg.Radio('Foarte mult.', default = False, group_id= '14')],
        [sg.Text('15. Ma gandesc la cum m-as putea sinucide.')],
        [sg.Radio('Deloc.', default = False, group_id= '15')],
        [sg.Radio('Putin.', default = False, group_id= '15')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '15')],
        [sg.Radio('Moderat.', default = False, group_id= '15')],
        [sg.Radio('Mult.', default = False, group_id= '15')],
        [sg.Radio('Foarte mult.', default = False, group_id= '15')],
        [sg.Text('16. Ma simt incatusat.')],
        [sg.Radio('Deloc.', default = False, group_id= '16')],
        [sg.Radio('Putin.', default = False, group_id= '16')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '16')],
        [sg.Radio('Moderat.', default = False, group_id= '16')],
        [sg.Radio('Mult.', default = False, group_id= '16')],
        [sg.Radio('Foarte mult.', default = False, group_id= '16')],
        [sg.Text('17. Ma simt deprimat chiar si atunci cand mi se intampla lucruri bune.')],
        [sg.Radio('Deloc.', default = False, group_id= '17')],
        [sg.Radio('Putin.', default = False, group_id= '17')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '17')],
        [sg.Radio('Moderat.', default = False, group_id= '17')],
        [sg.Radio('Mult.', default = False, group_id= '17')],
        [sg.Radio('Foarte mult.', default = False, group_id= '17')],
        [sg.Text('18. M-am ingrasat sau am slabit fara a tine o dieta speciala.')],
        [sg.Radio('Deloc.', default = False, group_id= '18')],
        [sg.Radio('Putin.', default = False, group_id= '18')],
        [sg.Radio('Intr-o oarecare masura.', default = False, group_id= '18')],
        [sg.Radio('Moderat.', default = False, group_id= '18')],
        [sg.Radio('Mult.', default = False, group_id= '18')],
        [sg.Radio('Foarte mult.', default = False, group_id= '18')]

    ]

    layout_two = [
        
    ]

    layout_three = [
        
    ]

    layout_four = [
        
    ]

    layout_five = [
        
    ]

    layout_six = [
        
    ]

    error_layout =  [
        [sg.Text('Nu ati completat toate campurile', justification = 'c')],
        [sg.Stretch(), sg.Exit('Inchide', size = (80, 35)), sg.Stretch()]
    ]


    window = sg.Window('Test screening pentru depresie').Layout([[sg.Column(layout_one, size = (800, 500), scrollable = True)], 
            [sg.Stretch(), sg.Button('Finalizeaza test', size = (150, 35)), sg.Stretch()]])
    #window = sg.Window('Chestionare', layout, size=(400, 380))
    error_window = sg.Window('Eroare!', error_layout, size=(265, 80), finalize=True)
    
    inputFile = None
    inputType = None
    folderPath = None
    valutaType = None

    while True:
        event, values = window.read()
        if event == 'Export':
            inputFile = str(values['input_file'])
            inputType = values['_LIST_']
            valutaType = values['_VALUTA_LIST_']
            folderPath = str(values['folder'])
            if inputFile and inputType and folderPath and valutaType:
                import os
                base = os.path.basename(inputFile)
                fileName = os.path.splitext(base)[0]
                filePath = os.path.join(folderPath, fileName + ".csv")
                check = os.path.isfile(filePath)
                if check == False:
                    try:
                        main(inputFile, filePath, inputType[0], valutaType[0])
                    except Exception as inst:
                        print(inst)
                    window.close()
                    break
                else:
                    check_file_window.UnHide()
                    while True:
                        event, values = check_file_window.read()
                        if event in (None, 'Inchide'):
                            break
                    check_file_window.Hide()
            else:
                error_window.UnHide()
                while True:
                    event, values = error_window.read()
                    if event in (None, 'Inchide'):
                        break
                error_window.Hide()
        elif event == sg.WIN_CLOSED or event == "Inchide":
            shoud_be_open = False
            break