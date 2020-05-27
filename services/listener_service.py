from models.listener_model import ListenerModel

class ListenerService:
    def __init__(self):
        self.model = ListenerModel()

    def create(self, params):
        return self.model.create(params["username"], params["email"])

    def list(self):
        return self.model.list()

    def delete(self):
        return self.model.delete()