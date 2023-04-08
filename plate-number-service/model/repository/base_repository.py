from model.database import SessionLocal

class BaseRepository():

    def __init__(self) -> None:
        self.db = SessionLocal()