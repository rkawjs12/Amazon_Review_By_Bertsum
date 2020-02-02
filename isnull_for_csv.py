import pandas as pd
import os

def dropna(file_name):
    before = pd.read_csv(file_name, header = None)
    after = before.dropna()
    shape = after.shape

    find_csv = file_name.find(".csv")
    file_name_csv = file_name[:find_csv]

    list_for_contents = []

    for i in range(shape[0]):
        title = after.iloc[i][1]
        title = title.replace("\n", "")
        title = title[:-2]
        
        if title[len(title)-1] not in ["!","?","."]:
            title = title + "."
        
        text = after.iloc[i][4]
        
        combine = title + text
        combine = combine.replace("\n","")
        
        combine = combine
        list_for_contents.append(combine)

    dataframe_for_save = pd.DataFrame(data={'contents':list_for_contents})
    dataframe_for_save.to_csv(file_name + "_for_change.csv", mode = 'a', index = False)

dropna("amazon_echoshow.csv")