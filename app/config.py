import os
from dotenv import load_dotenv  

load_dotenv()

class AppConfig:
    secretKey = os.getenv("secretKey")
    databaseUrl = os.getenv("databaseUrl")
    sqlalchemyTrackModifications = False
