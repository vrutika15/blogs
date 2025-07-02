from sqlalchemy.orm import Session
import schemas
import models
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id: int, db: Session):
    db.query(models.Blog).filter(models.Blog.id == id)
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Done'

def update(id: int,request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    update_data = request.dict(exclude_unset=True)
    blog.update(update_data)
    db.commit()
    return 'updated'

def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    #if id is not found then:
    # response.status_code = status.HTTP_404_NOT_FOUND
    # return {'detail': f"Blog with the id {id} is not available"}
    return blog