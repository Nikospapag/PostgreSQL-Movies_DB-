PostgreSQL Database MoviesDB
General Info
It started as a university project, where the goal was to set up and manage an Azure PostgreSQL Database with IMDB Data. Now that the Database is no longer on AzureCloud, we built an app to set it up locally and explore it easily. The code is written mainly in Python and it can work with any PostgreSQL Database.

Installation
Firstly, some python packages are needed for the app to work properly.

pip install prettytable
pip install pandas
pip install psycopg2
Then, PostgreSQL needs to be installed on your computer, with an empty database already created. After downloading the files, database.ini must be edited with the right properties as follows:

[postgresql]
host= (localhost for local DB or url for cloud)
database= (database name)
user= (postgres username)
password= (postgres password)
Finally, the app is ready to be launched.

Usage
The UI is quite simple, as the following menu shows up at first.

Welcome:
1.Set Up Database
2.Execute SQL Queries
3.Clear Database
4.Exit
            
On the initial launch, you must choose Option 1, for the installation to be completed. Option 3 drops all the tables without deleting the Database itself, while Option 2 executes all the SQL queries that are located in the sql_queries folder, printing the results below.

Customization
If you want to use a different Database, you have to follow some instructions for the app to work properly. In the "data" folder should be stored .csv files that contain table data, one for each table. In the "create_tables" folder should be stored .sql scripts, each one responsible for the creation of a table. The naming template needs to be strict for the binding to work: "create_tablename.sql" and "tablename.csv". Any further alterations regarding the schema, must be represented as .sql scripts at the "alter_tables" folder.
























CREATE DATABASE MOVIES_DB ;



pip install psycopg2
