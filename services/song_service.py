from models.song_model import SongModel


class SongService:
    def __init__(self):
        self.model = SongModel()

    def create(self, params):
        return self.model.create(params["title"])

    def update(self, params):
        return self.model.update(params["id"], params["title"])

    def list(self, params):
        if params["artist"] is not None and params["album"] is not None:
            pass
        elif params["artist"] is not None:
            result = self.model.list_by_artist(params["artist"])
        elif params["album"] is not None:
            result = self.model.list_by_album(params["album"])
        else:
            result = self.model.list_all()

        return result

    def delete(self, _id):
        return self.model.delete(_id)
