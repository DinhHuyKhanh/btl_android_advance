from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

#DATABASE 
# DATABASE URL
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