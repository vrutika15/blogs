from fastapi import FastAPI
import models
from db import engine
import uvicorn
from routers import blog, user, authentication

app = FastAPI()

#to drop the database: 
# models.Base.metadata.drop_all(engine)
#to create the database:
models.Base.metadata.create_all(engine)
# print("Database reset completed.")

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


@app.get('/')
def read_root():
    return {'data':'home'}


# if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=7000)