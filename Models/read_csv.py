import csv

with open('../Resources/curps_table_valid.csv', newline='') as csvfile:
    list_curps = []
    count_male = 0
    count_female = 0
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        curp = ', '.join(row)
        list_curps.append(curp)

    list_curps.pop(0)

    #----CALCULATE COUNT OF MENS AND FEMALES-------
    for i in range(len(list_curps)):
        caracters_curp = list(list_curps[i])

        for i in range(len(caracters_curp)):                     
            if(i == 10):
                if(caracters_curp[i] == 'H'):
                    count_male+=1
                else:
                    count_female+=1

    print('COUNT OF MALES: ', count_male)
    print('COUNT OF FEMALES: ', count_female)