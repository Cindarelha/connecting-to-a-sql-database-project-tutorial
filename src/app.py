import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv


# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

DB_USER='gitpod'
DB_PASSWORD='postgres'
DB_PORT=3306
DB_HOST='localhost'
DB_NAME='sample-db'
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(connection_string).execution_options(autocommit=True)
engine.connect()

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
engine.execute("""
CREATE TABLE IF NOT EXISTS publishers(
    publisher_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY(publisher_id)
);
""")

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
engine.execute("""
INSERT INTO publishers(publisher_id, name) VALUES (1, 'O Reilly Media');
INSERT INTO publishers(publisher_id, name) VALUES (2, 'A Book Apart');
INSERT INTO publishers(publisher_id, name) VALUES (3, 'A K PETERS');
INSERT INTO publishers(publisher_id, name) VALUES (4, 'Academic Press');
INSERT INTO publishers(publisher_id, name) VALUES (5, 'Addison Wesley');
INSERT INTO publishers(publisher_id, name) VALUES (6, 'Albert&Sweigart');
INSERT INTO publishers(publisher_id, name) VALUES (7, 'Alfred A. Knopf');
""")

# 4) Use pandas to print one of the tables as dataframes using read_sql function
               
result_dataFrame = pd.read_sql("Select * from publishers;", engine)
print(result_dataFrame)

# Cerrar la conexión
#engine.close()