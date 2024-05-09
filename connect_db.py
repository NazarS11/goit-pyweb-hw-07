from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://admin:4321@localhost/univercity_db")
Session = sessionmaker(bind=engine)
session = Session()
