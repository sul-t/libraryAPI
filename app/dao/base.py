from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select, update as sqlalchemy_update, delete as sqlalchemy_delete
from app.database import async_session_maker



class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)

            return result.scalars().all()
        
    @classmethod
    async def find_one_or_none_by_id(cls, id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=id)
            result = await session.execute(query)

            return result.scalar_one_or_none()
        
    @classmethod
    async def add(cls, values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                
                try: 
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()

                    raise e
                
                return new_instance
            
    @classmethod
    async def update(cls, id, values):
        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    sqlalchemy_update(cls.model)
                    .where(cls.model.id == id)
                    .values(**values)
                    .execution_options(synchronize_session="fetch")
                )
                result = await session.execute(query)

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()

                    raise e
                
                return result.rowcount
            
    @classmethod
    async def delete(cls, id):
        async with async_session_maker() as session:
            async with session.begin():
                query = sqlalchemy_delete(cls.model).filter_by(id=id)
                result = await session.execute(query)

                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()

                    raise e
                
                return result