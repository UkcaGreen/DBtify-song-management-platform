from models.album_model import AlbumModel


class AlbumService:
    def __init__(self):
        self.model = AlbumModel()

    def create(self, params):
        return self.model.create(params["album_title"], params["album_genre"], params["artist_id"])

    def update(self, params):
        return self.model.update(params["album_id"], params["album_title"], params["album_genre"])

    def list(self):
        return self.model.list()

    def get_by_id(self, _id):
        return self.model.get_by_id(_id)

    def delete(self, _id):
        return self.model.delete(_id)

    def like(self, params):
        return self.model.like(params["album_id"], params["listener_id"])

    def unlike(self, params):
        return self.model.unlike(params["album_id"], params["listener_id"])
