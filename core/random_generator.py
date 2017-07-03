import random
import string


class RandomGenerator(object):
    def __init__(self, length: int):
        self._length = length

    def generate_string(self, output: str) -> str:
        if output == 'string':
            return ''.join(random.sample(string.ascii_letters, self._length))
        elif output == 'digits':
            return ''.join(random.sample(string.digits, self._length))
        else:
            raise Exception('Can\'t generate string')
