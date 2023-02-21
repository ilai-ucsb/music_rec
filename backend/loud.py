# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:21:26 2023

@author: Parssa Hafezi
"""

import pandas as pd
def getLoud(data, loud, num):
    df = pd.DataFrame(data)
    df['distances'] = abs(df["loudness"] - loud)
    df.sort_values("distances", ascending=True,  inplace=True)
    idx = df.columns.get_loc("distances")
    df.drop(df.columns[idx], axis=1, inplace=True)
    df = df.head(num)
    
    return df.to_dict('records')

