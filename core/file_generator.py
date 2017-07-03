from abc import abstractmethod, ABC


class FileGenerator(ABC):
    @abstractmethod
    def get_name(self):
        pass


class TxtFileGenerator(FileGenerator):
    def __init__(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name + '.txt'


class RemoteHomeFileGenerator(FileGenerator):
    def __init__(self, file: FileGenerator, user_name: str):
        self.text = file
        self._user_name = user_name

    def get_name(self) -> str:
        print(self.text.get_name())
        return '/home/{}/{}'.format(self._user_name, self.text.get_name())
