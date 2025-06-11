import soundfile as sf

def load_file(filepath="test.wav"):
    """
    Load an audio file and return (data, samplerate).
    """
    data, samplerate = sf.read(filepath)
    return data, samplerate

