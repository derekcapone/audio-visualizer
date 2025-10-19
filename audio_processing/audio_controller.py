from PySide6.QtCore import QObject, Signal, QTimer
from audio_processing.audio_source import AudioSource

class AudioController(QObject):
    data_ready = Signal(object)  # emits NumPy array chunks

    def __init__(self, audio_source: AudioSource, interval_ms=30):
        super().__init__()

        self.audio_source = audio_source

        self.timer = QTimer()
        self.timer.timeout.connect(self._on_timer)
        self.timer.setInterval(interval_ms)

    def start(self):
        self.audio_source.start()
        self.timer.start()

    def stop(self):
        self.audio_source.stop()
        self.timer.stop()

    def _on_timer(self):
        if not self.audio_source.is_active():
            self.stop()
            return
        data = self.audio_source.read_chunk()
        if data.size > 0:
            self.data_ready.emit(data)

