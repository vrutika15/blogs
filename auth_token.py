from datetime import datetime, timedelta
from jose import JWTError, jwt
from jwt import ExpiredSignatureError, InvalidTokenError
import schemas
from dotenv import load_dotenv
import os
load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Secret key and algorithm

def create_access_token(data: dict) -> str:
    # Create a copy of the data to avoid modifying the original dictionary
    to_encode = data.copy()
    
    # Set the expiration time for the token
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  # Add expiration time

    # Use "sub" (subject) for user identification
    if "sub" in data:
        to_encode.update({"sub": data["sub"]})  # Use 'sub' as the subject key
    
    # Encode the JWT with the specified secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print(f"Generated Token: {encoded_jwt}") 
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try:
        # Decode the JWT token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")  # 'sub' contains the user email
        
        if email is None:
            raise credentials_exception
        
        # Return the token data (user's email)
        token_data = schemas.TokenData(email=email)
        print(f"Token is valid for user: {email}")  
        return token_data

    except ExpiredSignatureError:
        raise credentials_exception  # Token has expired
    except JWTError as e:
        print(f"Error decoding token: {e}")
        raise credentials_exception  # General JWT error (invalid signature, etc.)
