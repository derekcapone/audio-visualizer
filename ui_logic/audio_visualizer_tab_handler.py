from PySide6.QtWidgets import QWidget
from ui_generated.audio_visualizer_tab import Ui_AudioVisualizerTab

class AudioVisualizerTab(QWidget, Ui_AudioVisualizerTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)