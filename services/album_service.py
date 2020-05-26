from models.album_model import AlbumModel

class AlbumService:
    def __init__(self):
        self.model = AlbumModel()
        
    def create(self, params):
        self.model.create(params["title"], params["genre"])

    def getAll(self, params):
        self.model.getAll()