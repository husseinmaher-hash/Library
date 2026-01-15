import os
from dotenv import load_dotenv  

load_dotenv()

class AppConfig:
    secretKey = os.getenv("SECRET_KEY")
    databaseUrl = os.getenv("DATABASE_URL")
    sqlalchemyTrackModifications = False
