from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from .schemas import PostBase, PostInDb, PostCreate, Post
import uuid
from ..inference.segment import get_and_save_image_embedding
from db import crud

router = APIRouter(prefix="/posts")

@router.get("/p/{post_id}")
def get_post(post_id: str):
    return {'post_id': post_id }


@router.get("/all_posts")
def get_all_posts() -> str:
    test =  crud.post.get_all()
    print(test)
    return 'This should work'


@router.post("/create", response_model=Post)
async def create_post(
    file: UploadFile = File(), 
    title:str =  Form(), description: str = Form(), 
    owner: str = 'Jinbesan'):
    """Create Post Draft

    Args:
        file (UploadFile, optional): Image file to be uploaded
        title (str, optional): Title of the post
        description (str, optional): Description of the post
        owner (str, optional): Owner of the post

    Raises:
        HTTPException: HTTP Exception 422 if uploaded file is not an image

    Returns:
        _type_: Post Draft
    """
    if file.content_type.split("/")[0] != "image":
        raise HTTPException(
            422, detail="Input file must be an image")
    
    post_id = uuid.uuid4().hex
    filepath = await get_and_save_image_embedding(file.file, post_id)
    
    post = PostInDb(title=title, description=description, post_id=post_id,
                    owner_id=owner, draft=True)
    
    crud.post.create(obj=post)
    return post

@router.patch("/create", response_model=PostInDb)
async def publish_post(post:PostInDb):
    """If we choose to publish the post, update everything with the new post 
    details but the difference is that the draft column will become false
    """
    post.draft = False
    crud.post.publish(obj=post)
    return post