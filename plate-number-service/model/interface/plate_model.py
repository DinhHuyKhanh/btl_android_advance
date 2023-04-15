
class PlateModel():
    def register(self, plate=None):
        raise NotImplementedError
    
    def update(self, id, plate=None):
        raise NotImplementedError

    def get_plate_by_id(self, id=None):
        raise NotImplementedError