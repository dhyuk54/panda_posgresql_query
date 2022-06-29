from sqlite3 import DatabaseError
import numpy as np
import pandas as pd
import psycopg2 
import psycopg2.extras as extras
import sys
# Complete example of how to convert a csv to
# a pandas dataframe, and then to PostgreSQL
# Method: Bulk Insert using execute_values()
#------------------------------------------------------------------------------
# Author: Hyuk, June 2022

#Connection parameter
param_dic = {
    "host":"localhost",
    "database":"globaldata",
    "user":"myuser",
    "password":"PasswOrd"
}

def connect(param_dic):
    conn = None
    
    try:
        print("Connecting to the PostgreSql database...")
        conn = psycopg2.connect(**param_dic)
    except (Exception ,psycopg2.DatabaseError ) as error :
        print(error)
        sys.exit(1)
    print("Connection sucsessful")
    return conn

def excute_query(conn,query):
    """ Execute a single query """
    ret = 0
    # get DB current cursor 
    cursor = conn.cursor()
    try:
        # excute "select count(*) from MonthlyTemp" 
        cursor.excute(query)
        conn.commit()
    except (Exception,psycopg2.DatabaseError) as error:
        print("Error:%S" %error )
        conn.rollback()
        conn.close()
        return 1
    if 'select' in query.lower():
        ret = cursor.fetchall()
    cursor.close()
    return ret


def execute_values(conn,df,table):
    """
    Using psycopg2.extras.execute_values() to insert the dataframe
    """  
    tuples = [tuple(x) for x in df.to_numpy()]
    # join columns ex A,B,C,D
    cols = ''.join(list(df.columns))
    query = "INSERT INTO %s(%s) VALUES %%s" %(table,cols)
    cursor = conn.cursor()
    try:
        extras.execute_values(cursor,query,tuples)
        conn.commit()
    except (Exception ,psycopg2.DatabaseError ) as error:
        print("Error:%s" %error)
        conn.rollback()
        conn.close()
        return 1
    
    print("excute_values() done")
    cursor.close()
    
def read_dataframe(csv_file):
    df = df.read_csv(csv_file)
    df = df.rename(columns={
        "source":"source",
        "Date":"datetime",
        "Mean":"mean_temp"
    })
    return df 


def main():
    csv_file = "/data/bulk_insert_execute_values"
    df = read_dataframe(csv_file)
    print(df.hean(5))
    
    conn = connect(param_dic)
    execute_values(conn,df,'MonthlyTemp')
    n_rows = excute_query(conn,"select count(*) from MonthlyTemp")
    print("Number of rows in the table = %" %n_rows)
    
    excute_query(conn,"delete from MonthlyTemp where true;")
    
    conn.close()
    
if __name__ == "__main__":
    main()
       
    