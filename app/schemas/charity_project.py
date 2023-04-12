from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt, validator


class CharityProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectUpdate(CharityProjectBase, extra=Extra.forbid):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]

    @validator('name')
    def name_cant_be_none(cls, value):
        if value is None:
            raise ValueError('Название проекта не может быть пустым!')
        return value

    @validator('description')
    def description_cannot_be_null(cls, value):
        if value is None:
            raise ValueError('Описание проекта не может быть пустым!')
        return value

    @validator('full_amount')
    def check_full_amount(cls, value, values):
        if value is None:
            raise ValueError('Поле с требуемой суммой не может быть пустым!')
        if 'invested_amount' in values and values['invested_amount'] is not None:
            if value < values['invested_amount']:
                raise ValueError('Сумма не может быть меньше уже вложенной!')
        return value

    @validator('close_date', check_fields=False)
    def project_must_be_open(cls, value):
        if value is not None:
            raise ValueError('Проект уже закрыт и не может быть обновлен!')
        return value


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
