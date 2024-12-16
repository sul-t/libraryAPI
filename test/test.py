import requests

def authors():
    authors = [
        {
            "name": "Лев", 
            "surname": "Толстой",
            "date_of_birth": "1910-11-20",
        },
        {
            "name": "Александр", 
            "surname": "Пушкин",
            "date_of_birth": "1799-05-26",
        },
        {
            "name": "Николай", 
            "surname": "Некрасов",
            "date_of_birth": "1821-11-28",
        }
    ]

    return authors


def test_create_authors():
    url = 'http://127.0.0.1:8000/authors'

    for author in authors():
        print(author)
        response = requests.post(url, json = author)
        
        assert response.status_code == 200


def test_all_authors():
    url = 'http://127.0.0.1:8000/authors' 
    response = requests.get(url)

    assert response.status_code == 200


def test_author_by_id():
    id = 1
    url = f'http://127.0.0.1:8000/authors/{id}' 
    response = requests.get(url)

    assert response.status_code == 200


def test_update_authors():
    id = 1  
    url = f'http://127.0.0.1:8000/authors/{id}' 
    author = {
        "name": "Жека", 
        "surname": "Толстой",
        "date_of_birth": "2003-11-20",
    }

    response = requests.put(url, json=author)
    
    assert response.status_code == 200


def test_delete_authors():
    id = 1  
    url = f'http://127.0.0.1:8000/authors/{id}' 

    response = requests.delete(url)

    assert response.status_code == 200


def books():
    books = [
        {
            "name": "Сказка о царе Салтане",
            "desc": "Интересная",
            "author_id": 2,
            "available_count": 5
        },
        {
            "name": "Дубровский",
            "desc": "Написана в 1841",
            "author_id": 2,
            "available_count": 15
        }
    ]

    return books


def test_create_books():
    url = 'http://127.0.0.1:8000/books' 
    for book in books():
        response = requests.post(url, json=book)

        assert response.status_code == 200


def test_all_books():
    url = 'http://127.0.0.1:8000/books' 
    response = requests.get(url)

    assert response.status_code == 200


def test_book_by_id():
    id = 1
    url = f'http://127.0.0.1:8000/books/{id}' 
    response = requests.get(url)

    assert response.status_code == 200

def test_update_books():
    id = 1
    url = f'http://127.0.0.1:8000/books/{id}' 
    book = {
            "name": "Капитанская дочка",
            "desc": "Гиганская",
            "author_id": 2,
            "available_count": 3
        }
    response = requests.put(url, json=book)

def test_delete_authors():
    id = 1  
    url = f'http://127.0.0.1:8000/books/{id}' 

    response = requests.delete(url)

    assert response.status_code == 200


def borrows():
    borrows = [
        {
            "book_id": 2,
            "reader_name": "Кирилл"
        },
        {
            "book_id": 2,
            "reader_name": "Данил"
        }
    ]

    return borrows

def test_create_borrows():
    url = 'http://127.0.0.1:8000/borrows' 
    for borrow in borrows():
        response = requests.post(url, json=borrow)

        assert response.status_code == 200

def test_all_borrows():
    url = 'http://127.0.0.1:8000/borrows' 
    response = requests.get(url)

    assert response.status_code == 200

def test_borrow_by_id():
    id = 1
    url = f'http://127.0.0.1:8000/borrows/{id}' 
    response = requests.get(url)

    assert response.status_code == 200

def test_update_status_order():
    id = 1
    url = f'http://127.0.0.1:8000/borrows/{id}/return' 
    response = requests.patch(url, json={"date_of_return": "2024-12-30"})

    assert response.status_code == 200


