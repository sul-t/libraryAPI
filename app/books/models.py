from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base



class Book(Base):
    name: Mapped[str]
    desc: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.id'), nullable=False)
    available_count: Mapped[int]

