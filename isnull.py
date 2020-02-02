import pandas as pd
import os

def dropna(file_name):
    before = pd.read_csv(file_name, header = None)
    after = before.dropna()
    shape = after.shape

    find_csv = file_name.find(".csv")
    file_name_csv = file_name[:find_csv]

    if os.path.isfile(file_name_csv + ".txt") == False:
        f = open(file_name_csv + ".txt", 'w')
        f.close() 

    for i in range(shape[0]):
        title = after.iloc[i][1]
        title = title.replace("\n", "")
        title = title[:-2]
        
        if title[len(title)-1] not in ["!","?","."]:
            title = title + "."
        
        text = after.iloc[i][4]
        
        combine = title + text
        combine = combine.replace("\n","")
        
        combine = combine + "\n"

        f = open(file_name_csv + ".txt", mode = 'a', encoding = 'utf-8')
        f.write(combine)
        f.close()

dropna("samsung_galaxynote10.csv")