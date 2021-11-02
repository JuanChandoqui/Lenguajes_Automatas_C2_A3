import csv
import os

def writeCSVFile(isaceptable, curp):
        path_csv_valid = './Resources/Tables/curps_table_valid.csv'
        path_csv_invalid = './Resources/Tables/curps_table_invalid.csv'
        print(curp)
        if(os.path.exists(path_csv_valid)):
            print('FILE EXIST!')  
            if(isaceptable):
                with open(path_csv_valid, 'a+', newline='') as f:
                    writer = csv.writer(f)
                    row = [curp]
                    writer.writerow(row)
            else:
                with open(path_csv_invalid, 'a+', newline='') as f:
                    writer = csv.writer(f)
                    row = [curp]
                    writer.writerow(row)
        else:
            print('FILE NOT EXIST!')     
            if(isaceptable):
                header = ['ACCEPT']
                with open(path_csv_valid, 'w+', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    row = [curp]
                    writer.writerow(row)
            else:
                header = ['NOT ACCEPT']
                with open(path_csv_invalid, 'w+', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(header)
                    row = [curp]
                    writer.writerow(row)