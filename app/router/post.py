import datetime
from bson import ObjectId
from fastapi import APIRouter, HTTPException, Request

from guard import local_auth_guard
from model.post import CreatePostDto, CreatePostRequestDto, PostResponseDto, UpdatePostDto, UpdatePostRequestDto
from mongodb import mongodb

router = APIRouter(prefix="/post")

@router.get("/")
async def get_all_post(request: Request):
    post_collection = mongodb.collection("posts")
    post_cursor = post_collection.find({})
    posts = []
    
    for post in post_cursor:
        posts.append(
            PostResponseDto(
                id=str(post["_id"]),
                title=post["title"],
                content=post["content"],
                author=post["author"],
                createdAt=post["createdAt"],
                updatedAt=post.get("updatedAt")
            )
        )
    
    return posts

@router.get("/{id}")
def get_post(id: str):
    post_collection = mongodb.collection("posts")
    post = post_collection.find_one({'_id': ObjectId(id)})

    return PostResponseDto(
        id=str(post["_id"]),
        title=post["title"],
        content=post["content"],
        author=post["author"],
        createdAt=post["createdAt"],
        updatedAt=post.get("updatedAt")
    )

@router.post("/")
@local_auth_guard
def create_post(request: Request, post: CreatePostRequestDto):
    # extract author from session
    post = CreatePostDto(
        title=post.title,
        content=post.content,
        author= request.session.get("user").get("name"),
        createdAt=datetime.datetime.now().isoformat(),
    )
    
    # create post
    post_collection = mongodb.collection("posts")
    post_id = post_collection.insert_one(post.model_dump()).inserted_id
    return {"id": str(post_id)}

@router.put("/{id}")
@local_auth_guard
def update_post(request: Request, id: str, post: UpdatePostRequestDto): 
    author = request.session.get("user").get("name")
    post_collection = mongodb.collection("posts")
    result = post_collection.update_one(
        {"_id": ObjectId(id), "author": author},
        {"$set": post.model_dump()}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Not Found")
    
    return {"id": id}

@router.delete("/{id}")
@local_auth_guard
def delete_post(request: Request, id: str):
    author = request.session.get("user").get("name")
    post_collection = mongodb.collection("posts")
    result = post_collection.delete_one({"id": id, "author": author})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Not Found")
    
    return {"id": id}