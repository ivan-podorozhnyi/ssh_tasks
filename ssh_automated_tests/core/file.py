from abc import abstractmethod, ABC


class File(ABC):
    @abstractmethod
    def name(self):
        pass


class RawFile(File):
    def __init__(self, name):
        self._name = name

    def name(self):
        return str(self._name)


class TxtFile(File):
    def __init__(self, name: str):
        self._name = name

    def name(self) -> str:
        return self._name + '.txt'


class RemoteHomeFile(File):
    def __init__(self, file: File, user_name: str):
        self.text = file
        self._user_name = user_name

    def name(self) -> str:
        print(self.text.name())
        return '/home/{}/{}'.format(self._user_name, self.text.name())
