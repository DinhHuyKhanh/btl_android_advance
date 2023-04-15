from dotenv import load_dotenv
import os

from fastapi_mail import ConnectionConfig

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

#DATABASE 
drivername = 'mysql+mysqlconnector'
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
database = os.getenv('DB_DATABASE')

DATABASE = f"{drivername}://{username}:{password}@{host}:{port}/{database}"
#MEDIA
STATIC_MEDIA = os.getenv('STATIC_MEDIA')
SAVE_MODEL = os.getenv('SAVE_MODEL')

#EMAIL
EMAIL = ConnectionConfig(
    MAIL_USERNAME = os.getenv('MAIL_USERNAME'),
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD'),
    MAIL_FROM = os.getenv('MAIL_FROM'),
    MAIL_PORT = int(os.getenv('MAIL_PORT')),
    MAIL_SERVER = os.getenv('MAIL_SERVER'),
    MAIL_FROM_NAME = os.getenv('MAIL_FROM_NAME'),
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)
