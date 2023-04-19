from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:mailong2000@localhost:3306/tiktok')
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
