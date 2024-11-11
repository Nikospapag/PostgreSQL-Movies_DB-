import matplotlib.pyplot as plt
import numpy as np
import psycopg2
from mpl_toolkits.mplot3d import axes3d
from config import config
import os
import pandas as pd
from prettytable import PrettyTable


def connect():
    connection = None
    action = None
    set_up= False

    try:
        params = config()
        print(f'Connecting to {params["database"]}...\n')
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()

        print('Connected successfully.\n')

        
        
        while True:
            print("Welcome:\n 1.Set Up Database \n 2.Execute SQL Queries \n 3.Clear Database\n 4.Exit\n")
            action = input("Enter your action: ")
            if action == str(1):
                print("Creating the required tables...\n")
                sql_directory = "../create_tables"
                data_directory = "../data"
                alter_directory= "../alter_tables"
                create_tables(cursor, sql_directory, data_directory, connection)
                alter_tables(cursor, alter_directory, connection)
                set_up = True  
            elif action == str(2):
                
                query_directory = "../sql_queries"
                if set_up:
                    execute_queries(connection, cursor, query_directory)
                else:
                    print("Can't execute queries because the database isn't set up.\n")    
                

            elif action == str(3):
                if set_up:
                    cursor.execute('''DO $$ DECLARE
                        r RECORD;
                        BEGIN
                        FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
                            EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                        END LOOP;
                        END $$;''')
                    connection.commit()
                    set_up = False
                
                else:
                    print("Can't execute queries because the database isn't set up.\n")   

            else:
                break
                

    
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection terminated.\n')

def alter_tables(cursor, alter_directory, connection):
    for filename in os.listdir(alter_directory):
        if filename.endswith(".sql"):
            file_path = os.path.join(alter_directory, filename)
            print('Executing sql script...\n')

            with open(file_path, 'r') as file:
                sql_script = file.read()
                try:
                    cursor.execute(sql_script)
                    connection.commit()
                    print(f"Executed  sql script{filename}.\n")
                except Exception as e:
                    print(f"Error executing {filename}: {e}\n")
                    connection.rollback()

            

def create_tables(cursor, sql_directory, data_directory, connection):

    for filename in os.listdir(sql_directory):
        if filename.endswith(".sql"):

            file_path = os.path.join(sql_directory, filename)
            table_name = filename.replace('create_', '').replace('.sql', '')
            print(f'Executing {filename}...')
            with open(file_path, 'r') as file:
                sql_script = file.read()
                try:
                    cursor.execute(sql_script)
                    connection.commit()
                    print(f"Executed {filename} and created table {table_name}.\n")

                    data_file_path = os.path.join(data_directory, f"{table_name}.csv")
                    if os.path.exists(data_file_path):
                        insert_data(cursor, data_file_path, table_name, connection)
                    else:
                        print(f"No corresponding CSV file found for {table_name}.\n")

                except Exception as e:
                    print(f"Error executing {filename}: {e}\n")
                    connection.rollback()



def insert_data(cursor, data_file_path, table_name, connection):
    
    df = pd.read_csv(data_file_path)
    print(f"Inserting data from {data_file_path} into {table_name}...")
    if table_name == "movie":
        df['release_date'] = df['release_date'].fillna(pd.to_datetime('1970-01-01'))
    
    for index, row in df.iterrows():
        
        columns = ', '.join(df.columns)
        values = ', '.join(['%s'] * len(row))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        try:
            cursor.execute(insert_query, tuple(row))
        except Exception as e:
            print(f"Error inserting data into {table_name}: {e}\n")
            connection.rollback()
            return

    connection.commit()
    print(f"Data inserted into {table_name} successfully.\n")


def execute_queries(connection, cursor, query_directory):
    for filename in os.listdir(query_directory):
        if filename.endswith(".sql"):
            file_path = os.path.join(query_directory, filename)
            print(f'Executing {filename}...\n')
            with open(file_path, 'r') as file:
                sql_script = file.read()
                try:
                    cursor.execute(sql_script)
                    connection.commit()
                    rows = cursor.fetchall()

                    column_names = [desc[0] for desc in cursor.description]

                    table = PrettyTable()
                    table.field_names = column_names
                    for row in rows:
                        table.add_row(row)
                    
                    
                    print(f"Executed {filename}. Results: \n")
                    print(table)
                    print('\n')
                except Exception as e:
                    print(f"Error executing {filename}: {e}\n")
                    connection.rollback()



if __name__ == "__main__":
    connect()
