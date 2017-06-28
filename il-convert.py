import csv
import logging

logging.basicConfig(level=logging.INFO)

group_slot_names = [
    ['legcor_1', 'legcor_2', 'legcor_3', 'legcor_4', 'legcor_5', 'legcor_6', 'legcor_7',
     'legcor_8', 'legcor_9', 'legcor_10', 'legcor_11', 'legcor_12', 'legcor_13', 'legcor_14',
     'legcor_15', 'legcor_16', 'legcor_17', 'legcor_18', 'legcor_19', 'legcor_20', 'legeco_1 ',
     'legeco_2', 'legeco_3', 'legeco_4', 'legeco_5', 'legeco_6', 'legeco_7', 'legeco_8',
     'legeco_9', 'legeco_10', 'legeco_11', 'legeco_12', 'legeco_13', 'legeco_14', 'legeco_15',
     'legeco_16', 'legeco_17', 'legeco_18', 'legeco_19', 'legeco_20', 'legeco_21', 'legeco_22',
     'legeco_23'],
    ['autcor_1', 'autcor_2', 'autcor_3', 'autcor_4', 'autcor_5', 'autcor_6', 'autcor_7', 'autcor_8',
     'autcor_9', 'autcor_10', 'autcor_11', 'autcor_12', 'autcor_13', 'autcor_14', 'autcor_15',
     'autcor_16', 'autcor_17', 'autcor_18', 'autcor_19', 'autcor_20', 'autcor_21', 'autcor_22',
     'autcor_23', 'autcor_24', 'autcor_25', 'autcor_26', 'autcor_27', 'autcor_28', 'autcor_29',
     'autcor_30', 'auteco_1', 'auteco_2', 'auteco_3', 'auteco_4', 'auteco_5', 'auteco_6', 'auteco_7',
     'auteco_8', 'auteco_9', 'auteco_10', 'auteco_11', 'auteco_12', 'auteco_13', 'auteco_14',
     'auteco_15', 'auteco_16', 'auteco_17', 'auteco_18', 'auteco_19', 'auteco_20', 'auteco_21'],
    ['Idecor_1', 'Idecor_2', 'Idecor_3', 'Idecor_4', 'Idecor_5', 'Idecor_6', 'Idecor_7', 'Idecor_8',
     'Idecor_9', 'Idecor_10', 'Idecor_11', 'Idecor_12', 'Idecor_13', 'Idecor_14', 'Idecor_15',
     'Ideeco_1', 'Ideeco_2', 'Ideeco_3', 'Ideeco_4', 'Ideeco_5', 'Ideeco_6', 'Ideeco_7', 'Ideeco_8',
     'Ideeco_9', 'Ideeco_10', 'Ideeco_11', 'Ideeco_12', 'Ideeco_13', 'Ideeco_14', 'Ideeco_15'],
    ['Norcor_1', 'Norcor_2', 'Norcor_3', 'Norcor_4', 'Norcor_5', 'Norcor_6', 'Norcor_7', 'Norcor_8', 'Norcor_9',
     'Norcor_10', 'Norcor_11', 'Norcor_12', 'Norcor_13', 'Norcor_14', 'Norcor_15', 'Norcor_16', 'Norcor_17',
     'Norcor_18', 'Norcor_19', 'Norcor_20', 'Norcor_21', 'Norcor_22', 'Norcor_23', 'Norcor_24', 'Norcor_25',
     'Norcor_26', 'Norcor_27', 'Norcor_28', 'Norcor_29', 'Norcor_30', 'Norcor_31', 'Norcor_32', 'Norcor_33',
     'Norcor_34', 'Norcor_35', 'Norcor_36', 'Norcor_37', 'Norcor_38', 'Norcor_39', 'Norcor_40', 'Norcor_41',
     'Norcor_42', 'Noreco_1', 'Noreco_2', 'Noreco_3', 'Noreco_4', 'Noreco_5', 'Noreco_6', 'Noreco_7', 'Noreco_8',
     'Noreco_9', 'Noreco_10', 'Noreco_11', 'Noreco_12', 'Noreco_13', 'Noreco_14', 'Noreco_15', 'Noreco_16', 'Noreco_17',
     'Noreco_18', 'Noreco_19', 'Noreco_20'],
    ['Attcor_1', 'Attcor_2', 'Attcor_3', 'Attcor_4', 'Attcor_5', 'Attcor_6', 'Attcor_7', 'Attcor_8',
     'Attcor_9', 'Attcor_10', 'Attcor_11', 'Attcor_12', 'Attcor_13', 'Attcor_14', 'Attcor_15',
     'Attcor_16', 'Attcor_17', 'Atteco_1', 'Atteco_2', 'Atteco_3', 'Atteco_4', 'Atteco_5', 'Atteco_6',
     'Atteco_7', 'Atteco_8', 'Atteco_9', 'Atteco_10', 'Atteco_11'],
    ['Strcor_1', 'Strcor_2', 'Strcor_3', 'Strcor_4', 'Strcor_5', 'Strcor_6', 'Strcor_7', 'Strcor_8',
     'Strcor_9', 'Strcor_10', 'Strcor_11', 'Strcor_12', 'Strcor_13', 'Strcor_14', 'Strcor_15',
     'Strcor_16', 'Strcor_17', 'Strcor_18', 'Strcor_19', 'Strcor_20', 'Strcor_21', 'Strcor_22',
     'Strcor_23', 'Strcor_24', 'Strcor_25', 'Strcor_26', 'Strcor_27', 'Strcor_28', 'Strcor_29',
     'Strcor_30', 'Strcor_31', 'Strcor_32', 'Streco_1', 'Streco_2', 'Streco_3', 'Streco_4', 'Streco_5',
     'Streco_6', 'Streco_7', 'Streco_8', 'Streco_9', 'Streco_10', 'Streco_11', 'Streco_12',
     'Streco_13', 'Streco_14', 'Streco_15', 'Streco_16', 'Streco_17', 'Streco_18', 'Streco_19',
     'Streco_20', 'Streco_21', 'Streco_22'],
    ['Inscor_1', 'Inscor_2', 'Inscor_3', 'Inscor_4', 'Inscor_5', 'Inscor_6', 'Inscor_7', 'Inscor_8',
     'Inscor_9', 'Inseco_1', 'Inseco_2', 'Inseco_3', 'Inseco_4', 'Inseco_5', 'Inseco_6', 'Inseco_7',
     'Inseco_8', 'Inseco_9'],
    ['Pricor_1', 'Pricor_2', 'Pricor_3', 'Pricor_4', 'Pricor_5', 'Pricor_6', 'Pricor_7', 'Pricor_8',
     'Pricor_9', 'Pricor_10', 'Pricor_11', 'Pricor_12', 'Pricor_13', 'Pricor_14', 'Pricor_15',
     'Pricor_16', 'Pricor_17', 'Pricor_18', 'Pricor_19', 'Prieco_1', 'Prieco_2', 'Prieco_3',
     'Prieco_4', 'Prieco_5', 'Prieco_6', 'Prieco_7', 'Prieco_8', 'Prieco_9', 'Prieco_10', 'Prieco_11',
     'Prieco_12', 'Prieco_13', 'Prieco_14']
]

