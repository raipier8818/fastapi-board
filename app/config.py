import os
import dotenv


dotenv.load_dotenv()

class MongoDBConfig():
    def __init__(self):
        self.MONGO_URI = os.getenv('MONGO_URI')
        self.MONGO_DB_NAME = os.getenv('MONGO_DB_NAME')

class RedisConfig():
    def __init__(self):
        self.REDIS_HOST = os.getenv('REDIS_HOST')
        self.REDIS_PORT = os.getenv('REDIS_PORT')
        self.REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
        
class AppConfig():
    def __init__(self) -> None:
        self.PORT = os.getenv('PORT')
        self.ENV = os.getenv('ENV') or 'development'

class GoogleOauthConfig():
    def __init__(self) -> None:
        self.GOOGLE_OAUTH_CLIENT_ID = os.getenv('GOOGLE_OAUTH_CLIENT_ID')
        self.GOOGLE_OAUTH_CLIENT_SECRET = os.getenv('GOOGLE_OAUTH_CLIENT_SECRET')
        self.GOOGLE_OAUTH_CALLBACK_URI = os.getenv('GOOGLE_OAUTH_CALLBACK_URI')
        
class SessionConfig():
    def __init__(self) -> None:
        self.SECRET_KEY = os.getenv('SECRET_KEY')
        
class Config():
    def __init__(self) -> None:
        self.app = AppConfig()
        self.mongodb = MongoDBConfig()
        self.redis = RedisConfig()
        self.google_oauth = GoogleOauthConfig()
        self.session = SessionConfig()

config = Config()