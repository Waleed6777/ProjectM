from audio.file_loader import load_file
from audio.player import play_audio

if __name__ == "__main__":
    filepath = "test.wav"  # Name your WAV file exactly this
    audio_data, sr = load_file(filepath)
    print(f"Playing '{filepath}' at {sr} Hz...")
    play_audio(audio_data, sr)
