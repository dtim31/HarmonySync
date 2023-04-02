from PyQt5.QtWidgets import *
from gui import CustomQt

class SettingsWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(100, 100, 1200, 800)