from fastapi import FastAPI
from .database import Base, engine
from .routers import auth, tasks
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Management API")

app.include_router(auth.router)
app.include_router(tasks.router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "API Running 🚀"}