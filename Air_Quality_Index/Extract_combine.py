from Plot_AQI import avg_data
from bs4 import BeautifulSoup
import pandas as pd
import glob
import os
import csv
import sys


def met_data(month, year):
    file_html = open('Data\Html_Data\{}\{}.html'.format(year, month), 'rb')
    plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, 'lxml')

    for table in soup.find_all('table', {'class':'medias mensuales numspan'}):
        for tbody in table:
            for tr in tbody:
                a = tr.get_text()
                tempD.append(a)

    rows = len(tempD)/15
    #just for visualizing:
    # print(tempD)
    # print(rows)

    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)
    
    # print(finalD)
    
    length = len(finalD)

    finalD.pop(length - 1)
    finalD.pop(0)


    for row in finalD:
        row.pop(0)
        row.pop(3)
        row.pop(4)
        row.pop(7)
        row.pop(7)
        row.pop(7)
        row.pop(7)
        row.pop(7)

    return finalD


def data_combine():
    csv_files_pattern = 'Data/Real_data/Real_*.csv'
    csv_files = glob.glob(csv_files_pattern)
    dfs = []
    for file in csv_files:
        df = pd.read_csv(file, skiprows=1, header=None)  # Specify header=None to ignore the existing header
        dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.to_csv('Data/Real_combined_file.csv', index=False, header=['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM 2.5'])

if __name__ == "__main__":
    if not os.path.exists("Data/Real_data"):
        os.makedirs("Data/Real_data")

    pm = getattr(sys.modules[__name__], 'avg_data')()
    # print(len(pm))
    # print(type(pm))
    a = 0  #for year 2013 i.e. pm[0] 
    for year in range(2013, 2019):
        final_data = []
        temp_pm = []

        temp_pm.extend(pm[a])
        # print(temp_pm)
        # print(type(temp_pm))
        a = a + 1

        if len(temp_pm) == 364:
            temp_pm.insert(364, '-')
        
        # print("Pm:")
        # print(len(temp_pm))

        for month in range(1,13):
            temp = met_data(month, year)
            final_data = final_data + temp

            if len(final_data) == 366:
                final_data = final_data[:-1]

        for i in range(len(final_data) - 1):
            final_data[i].insert(7, temp_pm[i])

        
        with open("Data/Real_data/Real_" + str(year) + ".csv", 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(['T', 'TM', 'Tm', 'H', 'VV', 'V', 'VM', 'PM 2.5'])

            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                
                if flag != 1:
                    wr.writerow(row)



    data_combine()
        



