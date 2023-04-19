from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from __init__ import *
Base = declarative_base()

class account(Base):
    __tablename__ = "account"
    url_tiktok = Column(String(256), primary_key=True, nullable= False)
    count_live = Column(Integer)
    count_flower = Column(Integer)
    user_subtitle = Column(String(256))
    user_bio = Column(String(256))
    spanlink = Column(String(256))
    phone_number = Column(String(256))
    url_facebook = Column(String(256))
    check = Column(Boolean, default=False)
    def toString(self):
        return ([self.url_tiktok, self.count_live,self.count_flower, self.user_subtitle, self.user_bio,self.spanlink, self.phone_number, self.url_facebook])

if __name__ == '__main__':
    Base.metadata.create_all(engine)