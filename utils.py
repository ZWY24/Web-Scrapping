import os
import pandas as pd

def load_question_ids():
    df_ids = pd.read_csv("all_data.csv")
    question_ids = df_ids[df_ids['id'].astype(int) <= 1000000000]['id'].astype(int).tolist()
    chunks = [question_ids[i:i + 216] for i in range(0, len(question_ids), 216)]
    return chunks

def save_to_csv(dataframe):
    if not os.path.isfile('zhihu_data.csv'):
        dataframe.to_csv('zhihu_data.csv', mode='w', index=False)
    else:
        dataframe.to_csv('zhihu_data.csv', mode='a', header=False, index=False)
