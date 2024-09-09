from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.main import create_app


app = create_app()
client = TestClient(app)

def test_get_all_posts():
    response = client.get("/post/")
    assert response.status_code == 200
    assert type(response.json()) == list

def test_create_post():
    response = client.post("/post/", json={"title": "test", "content": "test"})
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_post():
    response = client.get("/post/")
    assert response.status_code == 200
    post_id = response.json()[0]["id"]
    response = client.get(f"/post/{post_id}")
    assert response.status_code == 200
    assert "id" in response.json()
    assert "title" in response.json()
    assert "content" in response.json()
    
def test_update_post():
    response = client.get("/post/")
    assert response.status_code == 200
    post_id = response.json()[0]["id"]
    response = client.put(f"/post/{post_id}", json={"title": "test2", "content": "test2"})
    assert response.status_code == 200
    assert "id" in response.json()

def test_delete_post():
    response = client.get("/post/")
    assert response.status_code == 200
    post_id = response.json()[0]["id"]
    response = client.delete(f"/post/{post_id}")
    assert response.status_code == 200
    assert "id" in response.json()