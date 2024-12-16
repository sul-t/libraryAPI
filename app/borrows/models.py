from datetime import date
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base



class Borrow(Base):
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'), nullable=False)
    reader_name: Mapped[str]
    date_of_issue: Mapped[date] = mapped_column(server_default=func.now())
    date_of_return: Mapped[date | None]