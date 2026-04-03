from fastapi import APIRouter, status, Response
from schemas.post import PostIn
from views.post import PostOut
from models.post import posts
from database import database

router = APIRouter(prefix="/posts")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
def crate_post(post: PostIn):
    # ---old fake_db
    return post

@router.get("/",response_model=list[PostOut])
async def read_posts(
    response: Response,
    published: bool,
    limit: int,
    skip: int =0    
    ):
    query = posts.select()
    return  await database.fetch_all(query)