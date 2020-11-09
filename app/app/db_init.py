from .core.database import *
from .models import *


def db_init():
    Base.metadata.create_all(bind=engine)
    db_session.commit()


if __name__ == '__main__':
    db_init()
