import configparser
from abc import ABC, abstractmethod

import paramiko

from ssh_automated_tests.core.file import File


class User(ABC):
    @abstractmethod
    def connection_data(self):
        pass


class SshUser(User):
    def __init__(self, name: str, port: int, key: str, address: str):
        self._name = name
        self._port = port
        self._key = key
        self._address = address

    def connection_data(self):
        return {"hostname": self._address, "port": self._port,
                "username": self._name, "pkey": self._key}


class ParamikoUser(User):
    def __init__(self, name: str, port: int, key: str, address: str):
        self._name = name
        self._port = port
        self._key = key
        self._address = address

    def connection_data(self):
        pkey = paramiko.RSAKey.from_private_key_file(self._key)
        return {"hostname": self._address, "port": self._port,
                "username": self._name, "pkey": pkey}


class ParamikoUserFromPropFile(User):
    def __init__(self, file: File):
        self._config_file = file
        self._config = configparser.ConfigParser()

    def connection_data(self):
        self._config.read(self._config_file.name())
        user = ParamikoUser(self._config.get('connection', 'user_name'),
                       int(self._config.get('connection', 'port')),
                       self._config.get('connection', 'key'),
                       self._config.get('connection', 'ip_address'))
        return user.connection_data()
