from dotenv import load_dotenv
from datetime import timedelta
import os 

load_dotenv()

class Config:
    JWT_SECRET_KEY=os.getenv("JWT_SECRET_KEY")
    DATABASE=os.getenv("DATABASE")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)