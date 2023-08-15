from typing import Optional

from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    description: Optional[str] = None

class PostCreate(PostBase):
    pass


class PostInDb(PostBase):
    post_id:str
    owner_id: str
    draft: bool

class Post(PostInDb):
    pass

    