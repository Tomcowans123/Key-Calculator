from UIDesignFiles.Ui import *
import Globals
from functools import partial

class App(Ui_KeyCalc):
    def setupUi(self, KeyCalc):
        super(App, self).setupUi(KeyCalc)
        self.set_up_connections()
        self.update()

    #Sets Up the Changes and connections needed to connect the front end to te back end
    def set_up_connections(self):
        for button in self.frame.children():
            if isinstance(button, QtWidgets.QPushButton):
                button.clicked.connect(partial(self.set_global_root, button.text()))

        self.ModeSelector.currentIndexChanged.connect(lambda: self.set_global_mode(self.ModeSelector.currentText()))

        Globals.Global.key_changed.connect(self.update)

    def set_global_root(self, root):
        Globals.Global.root = root
        print(root)

    def set_global_mode(self, mode:str):
        Globals.Global.mode = mode

    def update(self):
        self.NotesBox.setText(', '.join(Globals.Global.key.notes))
        self.ChordsBox.setText(', '.join(Globals.Global.key.chords))
        self.Progression1.setText(', '.join(Globals.Global.key.progressions['progression 1']))
        self.Progression2.setText(', '.join(Globals.Global.key.progressions['progression 2']))
        self.Progression3.setText(', '.join(Globals.Global.key.progressions['progression 3']))