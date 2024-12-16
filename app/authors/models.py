from datetime import date
from sqlalchemy.orm import Mapped

from app.database import Base



class Author(Base):
    name: Mapped[str]
    surname: Mapped[str]
    date_of_birth: Mapped[date]
