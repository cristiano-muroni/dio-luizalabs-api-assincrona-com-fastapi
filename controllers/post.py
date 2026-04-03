from fastapi import APIRouter, status, Response
from schemas.post import PostIn
from views.post import PostOut


router = APIRouter(prefix="/posts")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def crate_post(post: PostIn):
    # fake_db.append(post.model_dump())
    return post

@router.get("/",response_model=list[PostOut])
def read_posts_pub(
    response: Response,
    published: bool,
    limit: int,
    skip: int =0    
    ):
    return []
    # tail = skip + limit   
    # [post for post in fake_db[skip: tail] if post['published'] is published]