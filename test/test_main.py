from fastapi.testclient import TestClient
from main import app
import test

client = TestClient(app)

def test_read_post():
    response = client.get("/post")
    assert response.status_code == 200
    posts = response.json()
    
    assert type(posts) == list
    
    for post in posts:
        response = client.get(f"/post/{post['id']}")
        assert response.status_code == 200
        response_post = response.json()
        assert type(response_post) == dict
        assert response_post['id'] == post['id']
        assert response_post['title'] == post['title']
        assert response_post['content'] == post['content']
        assert response_post['createdAt'] == post['createdAt']
        assert response_post['updatedAt'] == post['updatedAt']
        assert response_post['author'] == post['author']
    
        
        
