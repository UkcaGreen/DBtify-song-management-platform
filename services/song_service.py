from models.song_model import SongModel


class SongService:
    def __init__(self):
        self.model = SongModel()

    def create(self, params):
        return self.model.create(params["song_title"], params["album_id"], params["artist_id"], params["other_artists"])

    def update(self, params):
        return self.model.update(params["song_id"], params["song_title"])

    def list(self):
        return self.model.list()

    def get_by_album_id(self, album_id):
        return self.model.get_by_album_id(album_id)

    def delete(self, _id):
        return self.model.delete(_id)

    def like(self, params):
        return self.model.like(params["song_id"], params["listener_id"])

    def unlike(self, params):
        return self.model.unlike(params["song_id"], params["listener_id"])
