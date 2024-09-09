import datetime
from bson import ObjectId
from fastapi import APIRouter, HTTPException

from model.post import CreatePostDto, CreatePostRequestDto, PostResponseDto, UpdatePostDto, UpdatePostRequestDto
from mongodb import mongodb

router = APIRouter(prefix="/post")

@router.get("/")
async def get_all_post():
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
def create_post(post: CreatePostRequestDto):
    # extract author from session
    post = CreatePostDto(
        title=post.title,
        content=post.content,
        author="temp",
        createdAt=datetime.datetime.now().isoformat(),
    )
    
    # create post
    post_collection = mongodb.collection("posts")
    post_id = post_collection.insert_one(post.model_dump()).inserted_id
    return {"id": str(post_id)}

@router.put("/{id}")
def update_post(id: str, post: UpdatePostRequestDto):
    post_collection = mongodb.collection("posts")
    post_collection.find_one_and_update({'_id': ObjectId(id)}, {"$set": post.model_dump()})
    
    return {"id": id}

@router.delete("/{id}")
def delete_post(id: str):
    post_collection = mongodb.collection("posts")
    post_collection.delete_one({"id": id})
    return {"id": id}
