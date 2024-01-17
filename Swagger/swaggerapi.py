from main import Route


class BotList(Route):
    def send(self, uri: str, method: str = 'GET') -> None:
        self.set_parameters()
        return super().send(method=method, uri=uri)


class BotDetails(Route):
    def send(self, uri: str, method: str = 'GET') -> None:
        bot_id = uri.split('/')[1]
        self.set_parameters(id=str(bot_id))
        return super().send(method=method, uri=uri)


class Register(Route):
    def send(self, uri: str, method: str = 'POST') -> None:
        self.set_parameters(email='abc@mail.com', password='123456abcerq')
        return super().send(method=method, uri=uri)


class Login(Route):
    def send(self, uri: str, method: str = 'POST') -> None:
        self.set_parameters(email='abc@mail.com', password='123456abcerq')
        return super().send(method=method, uri=uri)
