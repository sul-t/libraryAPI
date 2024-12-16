from app.dao.base import BaseDAO
from app.books.models import Book
from app.authors.models import Author
from app.database import async_session_maker

from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError


class BookDAO(BaseDAO):
    model = Book

    @classmethod
    async def find_book_by_id(cls, book_id):
        async with async_session_maker() as session:
            query = select(cls.model.name, cls.model.desc, Author.name, cls.model.available_count).join(Author, cls.model.author_id == Author.id).where(cls.model.id == book_id)
            result = await session.execute(query)

            return result.first()
        
    @classmethod
    async def add_book(cls, values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)

                book_info = await session.get(Author, new_instance.author_id)
                if not book_info:
                    return None

                session.add(new_instance)
                
                try: 
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()

                    raise e
                
                return new_instance
            
            
