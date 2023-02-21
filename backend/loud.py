# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:21:26 2023

@author: Parssa Hafezi
"""

import pandas as pd
def getLoud(data, loud, num):
    """
    usage pass in the data in from of list of dictionaries
    pass in desired number of song and loud 
    get back song with closest absolute loudness
    
    
    internals:
    read the data and convert it to a panda Data Frame
    add a distances column 
    sort data frame by distances
    drop the distances columns 
    return the top num songs in form of list of dict same structure as the mock_db
    """
    
    df = pd.DataFrame(data)
    df['distances'] = abs(df["loudness"] - loud)
    df.sort_values("distances", ascending=True,  inplace=True)
    idx = df.columns.get_loc("distances")
    df.drop(df.columns[idx], axis=1, inplace=True)
    df = df.head(num)
    
    return df.to_dict('records')

