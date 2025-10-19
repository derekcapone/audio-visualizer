from PySide6.QtWidgets import QMainWindow, QApplication
from ui_generated.main_window import Ui_MainWindow
from ui_logic.audio_visualizer_tab_handler import AudioVisualizerTab


class MainApplication(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tab1_widget = AudioVisualizerTab()
        self.main_tab_widget.addTab(self.tab1_widget, "Audio Visualizer")

# Run the application
if __name__ == "__main__":
    app = QApplication([])
    window = MainApplication()
    window.show()
    app.exec()