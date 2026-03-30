from fastapi import FastAPI, Header, status, Response, Cookie

from  datetime import datetime, UTC 

from pydantic import BaseModel

from typing import Annotated

app = FastAPI()

fake_db = [
    {"title": f"Criando uma aplicação com Django", "date": datetime.now(UTC),'published': True},
    {"title": f"Intercionalizando uma aplicação com Flask", "date": datetime.now(UTC), 'published': True},
    {"title": f"Criando uma aplicação com FastAPI", "date": datetime.now(UTC), 'published': True},
    {"title": f"Hands-on de uma aplicação com Pandas", "date": datetime.now(UTC), 'published': False}
] # type: ignore

class Post(BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False   

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def crate_post(post: Post):
    fake_db.append(post.model_dump())
    return post

@app.get("/posts")
def read_posts_pub(response: Response, published: bool, limit: int, skip: int =0,
                   ads_id: Annotated[str | None, Cookie()] = None, 
                   user_agent: Annotated[str | None, Header()] = None
     ):
    print(f"Cockie: {ads_id}")
    print(f"Header: {user_agent}")
    response.set_cookie(key="user", value="cris.teste@gmail.com")
    posts = []
    for post in fake_db:
        if len(posts) is limit:
            break
        if post["published"] is published:
            posts.append(post)
    return posts # [post for post in fake_db[skip: skip + limit] if post['published'] is published]

@app.get("/posts/{framework}")
def read_posts(framework: int):
    return {"posts": [
        {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
        {"title": f"Intercionalizando uma aplicação com {framework}", "date": datetime.now(UTC)}
        ]}
