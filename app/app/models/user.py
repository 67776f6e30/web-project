from ..core.database import *


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    phone = Column(String(20))
    password = Column(String(100))
