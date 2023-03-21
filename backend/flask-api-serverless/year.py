#!/usr/bin/python3

import pandas as pd
def getYear(data, minYear, maxYear, num):
    """
    
    returns that songs within the years of minYear and maxYear
   
    Parameters:
    data (int): the dataset
    minYear (float): a value ranging from 1920 to maxYear
    maxYear (float): a value ranging from minYear to 2022
    num (int): the number of results to return
  
    Returns:
    list of dict: songs with the closest loudness level
    
    internals:
    reads the data and convert it to a panda Data Frame
    add a distances column 
    sort data frame by distances
    drop the distances column 
    return the top num songs in form of list of dict same structure as the mock_db
  
    """

    df = pd.DataFrame(data)
    df_actual = df[(df["year"].astype(int) >= int(minYear)) & (df["year"].astype(int) <= int(maxYear))]
    if len(df_actual) > 0:
        return df_actual[:num].to_dict('records')
    else:
        raise LookupError("No records found")
