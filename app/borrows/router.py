from fastapi import APIRouter
from app.borrows.schemas import SBorrow, SBorrowAdd, SBorrowInfo, SBorrowReturn
from app.borrows.dao import BorrowDAO

from datetime import date



router = APIRouter(prefix='/borrows', tags=['Эндпоинты для выдачи'])



@router.get('/', summary='Получение списка всех выдач')
async def get_all_borrow() -> list[SBorrow]:
    return await BorrowDAO.find_all()

@router.get('/{id}', summary='Получение информации о выдече по id')
async def get_borrow_by_id(id: int) -> SBorrowInfo | dict:
    check = await BorrowDAO.fing_borrow_by_id(borrow_id=id)
    if check is None:
        return {"message": f"Информация о выдаче по ID {id} не найдена"}

    book_info = SBorrowInfo.from_tuple(check)

    return book_info

@router.post('/', summary='Создание записи о выдаче книги')
async def create_borrow(borrow: SBorrowAdd) -> dict:
    check = await BorrowDAO.add_borrow(borrow.dict())
    if check:
        return {
            "message": "Запись о выдече успешно добавлена", 
            "borrow": borrow
        }
    else:
        return {"message": "Ошибка при создании записи о выдаче. Данной книги не существует или нет доступных экземпляров книги"}
    
@router.patch('/{id}/return', summary='Завершение выдачи')
async def pathc_borrow(id: int, borrow: SBorrowReturn) -> dict:
    check = await BorrowDAO.patch_borrow(borrow_id=id, date_of_return=borrow.date_of_return)
    if check:
        return {
            "message": "Дата возврата успешно добавлена",
            "borrow": borrow
        }
    else:
        return {"messege": "Ошибка при добавлении даты возврата"}