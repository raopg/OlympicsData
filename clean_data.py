# -*- coding : utf -8 -*-
import pandas as py
#First, we import the data from the csv file included
def clean_data(csv_filename = 'olympics.csv'):
    df = pd.read_csv(csv_filename, index_col = 0, skiprows=1)

    for col in df.columns():
        if col[:2] == '01':
            df.rename(columns={col:'Gold'+col[4:]}, inplace = True)
        if col[:2] == '02':
            df.rename(columns={col:'Silver'+col[4:]}, inplace = True)
        if col[:2] == '03':
            df.rename(columns={col:'Bronze'+col[4:]}, inplace = True)
        for e in col[:1]:
            if ord(e) > 128:
                df.rename(columns={col:'#'+col[1:]}, inplace = True)

    names_ids =  df.index.str.split('\s\(')

    df.index = names_ids.str[0]# The [0] element is the country name
    df['ID'] =  names_ids.str[1]# The [1] element is the abbreviation of the country

    print(df.head) # Print the first few elements to ensure that this data has been cleaned and is ready for use.
    return df 
    
if __name__ == "__main__":
    print("-------------------------------- \n")
    df = None
    print('This program cleans the Olympics data for all countries which has participated in Summer and Winter Olympics \n')
    filename = input('Enter the CSV file that needs to be cleaned, default is \'olympics.csv\' \n')
    if filename == '':
        clean_data()
    else:
        df = clean_data(filename)





    
    
