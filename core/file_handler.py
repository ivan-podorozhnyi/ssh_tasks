from abc import abstractmethod, ABC


class FileHandler(ABC):
    @abstractmethod
    def get_name(self):
        pass


class NoExtensionFileHandler(FileHandler):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return str(self._name)


class TxtFileHandler(FileHandler):
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name + '.txt'


class RemoteHomeFileHandler(FileHandler):
    def __init__(self, file: FileHandler, user_name: str):
        self.text = file
        self._user_name = user_name

    def get_name(self) -> str:
        print(self.text.get_name())
        return '/home/{}/{}'.format(self._user_name, self.text.get_name())
