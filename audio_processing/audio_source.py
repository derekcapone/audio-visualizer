from abc import ABC, abstractmethod
import numpy as np
import soundfile as sf

class AudioSource(ABC):
    @abstractmethod
    def start(self):
        """Begin producing audio data."""
        pass

    @abstractmethod
    def stop(self):
        """Stop producing audio data."""
        pass

    @abstractmethod
    def read_chunk(self) -> np.ndarray:
        """Return the next chunk of audio samples as a NumPy array."""
        pass

    @abstractmethod
    def is_active(self) -> bool:
        """Return True if there is still data to process."""
        pass


class FileAudioSource(AudioSource):
    """
    Reads audio from file and generates chunks of audio samples to be read.
    Implements abstract base class AudioSource.
    """
    def __init__(self, file_path, chunk_size=1024):
        self.file, self.samplerate = sf.read(file_path, always_2d=False)
        self.chunk_size = chunk_size
        self.position = 0
        self.active = True

    def start(self):
        self.position = 0
        self.active = True

    def stop(self):
        self.active = False

    def read_chunk(self):
        if not self.active:
            return np.array([])
        start = self.position
        end = start + self.chunk_size
        chunk = self.file[start:end]
        self.position = end
        if end >= len(self.file):
            self.active = False
        return chunk

    def is_active(self):
        return self.active


if __name__ == "__main__":
    test_file_path = "/home/caponed/Desktop/Projects/audio-visualizer/test/sine_440Hz.wav"


