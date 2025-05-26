# import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy_utils import database_exists, create_database,drop_database
from sqlalchemy.orm import sessionmaker, relationship,declarative_base
#
#
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root123",
#     port="3306",
#     database="mft"
# )
#
# cursor = connection.cursor()
# # cursor.execute("select * from students")
# # print(cursor.fetchall())
#
#
# cursor.execute("INSERT INTO students (name, family, birth_date, status) VALUES ('ali', 'alipour', null, 1)")
# connection.commit()
#
# connection.close()


connection_string = 'mysql+pymysql://mahi:root123@localhost/world'

if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)
session = sessionmaker(bind=engine)
session = session()

Base = declarative_base()


class Country(Base):
    __tablename__ = 'country'

    Code = Column(String(3), primary_key=True)
    Name = Column(String(52), nullable=False)



class City(Base):
    __tablename__ = 'city'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String(35), nullable=False)
    CountryCode = Column(String(3), ForeignKey('country.Code'), nullable=False)
    District = Column(String(20), nullable=False)
    Population = Column(Integer, nullable=False)
    country = relationship("Country")

new_city = City(Name='New City', CountryCode='USA', District='New District', Population=100000)
session.add(new_city)
session.commit()

query = (session.query(City.Name == 'New City'))
print(query)

#update
# session.merge()

#delete
# session.delete()

