from fastapi import HTTPException
from model.models import databases

def print_db():

    for database in databases:
        print(database)
        return database