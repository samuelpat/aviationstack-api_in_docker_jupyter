import pandas as pd
import os 
import psycopg2
from sqlalchemy import create_engine


def fetchData(file_name='data.csv'):
    df = pd.read_csv(file_name, index_col=0)
    return df


def insertIntoTable(): 
    """Insert a dataframe into the 'testdata' table in 'testfligoo' database.
    IMPORTANT: Replace if table exists is ENABLED. It means, every running is deleting previous stored data.
     
    Parameters: 
    has no parameters.

    Returns:
    dataFrame: return the data that is going to be stored in the database.

    """
    try:
        #Parameters for the connection. This should be in a external and secure source.
        engine = create_engine('postgresql://testfligoo:testfligoo@milindadatabase:5432/testfligoo')

        #search the transformed data csv file.
        df = fetchData()
        df.to_sql('testdata', con=engine, if_exists='replace', index=False)
        data = df
    except:
        print("ERROR SAVING DATA IN POSTGRES DB: An exception occurred trying saving the data in testdata table / testglifgoo db")

    return data   

def flow_loadApiData():
    data_inserted = insertIntoTable()
  
    #print for the logs.
    print('************************* FLIGHT DATA TO DB ***********************')
    print(data_inserted)
    print('*******************************************************************')

if __name__ == "__main__":
    flow_loadApiData()
    

    

