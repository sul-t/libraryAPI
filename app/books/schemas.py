from pydantic import BaseModel, Field
from typing import Tuple



class SBook(BaseModel):
    id: int
    name: str = Field(..., description='Название книги')
    desc: str = Field(..., description='Описание книги')
    author_id: int = Field(..., description='ID автора')
    available_count: int = Field(..., description='Кол-во доступных экземпляров')

class SBookInfo(BaseModel):
    name: str = Field(..., description='Название книги')
    desc: str = Field(..., description='Описание книги')
    author_name: str = Field(..., description='Имя автора')
    available_count: int = Field(..., description='Кол-во доступных экземпляров')

    @classmethod
    def from_tuple(cls, data: Tuple) -> 'SBookInfo':
        return cls(
            name=data[0],
            desc=data[1],
            author_name=data[2],
            available_count=data[3]
        )

class SBookAdd(BaseModel):
    name: str = Field(..., description='Название книги')
    desc: str = Field(..., description='Описание книги')
    author_id: int = Field(..., description='ID автора')
    available_count: int = Field(..., gt=0, description='Кол-во доступных экземпляров')

class SBookUpdate(BaseModel):
    name: str = Field(..., description='Название книги')
    desc: str = Field(..., description='Описание книги')
    author_id: int = Field(..., description='ID автора')
    available_count: int = Field(..., gt=0, description='Кол-во доступных экземпляров')
