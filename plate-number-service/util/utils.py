
import json
from sqlalchemy.orm import class_mapper

def convert_model_to_json(my_object, model):
    columns = model.__table__.columns.keys()
    my_json = {c: getattr(my_object, c) for c in columns}
    return my_json