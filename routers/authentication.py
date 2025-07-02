from fastapi import APIRouter, Depends, HTTPException, status
import schemas, db, models
from sqlalchemy.orm import Session
from hashing import Hash
import auth_token as token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid Credentials")
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Incorrect Password")
    
    #if everything is good then generate the jwt token:

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type":"bearer"}
