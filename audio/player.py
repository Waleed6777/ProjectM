
import sounddevice as sd

def play_audio(audio_data, samplerate):
    """
    Play the given audio_data (numpy array) at samplerate Hz.
    """
    sd.play(audio_data, samplerate)
    sd.wait()  # block until done
