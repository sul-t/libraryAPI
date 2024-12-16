from fastapi import APIRouter, Depends
from app.authors.dao import AuthorDAO
from app.authors.schemas import SAuthor, SAuthorAdd, SAuthorUpdate



router = APIRouter(prefix='/authors', tags=['Эндпоинты для авторов'])



@router.get('/', summary='Получиние списка авторов', response_model=list[SAuthor])
async def get_all_authors() -> list[SAuthor]:
    return await AuthorDAO.find_all()

@router.get('/{id}', summary='Получение информации об авторе по id', response_model=SAuthor | dict)
async def get_author_by_id(id: int) -> SAuthor | dict:
    result = await AuthorDAO.find_one_or_none_by_id(id=id)
    if result is None:
        return {"message": f"Автора с ID {id} не найден"}

    return result


@router.post('/', summary='Создание автора')
async def create_author(author: SAuthorAdd) -> dict:
    check = await AuthorDAO.add(author.dict())
    if check:
        return {
            "message": "Автор успешно создан", 
            "author": author
        }
    else:
        return {"message": "Ошибка при создании автора"}
    

@router.put('/{id}', summary='Обновление информации об авторе')
async def update_author(id: int, author: SAuthorUpdate) -> dict:
    check = await AuthorDAO.update(id, author.dict())
    if check:
        return {
            "message": "Данные автора успешно обновленны", 
            "author": author
        }
    else:
        return {"message": "Ошибка при обновлении данных автора"}
    

@router.delete('/{id}', summary='Удаление автора')
async def delete_author(id: int) -> dict:
    check = await AuthorDAO.delete(id)
    if check:
        return {"message": f"Автор с ID {id} удален"}
    else:
        return {"message": "Ошибка при удалении автора"}