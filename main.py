from abc import abstractmethod, ABC
import requests


class RouteInterface(ABC):

    @abstractmethod
    def set_parameters(self, data: list) -> dict:
        pass

    @abstractmethod
    def get_parameters(self) -> dict:
        pass

    @abstractmethod
    def set_response(self, data: list) -> dict:
        pass

    @abstractmethod
    def get_response(self) -> dict:
        pass

    @abstractmethod
    def send(self, uri: str, method: str = 'GET') -> None:
        pass


class Route(RouteInterface):
    APP_ID = '2750bc42-702e-4cbe-bae5-798f171389e1'
    _parameters = []
    _response = []

    def set_parameters(self, **data: dict) -> dict:
        self._parameters = data
        return self._parameters

    def get_parameters(self) -> dict:
        return self._parameters

    def set_response(self, data: dict) -> dict:
        self._response = data
        return self._response

    def get_response(self) -> dict:
        return self._response

    def send(self, uri: str, method: str = 'GET') -> None:
        params = self.get_parameters()
        url = 'http://core.webstktw.beget.tech/api/v0/apps/' + self.APP_ID + uri
        request = requests.request(method=method, url=url, json=params)
        response = request.text
        self.set_response(response)
        print(self.get_response())
