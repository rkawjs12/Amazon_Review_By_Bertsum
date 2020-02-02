import pandas as pd
import os

def divide_by_score(file_name):
    # file_name은 크롤링을 진행한 csv 파일이다.
    before = pd.read_csv(file_name, header = None)
    after = before.dropna()
    
    name = file_name
    find_csv = name.find(".csv")
    name = name[:find_csv]

    for i in range(5):
        divide_by_score_frame = after[after[0]==float(i+1)]
        make_sentence_by_score(divide_by_score_frame,i,name)    



def make_sentence_by_score(data_frame, i, name):
# data_frame은 데이터 프레임을 의미하며, i는 score -1을 의미한다. name은 파일의 이름을 의미한다.
    shape = data_frame.shape

    list_for_contents = []

    for j in range(shape[0]):
        title = data_frame.iloc[j][1]
        title = title.replace("\n", "")
        title = title[:-2]

        if title[len(title)-1] not in ["!","?","."]:
            title = title + "."

        text = data_frame.iloc[j][4]
        
        combine = title + text
        combine = combine.replace("\n","")
        list_for_contents.append(combine)

    dataframe_for_save = pd.DataFrame(data={'contents':list_for_contents})
    dataframe_for_save.to_csv(name + "_{}.csv".format(i + 1), mode = 'a', index = False)

divide_by_score("amazon_echoshow.csv")