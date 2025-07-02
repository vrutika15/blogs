from pydantic import BaseModel
from typing import List, Optional, ForwardRef


ShowBlog = ForwardRef("ShowBlog")


class BlogBase(BaseModel):
    title : str
    body : str

class Blog(BlogBase):
    class Config():
        orm_mode = True

#Create The User using the base model:
class User(BaseModel):
    name: str
    email: str
    password: str

#show only the name and the and email:
class ShowUser(User):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True


class ShowBlog(Blog):
    title: str
    body: str
    creator : Optional[ShowUser]

    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    emai: Optional[str] = None
