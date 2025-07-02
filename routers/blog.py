from fastapi import APIRouter, Depends, status, Response
import schemas, db
from typing import List
from sqlalchemy.orm import Session
from repository import blog
import oauth2

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

get_db = db.get_db

# Get all the blogs 
@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

#add a new blog:
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

#delete the blog:
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)

#update the blog:
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)