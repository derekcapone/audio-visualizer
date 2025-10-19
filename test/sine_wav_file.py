import numpy as np
import wave
import struct

# Parameters
frequency = 440  # Hz
duration = 10  # seconds
sample_rate = 44100  # samples per second
amplitude = 32767  # Max amplitude for 16-bit audio

# Generate the sine wave
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
sine_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Open a .wav file
with wave.open("sine_440Hz.wav", "w") as wav_file:
    n_channels = 1
    sampwidth = 2  # 16-bit audio
    n_frames = len(sine_wave)
    comptype = "NONE"
    compname = "not compressed"

    wav_file.setparams((n_channels, sampwidth, sample_rate, n_frames, comptype, compname))

    # Write frames
    for sample in sine_wave:
        wav_file.writeframes(struct.pack('h', int(sample)))

print("sine_440Hz.wav generated successfully!")
