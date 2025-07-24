from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Book API"}

def test_create_book():
    payload = {
        "id": 1,
        "title": "Test-Driven Development",
        "author": "Kent Beck",
        "description": "A book on TDD"
    }
    response = client.post("/books", json=payload)
    assert response.status_code == 200
    assert response.json() == payload

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_book():
    payload = {
        "id": 2,
        "title": "Delete Me",
        "author": "Someone",
        "description": "To be deleted"
    }
    client.post("/books", json=payload)

    # Delete the book
    response = client.delete("/books/2")
    assert response.status_code == 200
    assert response.json() == {"message": "Book deleted"}

    # Confirm the book is gone
    get_response = client.get("/books/2")
    assert get_response.status_code == 404
    assert get_response.json() == {"detail": "Book not found"}

