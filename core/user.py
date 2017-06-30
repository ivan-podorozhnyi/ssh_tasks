from abc import ABC


class User(ABC):
    pass


class SshUser(User):
    def __init__(self, name: str, port: int, key: str, address: str):
        self._name = name
        self._port = port
        self._key = key
        self._address = address

    def make_connection_data(self):
        return {"hostname": self._address, "port": self._port,
                "username": self._name, "key": self._key}

