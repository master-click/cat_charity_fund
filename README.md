# Приложение для благотворительного фонда QRKot

## Описание проекта
Фонд собирает пожертвования на различные целевые проекты.

У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.

Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму.

Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.

## Стек технологий
- Python 3.9.12;
- FastAPI 0.78;
- Аlembic 1.7.7;
- SQLAlchemy 1.4.36;
- Pydantic 1.9.1;
- Uvicorn 0.17.6.

## Запуск проекта

### 1) Склонировать репозиторий
```
git clone git@github.com:master-click/cat_charity_fund.git
```

### 2) Создать и активировать виртуальное окружение для проекта
```
python -m venv venv
```
```
source venv/scripts/activate
```

### 3) Установить зависимости
```
python -m pip install --upgrade pip
```
```
python pip install -r requirements.txt
```

### 4) Создать базу данных
```
alembic upgrade head
```

### 5) Запустить проект
```
uvicorn app.main:app --reload
```

После запуска проект должен быть доступен по адресу: http://127.0.0.1:8000/

Документация и выполнение запросов к API: http://127.0.0.1:8000/docs


## Примеры запросов
1. GET-запрос на получение всех проектов http://127.0.0.1:8000/charity_project/

```
# Ответ:
[
  {
    "name": "Важный проект",
    "description": "string",
    "full_amount": 5000,
    "id": 1,
    "invested_amount": 5000,
    "fully_invested": true,
    "create_date": "2023-04-10T15:57:24.584112",
    "close_date": "2023-04-11T18:02:54.849585"
  },
  {
    "name": "Интересный проект",
    "description": "string",
    "full_amount": 5000,
    "id": 2,
    "invested_amount": 5000,
    "fully_invested": true,
    "create_date": "2023-04-11T17:18:13.961236",
    "close_date": "2023-04-11T18:03:53.122154"
  },
  {
    "name": "Крутой проект",
    "description": "2 лимона",
    "full_amount": 2000000,
    "id": 3,
    "invested_amount": 1239000,
    "fully_invested": false,
    "create_date": "2023-04-11T17:26:47.486937"
  }
]
```

2. POST-запрос на добавление проекта: http://127.0.0.1:8000/charity_project/

```
# Запрос:
{
  "name": "Строительство приюта",
  "description": "Приют для бездомных кошек площадью 100 кв.м.",
  "full_amount": 3000000
}

# Ответ:
{
  "name": "Строительство приюта",
  "description": "Приют для бездомных кошек площадью 100 кв.м.",
  "full_amount": 3000000,
  "id": 8,
  "invested_amount": 0,
  "fully_invested": false,
  "create_date": "2023-04-13T10:00:01.232031"
}
```

3. GET-запрос на получение всех пожертвований http://127.0.0.1:8000/donation/

```
# Ответ:
[
  {
    "full_amount": 1000000,
    "comment": "миллион вам в руки",
    "id": 1,
    "create_date": "2023-04-11T17:25:47.369809",
    "user_id": 1,
    "invested_amount": 1000000,
    "fully_invested": true,
    "close_date": "2023-04-11T18:03:53.122154"
  },
  {
    "full_amount": 1000,
    "comment": "на доброе дело от Васи",
    "id": 2,
    "create_date": "2023-04-13T10:04:31.661262",
    "user_id": 1,
    "invested_amount": 1000,
    "fully_invested": true,
    "close_date": "2023-04-13T10:04:31.792795"
  }
]
```

4. POST-запрос на добавление пожертвования: http://127.0.0.1:8000/donation/
```
# Запрос:
{
  "full_amount": 1000,
  "comment": "на доброе дело от Васи"
}

# Ответ:
{
  "full_amount": 1000,
  "comment": "на доброе дело от Васи",
  "id": 8,
  "create_date": "2023-04-13T10:04:31.661262"
}
```

5. GET-запрос на получение информации о пользователе: http://127.0.0.1:8000/users/3
```
# Ответ:
{
  "id": 3,
  "email": "masha@masha.ru",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}
```

## Разработчик
Батова Ольга, [@olgabato](https://t.me/olgabato)
