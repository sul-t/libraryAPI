from fastapi import APIRouter

from app.books.dao import BookDAO
from app.books.schemas import SBook, SBookAdd, SBookUpdate, SBookInfo


router = APIRouter(prefix='/books', tags=['Эндпоинты для книг'])



@router.get('/', summary='Получение списка книг', response_model=list[SBook])
async def get_all_book() -> list[SBook]:
    return await BookDAO.find_all()

@router.get('/{id}', summary='Получение информации о книге по id', response_model=SBookInfo | dict)
async def get_book_by_id(id: int) -> SBookInfo | dict:
    result = await BookDAO.find_book_by_id(book_id=id)
    if result is None:
        return {"message": f"Кника по ID {id} не найдена"}

    book_info = SBookInfo.from_tuple(result)

    return book_info


@router.post('/', summary='Добавление книги')
async def add(book: SBookAdd) -> dict:
    check = await BookDAO.add_book(book.dict())
    if check:
        return {
            "message": "Книга успешно добавлена",
            "book": book
        }
    else:
        return {"message": "Ошибка при добавлении книги"}
    

@router.put('/{id}', summary='Обновление информации о книге')
async def update_book(id: int, book: SBookUpdate) -> dict:
    check = await BookDAO.update(id, book.dict())
    if check:
        return {
            "message": "Данные книги успешно обновленны", 
            "book": book
        }
    else:
        return {"message": "Ошибка при обновлении данных книги"}
    

@router.delete('/{id}', summary='Удаление книги')
async def delete_book(id: int) -> dict:
    check = await BookDAO.delete(id)
    if check:
        return {"message": f"Книга с ID {id} удалена"}
    else:
        return {"message": "Ошибка при удалении книги"}