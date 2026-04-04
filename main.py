from fastapi import FastAPI
from controllers import auth, post
from contextlib import asynccontextmanager
from database import database, engine, metadata



@asynccontextmanager
async def Lifespan(app: FastAPI):
    from models.post import posts #noqa
    
    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()
    

app = FastAPI(lifespan=Lifespan)
app.include_router(auth.router, tags=["auth"])
app.include_router(post.router, tags=["post"])