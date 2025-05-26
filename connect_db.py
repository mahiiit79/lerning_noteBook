from pandas import read_sql
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
import pandas as pd

connection_string = 'mysql+pymysql://mahi:root123@localhost/saleDB'

if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)
session = sessionmaker(bind=engine)
session = session()


df = pd.read_excel('ListData (5).xlsx')
df.drop(columns=['اولویت','شماره بچ','مشخصه فنی','مرکز نگهداری'],inplace=True)
# df.to_sql('productionorder',engine)

df = read_sql('select * from productionorder', con=engine)
print(df)