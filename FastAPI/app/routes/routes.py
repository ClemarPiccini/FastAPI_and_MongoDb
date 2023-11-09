from fastapi import APIRouter
from controllers.controllers import print_db

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/ListarDataBase")
def read_root():
    return {print_db}

