from models.song_model import SongModel

class SongService:
    def __init__(self):
        self.model = SongModel()

    def create(self, params):
        return self.model.create(params["title"])

    def update(self, params):
        return self.model.update(params["id"], params["title"])

    def list(self):
        return self.model.list()

    def delete(self, _id):
        return self.model.delete(_id)