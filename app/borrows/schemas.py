from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Tuple



class SBorrow(BaseModel):
    id: int
    book_id: int = Field(..., description='ID книги')
    reader_name: str = Field(..., description='Имя читателя')
    date_of_issue: date = Field(..., description='Дата выдачи')
    date_of_return: date | None = Field(..., description='Дата возврата')

class SBorrowInfo(BaseModel):
    book_name: str = Field(..., description='Название книги')
    reader_name: str = Field(..., description='Имя читателя')
    date_of_issue: date = Field(..., description='Дата выдачи')
    date_of_return: date | None = Field(..., description='Дата возврата')

    @classmethod
    def from_tuple(cls, data: Tuple) -> 'SBorrowInfo':
        return cls(
            book_name=data[0],
            reader_name=data[1],
            date_of_issue=data[2],
            date_of_return=data[3]
        )

class SBorrowAdd(BaseModel):
    book_id: int = Field(..., description='ID книги')
    reader_name: str = Field(..., description='Имя читателя')

class SBorrowReturn(BaseModel):
    date_of_return: date = Field(..., description='Дата возврата')
