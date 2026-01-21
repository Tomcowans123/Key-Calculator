from Config.KeyClassConfig import Key, Mode
from PySignal import Signal

class GlobalKey:
    def __init__(self):
        self._root:str = 'c'
        self._mode:str = 'major'
        self._key:Key = Key(self._root, self._mode)
        self.key_changed = Signal()

    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, value):
        self._key = value
        self.key_changed.emit()
    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, value):
        self._root = value
        self.key = Key(value, self.mode)
    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self, value):
        self._mode = value
        self.key = Key(self.root, value)


Global = GlobalKey()