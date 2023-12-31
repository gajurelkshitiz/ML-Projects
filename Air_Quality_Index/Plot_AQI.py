from glob import glob
import pandas as pd
import matplotlib.pyplot as plt

def avg_data():
    filenames = glob('Data/AQI/*.csv')
    avg_list_for_all_years = []
    
    for f in filenames:
        temp_i = 0
        average = []
        
        for rows in pd.read_csv(f, chunksize=24):
            add_var = 0
            avg = 0.0
            data = []
            df = pd.DataFrame(data=rows)
            
            for index, row in df.iterrows():
                data.append(row['PM2.5'])  # Use square brackets to access column values
                
            for i in data:
                if isinstance(i, (float, int)):
                    add_var += i
                elif isinstance(i, str):
                    if i not in ('NoData', 'PwrFail', '---', 'InVld'):
                        temp = float(i)
                        add_var += temp
                        
            avg = add_var / 24
            temp_i += 1
            average.append(avg)
        
        avg_list_for_all_years.append(average)
    
    return avg_list_for_all_years


if __name__ == '__main__':
    lst_all_years = avg_data()
    print(lst_all_years)
    print(len(lst_all_years))
    print(len(lst_all_years[0]))
    print(len(lst_all_years[1]))
    print(len(lst_all_years[2]))
    print(len(lst_all_years[3]))
    print(len(lst_all_years[4]))
    print(len(lst_all_years[5]))

# a = 2013
# for i in lst_all_years:
#     print('Days in year {} are {}'.format(a, len(i)))
#     a += 1

# a = 2013
# for i in lst_all_years:
#     plt.plot(range(0,len(i)),i,label="{} data".format(a))
#     a +=1

# plt.legend()
# plt.show()