filter_name = 'Sex'

group_slots = {'1': False, '2': False, '3': False, '4': False, '5': False, '6': False, '7': False, '8': False}
unfit_rows = []
currentSlot = 0
results = []
temp_row = {}

row_age_average = []
row_bdauer_average = []
row_mitarb_average = []
row_kennen_average = []
row_sem_average = []
bart_list = []
bbereich_list = []
branch_list = []
study_list = []
code_list = []
ids_list = []



def find_group(row):
    assigend_group = -1
    # falls NA in Endergebnis, dann alle group slots testen lassen
    if (len(row['legcor_1']) > 0) and (len(row['legeco_1 ']) > 0):
        logging.debug('Group 1')
        assigend_group = 0

    elif (len(row['autcor_1']) > 0) and (len(row['auteco_1']) > 0):
        logging.debug('Group 2')
        assigend_group = 1

    elif (len(row['Idecor_1']) > 0) and (len(row['Ideeco_1']) > 0):
        logging.debug('Group 3')
        assigend_group = 2

    elif (len(row['Norcor_1']) > 0) and (len(row['Noreco_1']) > 0):
        logging.debug('Group 4')
        assigend_group = 3

    elif (len(row['Attcor_1']) > 0) and (len(row['Atteco_1']) > 0):
        logging.debug('Group 5')
        assigend_group = 4

    elif (len(row['Strcor_1']) > 0) and (len(row['Streco_1']) > 0):
        logging.debug('Group 6')
        assigend_group = 5

    elif (len(row['Inscor_1']) > 0) and (len(row['Inseco_1']) > 0):
        logging.debug('Group 7')
        assigend_group = 6

    elif (len(row['Pricor_1']) > 0) and (len(row['Prieco_1']) > 0):
        logging.debug('Group 8')
        assigend_group = 7

    # Gruppe konnte nicht ermittelt werden
    else:
        logging.error('Gruppe nicht gefunden für Zeile: ' + str(row))

    # Gruppe stimmt nicht mit der zugewiesenen Gruppe überein
    if row['group'] != str(assigend_group + 1):
        logging.error('Fehler in Zeile: ' + str(row))

    return assigend_group


