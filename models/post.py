import sqlalchemy as sa
from main import metadata


posts = sa.Table(
    'posts', metadata,
     sa.column("id", sa.Integer, primary_key=True),
     sa.column("title", sa.String(150), nullable=False, unique=True),
     sa.column("content", sa.String(150), nullable=False),
     sa.column("published_at", sa.DateTime(), nullable=True),
     sa.column("published", sa.Boolean(), default=False),   
     
)