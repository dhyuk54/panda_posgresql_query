import numpy as np
import pandas as pd
import psycopg2
import sys

def connect(param_dic):
    conn = None
    try:
        print("Connecting to the PostgreSql database...")
        conn = psycopg2.connect(**param_dic)
        
    except(Exception,psycopg2.DatabaseError) as error:
        print("Error:%s" %error)
        sys.exit(1)
    return conn

def single_insert(conn,insert_req):
    cursor = conn.cursor()
    try:
        cursor.execute(insert_req)
        conn.commit()
    except (Exception,psycopg2.DatabaseErro) as error:
        print("Error:%s" %error)
        conn.rollback()
        conn.close()
        return 1
    cursor.close()
    
def main():
    # Connection params
    param_dic = {
        "host"      : "localhost",
        "database"  : "worldbankdata",
        "user"      : "myuser",
        "password"  : "Passw0rd"
    }
     
    csv_file = "/data/global_CO2_emissions.csv"
    df = pd.read_csv(csv_file)
    # Drop the 'Indicator Name' column as we don't need it
    df.drop('Indicator Name',axis=1,inplace=True)
    
     # Replace NaN values with 'NULL'
    years = [x for x in df.columns if x != 'Country Name']
    for year in years:
        df[year] = df[year].apply(lambda x:'NULL' if np.isnan(x) else x)
        # Also drop any special character in the country name
        df['Country Name'] = df['Country Name'].astype(str).replace('[^a-zA-Z0-9]','',regex=True)
        
        conn= connect(param_dic)
        # Insert the dataframe one row at the time
        # For each country, upload the yearly C02 emissions
        for i in df.index:
            country_name = df['Country Name'][i]
            # Loop through each year
            for year in years:
                co2 = df[year][i]
                query = """
                    INSERT into emissions(country_name,year,co2 values('%s','%s','%s');
                    """ %(country_name,year,co2)
                single_insert(conn,query)
                
        print("All rows were sucessfully inserted in the emission table")
        
        conn.close()
        

if "__name__ " == "__main__":
    main()
    
    
                 
       