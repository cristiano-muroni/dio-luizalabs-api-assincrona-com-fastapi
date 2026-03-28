from fastapi import FastAPI

from  datetime import datetime, UTC 

app = FastAPI()

fake_db = [
    {"title": f"Criando uma aplicação com Django", "date": datetime.now(UTC),'published': True},
    {"title": f"Intercionalizando uma aplicação com Flask", "date": datetime.now(UTC), 'published': True},
    {"title": f"Criando uma aplicação com FastAPI", "date": datetime.now(UTC), 'published': True},
    {"title": f"Hands-on de uma aplicação com Pandas", "date": datetime.now(UTC), 'published': False}
] # type: ignore

@app.get("/posts")
def read_posts_pub(skip: int = 0 , limit: int = len(fake_db), published: bool = True):
    return [post for post in fake_db[skip: skip + limit] if post['published'] is published]

@app.get("/posts/{framework}")
def read_posts(framework: int):
    return {"posts": [
        {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
        {"title": f"Intercionalizando uma aplicação com {framework}", "date": datetime.now(UTC)}
        ]}
