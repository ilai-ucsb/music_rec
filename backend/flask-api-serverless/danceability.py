import pandas as pd
def getDanceability(data, danceability_level, num_results):
    """
    
    returns that songs with the closest danceability level
   
    Parameters:
    data (int): the dataset
    danceability_level (float): a value ranging from 0 and 1
    num (int): the number of results to return
  
    Returns:
    list of dict: songs with the closest danceability_level 
    
    internals:
    reads the data and convert it to a panda Data Frame
    add a distances column 
    sort data frame by distances
    drop the distances column 
    return the top num songs in form of list of dict same structure as the mock_db
  
    """

    
    df = pd.DataFrame(data)
    df['distances'] = abs(df["danceability"] - energy_level)
    df.sort_values("distances", ascending=True,  inplace=True)
    idx = df.columns.get_loc("distances")
    df.drop(df.columns[idx], axis=1, inplace=True)
    df = df.head(num_results)
    
    return df.to_dict('records')
