import csv
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

def readCSVCurps():
    with open('./Resources/curps_table_valid.csv', newline='') as csvfile:
        list_curps = []
        list_statistics_dates = []
        count_male = 0
        count_female = 0
        as_count = 0
        bs_count = 0
        bc_count = 0
        cs_count = 0
        cc_count = 0
        cm_count = 0
        ch_count = 0
        cl_count = 0
        df_count = 0
        dg_count = 0
        gt_count = 0
        gr_count = 0
        hg_count = 0
        jc_count = 0
        mn_count = 0
        mc_count = 0
        ms_count = 0
        nt_count = 0
        ne_count = 0
        nl_count = 0
        oc_count = 0
        pl_count = 0
        qt_count = 0
        qr_count = 0
        sl_count = 0
        sr_count = 0
        sp_count = 0
        tc_count = 0
        ts_count = 0
        tl_count = 0
        vz_count = 0
        yn_count = 0
        zs_count = 0

        sex_dict = dict()
        federal_entity = dict()

        with open('./Resources/curps_table_valid.csv', newline='') as csvfile:

            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                curp = ', '.join(row)
                list_curps.append(curp)

            list_curps.pop(0)

            for i in range(len(list_curps)):
                caracters_curp = list(list_curps[i])

                for i in range(len(caracters_curp)):                     
                    
                #----CALCULATE COUNT OF MENS AND FEMALES-------
                    if(i == 10):
                        if(caracters_curp[i] == 'H'):
                            count_male+=1
                            sex_dict['HOMBRE'] = count_male
                        else:
                            count_female+=1
                            sex_dict['MUJER'] = count_female

                    if(i == 11):
                        if(caracters_curp[i] == 'A' and caracters_curp[i+1] == 'S'):
                            as_count += 1
                            federal_entity['AGUASCALIENTES'] = as_count
                        
                        elif (caracters_curp[i] == 'B'):
                            if(caracters_curp[i+1] == 'C'):
                                bc_count += 1
                                federal_entity['BAJA CALIFORNIA'] = bc_count
                            elif(caracters_curp[i+1] == 'S'):
                                bs_count += 1
                                federal_entity['BAJA CALIFORNIA SUR'] = bc_count
                        
                        elif (caracters_curp[i] == 'C'):
                            if(caracters_curp[i+1] == 'C'):
                                cc_count += 1
                                federal_entity['CAMPECHE'] = cc_count
                            elif(caracters_curp[i+1] == 'L'):
                                cl_count += 1
                                federal_entity['COAHUILA'] = cl_count
                            elif(caracters_curp[i+1] == 'M'):
                                cm_count += 1
                                federal_entity['COLIMA'] = cm_count
                            elif(caracters_curp[i+1] == 'S'):
                                cs_count += 1
                                federal_entity['CHIAPAS'] = cs_count
                            elif(caracters_curp[i+1] == 'H'):
                                ch_count += 1
                                federal_entity['CHIHUAHUA'] = ch_count                        

                        elif (caracters_curp[i] == 'D'):
                            if(caracters_curp[i+1] == 'F'):
                                df_count += 1
                                federal_entity['DISTRITO FEDERAL'] = df_count
                            elif(caracters_curp[i+1] == 'G'):
                                dg_count += 1
                                federal_entity['DURANGO'] = dg_count
                        
                        elif(caracters_curp[i] == 'G'):
                            if(caracters_curp[i+1] == 'T'):
                                gt_count += 1
                                federal_entity['GUANAJUATO'] = gt_count
                            elif(caracters_curp[i+1] == 'R'):
                                gr_count += 1
                                federal_entity['GUERRERO'] = gr_count
                        
                        elif(caracters_curp[i] == 'H' and caracters_curp[i+1] == 'G'):
                            hg_count += 1
                            federal_entity['HIDALGO'] = hg_count
                        
                        elif(caracters_curp[i] == 'J' and caracters_curp[i+1] == 'C'):
                            jc_count += 1
                            federal_entity['JALISCO'] = jc_count

                        elif(caracters_curp[i] == 'M'):
                            if(caracters_curp[i+1] == 'C'):
                                mc_count += 1
                                federal_entity['MEXICO'] = mc_count
                            elif(caracters_curp[i+1] == 'N'):
                                mn_count += 1
                                federal_entity['MICHOACAN'] = mn_count
                            elif(caracters_curp[i+1] == 'S'):
                                ms_count += 1
                                federal_entity['MORELOS'] = ms_count
                        
                        elif(caracters_curp[i] == 'N'):
                            if(caracters_curp[i+1] == 'T'):
                                nt_count += 1
                                federal_entity['NAYARIT'] = nt_count
                            elif(caracters_curp[i+1] == 'L'):
                                nl_count += 1
                                federal_entity['NUEVO LEON'] = nl_count
                        
                        elif(caracters_curp[i] == 'O' and caracters_curp[i+1] == 'C'):
                            oc_count += 1
                            federal_entity['OAXACA'] = oc_count
                        
                        elif(caracters_curp[i] == 'P' and caracters_curp[i+1] == 'L'):
                            pl_count += 1
                            federal_entity['PUEBLA'] = pl_count
                        
                        elif(caracters_curp[i] == 'Q'):
                            if(caracters_curp[i+1] == 'T'):
                                qt_count += 1
                                federal_entity['QUERETARO'] = qt_count
                            elif(caracters_curp[i+1] == 'R'):
                                qr_count += 1
                                federal_entity['QUINTANA ROO'] = qr_count
                        
                        elif(caracters_curp[i] == 'S'):
                            if(caracters_curp[i+1] == 'P'):
                                sp_count += 1
                                federal_entity['SAN LUIS POTOSI'] = sp_count
                            elif(caracters_curp[i+1] == 'L'):
                                sl_count += 1
                                federal_entity['SINALOA'] = sl_count
                            elif(caracters_curp[i+1] == 'R'):
                                sr_count += 1
                                federal_entity['SONORA'] = sr_count

                        elif(caracters_curp[i] == 'T'):
                            if(caracters_curp[i+1] == 'C'):
                                tc_count += 1
                                federal_entity['TABASCO'] = tc_count
                            elif(caracters_curp[i+1] == 'S'):
                                ts_count += 1
                                federal_entity['TAMAULIPAS'] = ts_count
                            elif(caracters_curp[i+1] == 'L'):
                                tl_count += 1
                                federal_entity['TLAXCALA'] = tl_count

                        elif(caracters_curp[i] == 'V' and caracters_curp[i+1] == 'Z'):
                            vz_count += 1
                            federal_entity['VERACRUZ'] = vz_count
                        
                        elif(caracters_curp[i] == 'Y' and caracters_curp[i+1] == 'N'):
                            yn_count += 1
                            federal_entity['YUCATAN'] = yn_count

                        elif(caracters_curp[i] == 'Z' and caracters_curp[i+1] == 'S'):
                            zs_count += 1
                            federal_entity['ZACATECAS'] = zs_count

        dict_freq_mounth = Freq_mes(list_curps)
        dict_freq_age = Freq_edad(list_curps)

        list_statistics_dates.append(sex_dict)
        list_statistics_dates.append(federal_entity)
        list_statistics_dates.append(dict_freq_mounth)
        list_statistics_dates.append(dict_freq_age)

        return list_statistics_dates   
    
    
def Freq_mes(list_curp):
    lst = []
    for curp_item in list_curp:
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


def Freq_edad(list_curp):
    lst = []
    for curp_item in list_curp:
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
    
        
        
    
    
    