def try_to_fill_in(row, is_new):
    global currentSlot
    global results
    global unfit_rows
    global temp_row

    # # ID, bart, bbereich, branch, Study, Code mit | trennen
    #  mittelwert: bdauer, mitarb, kennen, age, Sem
    # matching über Sex
    assigend_group = find_group(row)
    if assigend_group == currentSlot:
        tmp_obj = {}
        for qItem in group_slot_names[currentSlot]:
            tmp_obj[qItem] = row[qItem]

        current_age = int(row['Age'])
        current_bdauer = int(row['bdauer'])
        current_mitarb = int(row['mitarb'])
        current_kennen = int(row['kennen'])
        current_sem = int(row['Sem'])
        bart_list.append(row['bart'])
        bbereich_list.append(row['bbereich'])
        branch_list.append(row['branch'])
        study_list.append(row['Study'])
        code_list.append(row['Code'])
        # print(row)
        # exit()
        ids_list.append(row['\ufeffID'])

        if current_age != 999:
            row_age_average.append(current_age)

        if current_bdauer != 999:
            row_bdauer_average.append(current_bdauer)

        if current_mitarb != 999:
            row_mitarb_average.append(current_mitarb)

        if current_kennen != 999:
            row_kennen_average.append(current_age)

        if current_sem != 999:
            row_sem_average.append(current_sem)

        tmp_obj['Sex'] = row['Sex']

        temp_row.update(tmp_obj)
        # print(currentSlot)
        currentSlot += 1
        if currentSlot == 8:
            finish_row()
        return True
    else:
        if is_new:
            unfit_rows.append(row)
        return False


def finish_row():
    global temp_row, currentSlot, results
    global row_age_average, row_bdauer_average, row_mitarb_average, row_kennen_average, row_sem_average
    global bart_list, bbereich_list,  branch_list, study_list, code_list, ids_list

    temp_row['age_avg'] = calc_average(row_age_average)
    temp_row['bdauer_avg'] = calc_average(row_bdauer_average)
    temp_row['mitarb_avg'] = calc_average(row_mitarb_average)
    temp_row['kennen_avg'] = calc_average(row_kennen_average)
    temp_row['sem_avg'] = calc_average(row_sem_average)

    temp_row['bart_a'] = bart_list
    temp_row['bbereich_a'] = bbereich_list
    temp_row['branch_a'] = branch_list
    temp_row['Study_a'] = study_list
    temp_row['code_a'] = code_list
    temp_row['IDs'] = ids_list

    results.append(temp_row)
    temp_row = {}
    currentSlot = 0
    row_age_average = []
    row_bdauer_average = []
    row_mitarb_average = []
    row_kennen_average = []
    row_sem_average = []
    bart_list = []
    bbereich_list = []
    branch_list = []
    study_list = []
    code_list = []
    ids_list = []


def calc_average(row_age_average):
    if (sum(row_age_average)) != 0:
        return str(sum(row_age_average) / float(len(row_age_average)))
    else:
        return 'NA'


def do_it():
    global temp_row
    female_rows = []
    male_rows = []
    with open('data-il.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';', quoting=csv.QUOTE_NONE)

        for row in reader:
            if row['Sex'] == '1':
                female_rows.append(row)
            elif row['Sex'] == '2':
                male_rows.append(row)
            elif row['Sex'] == '999':
                unfit_rows.append(row)

    fit_rows(female_rows)

    fit_rows(male_rows)

    print('Volle Reihen: ', len(results))
    print('Noch ungematched: ', len(unfit_rows))

    flat_list = []
    for sublist in group_slot_names:
        for item in sublist:
            flat_list.append(item)

    flat_list.append('Sex')
    flat_list.append('age_avg')
    flat_list.append('bdauer_avg')
    flat_list.append('sem_avg')
    flat_list.append('kennen_avg')
    flat_list.append('mitarb_avg')
    flat_list.append('Study_a')
    flat_list.append('branch_a')
    flat_list.append('bbereich_a')
    flat_list.append('bart_a')
    flat_list.append('code_a')
    flat_list.append('IDs')
    # print(flat_list)

    with open('data-output.csv', 'w') as csv_out:
        wr = csv.DictWriter(csv_out, delimiter=';', fieldnames=flat_list, dialect=csv.excel, quoting=csv.QUOTE_ALL, quotechar='"')
        wr.writeheader()
        for result in results:
            wr.writerow(result)


def fit_rows(given_rows):
    for row in given_rows:
        try_to_fill_in(row, True)
        for urow in unfit_rows:
            if try_to_fill_in(urow, False):
                unfit_rows.remove(urow)
    finish_row()


if __name__ == "__main__":
    do_it()
