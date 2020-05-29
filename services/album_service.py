from models.album_model import AlbumModel

class AlbumService:
    def __init__(self):
        self.model = AlbumModel()

    def create(self, params):
        return self.model.create(params["title"])

    def list(self):
        return self.model.list()

    def delete(self, _id):
        return self.model.delete(_id)