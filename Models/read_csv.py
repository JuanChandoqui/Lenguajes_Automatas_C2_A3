import csv
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

with open('./Resources/curps_table_valid.csv', newline='') as csvfile:
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
    
    
    
    
    
    
def Freq_mes():
    lst = []
    for curp_item in list_curps:
        lst.append(int(curp_item[6:8]))
    lst.sort()
    result = {}
    for item in lst :
        mes = calendar.month_name[item]
        if mes not in result.keys():
            result[mes] = 1
        else:
            print(result[mes])
            result[mes] += 1
    return result        


def Freq_edad():
    lst = []
    for curp_item in list_curps:
        lst.append(""+str(curp_item[8:10])+"/"+str(curp_item[6:8])+"/20"+str(curp_item[4:6]))
    lst.sort()
    result = {}
    for item in lst :
        fecha_nacimiento = datetime.strptime(item, "%d/%m/%Y")
        edad = relativedelta(datetime.now(), fecha_nacimiento)
        if str(edad.years) not in result.keys():
            result[str(edad.years)] = 1
        else:
            result[str(edad.years)] += 1
    return result  
        

print(Freq_mes())
print(Freq_edad())
    
        
    
    
    