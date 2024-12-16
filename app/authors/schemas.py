from datetime import date, datetime
from pydantic import BaseModel, Field, field_validator, ConfigDict



class SAuthor(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int 
    name: str = Field(..., description='Имя автора')
    surname: str = Field(..., description='Фамилия автора')
    date_of_birth: date = Field(..., description='Дата рождения автора в формате ГГГГ-ММ-ДД')
   
class SAuthorAdd(BaseModel):
    name: str = Field(..., description='Имя автора')
    surname: str = Field(..., description='Фамилия автора')
    date_of_birth: date = Field(..., description='Дата рождения автора в формате ГГГГ-ММ-ДД')

    @field_validator('date_of_birth')
    def validate_date_of_birth(cls, value):
        if value and value >= datetime.now().date():
            raise ValueError('Дата рождения должна быть старше текущего времени')
        
        return value

class SAuthorUpdate(BaseModel):
    name: str = Field(..., description='Имя автора')
    surname: str = Field(..., description='Фамилия автора')
    date_of_birth: date = Field(..., description='Дата рождения автора в формате ГГГГ-ММ-ДД')