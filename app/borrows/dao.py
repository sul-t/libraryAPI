from app.dao.base import BaseDAO
from app.borrows.models import Borrow
from app.database import async_session_maker
from app.books.models import Book

from sqlalchemy import select, update as sqlalchemy_update
from sqlalchemy.exc import SQLAlchemyError
from datetime import date, datetime




class BorrowDAO(BaseDAO):
    model = Borrow

    @classmethod
    async def fing_borrow_by_id(cls, borrow_id):
        async with async_session_maker() as session:
            query = select(Book.name, cls.model.reader_name, cls.model.date_of_issue, cls.model.date_of_return).join(Book, cls.model.book_id == Book.id).where(cls.model.id == borrow_id)
            result = await session.execute(query)

            return result.first()

    @classmethod
    async def add_borrow(cls, values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)

                book_info = await session.get(Book, new_instance.book_id)
                if (not book_info) or (book_info.available_count == 0):
                    return None

                book_info.available_count -= 1

                session.add(new_instance)
                
                try: 
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()

                    raise e
                
                return new_instance
            
    @classmethod
    async def patch_borrow(cls, borrow_id, date_of_return):
        async with async_session_maker() as session:
            async with session.begin():
                borrow_info = await session.get(cls.model, borrow_id)
                if (not borrow_info) or (borrow_info.date_of_return is not None):
                    return None
                
                book_info = await session.get(Book, borrow_info.book_id)
                book_info.available_count += 1

                query = sqlalchemy_update(cls.model).where(cls.model.id == borrow_id).values(date_of_return=date_of_return)
                result = await session.execute(query)

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()

                    raise e
                
                return result