#using SQLAlchemy ORM
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import inspect


#put argument echo=True for SQL code being run in the background for debugging
eng = create_engine('sqlite:///crunchbase_data.db')
Base = declarative_base()


class Company(Base):
    '''
    Table companies with attributes Name, StockSymbol and Summary
    Primary key: Name
    '''
    __tablename__ = "companies"      
    name = Column(String, primary_key=True)      
    stockSymbol = Column(String)
    summary = Column(String, nullable=False)
    #make a link between the companies and social_accounts tables
    accounts = relationship("SocialAccount", backref="company")    
    

#table SocialAccount will be linked to table Company using Company.Name as the primary key
#splitting the date into two tables is strictly not required since we are dealing with few attributes
#splitting was done mainly to experiment and learn about working with foreign keys in ORM
class SocialAccount(Base):
    '''
    Table social_accounts with attributes Website, Name, Twitter, Facebook and LinkedIn linked to the companies table through Name
    Primary key: Website
    Foreign key: companies.Name
    '''
    __tablename__ = "social_accounts"  
    website = Column(String, primary_key=True)
    name = Column(String, ForeignKey("companies.name"))      
    twitter = Column(String, nullable=False)
    facebook = Column(String, nullable=False)
    linkedIn = Column(String, nullable=False)    


Base.metadata.bind = eng
Base.metadata.create_all()


class ORMInterface(object):
    '''
    Provides ORM functionality through SQLAlchemy for using a database (used system: SQLite)
    '''
    def write_row(self, item):
        Session = sessionmaker(bind=eng)
        ses = Session()        
        #to add a new row first check if the row is present, if not then add it
        #if two rows with the same name are added then a primary key constraint error will be thrown
        #retrieve row with given name
        curr_row = ses.query(Company).filter(Company.name.like(item[0])).first()
        #if no row present in database with given name
        if (curr_row == None):
            row = Company(name=item[0], stockSymbol=item[5], summary=item[6])
            row.accounts = [SocialAccount(website=item[1], twitter=item[2], facebook=item[3], linkedIn=item[4])]
            ses.add(row)
            ses.commit()
            print ("Row with {} added".format(item[0]))
        else:
            print ("Row with {} already exists".format(item[0]))
    def read_row(self, name):
        Session = sessionmaker(bind=eng)
        ses = Session() 
        #filter rows given a name value
        row = ses.query(Company).filter(Company.name.like(name)).first()  
        columns1 = [row.key for row in row.__table__.columns]
        print ("\nCompany details from database: \n")
        for x in columns1:
            print (x, " : ", getattr(row, x))
        columns2 = [row.key for row in row.accounts[0].__table__.columns]
        for x in columns2:
            if (x != 'name'):
                print (x, " : ", getattr(row.accounts[0], x))                
        print ("\n")
        return None
