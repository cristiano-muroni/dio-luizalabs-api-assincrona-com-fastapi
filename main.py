import databases
import sqlalchemy as sa
from fastapi import FastAPI
from controllers import post
from contextlib import asynccontextmanager

DATABASE_URL = "sqlite:///./blog.db"

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()
engine = sa.create_engine(DATABASE_URL, connect_args= {"check_same_thread": False})

@asynccontextmanager
async def Lifespan(app: FastAPI):
    from models.post import posts #noqa
    
    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()
    

app = FastAPI(lifespan=Lifespan)
app.include_router(post.router)   