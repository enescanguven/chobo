from pymongo import MongoClient
from helpers.settings import settings
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
import json
from pydantic import ValidationError

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"/api/v1/auth/oauth2"
)


def get_database():
    client = MongoClient(settings.MONGO_CONNECTION_STRING)
    return client['brainbrew']
