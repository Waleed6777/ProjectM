# enhancer.py

import numpy as np
import librosa
import soundfile as sf
from scipy.signal import butter, lfilter

# =======================
# Utility Functions
# =======================
def high_pass_filter(y, sr, cutoff=80):
    b, a = butter(N=2, Wn=cutoff / (sr / 2), btype='high', analog=False)
    return lfilter(b, a, y)

def noise_gate(y, threshold_db=-40):
    threshold = 10 ** (threshold_db / 20)
    return np.where(np.abs(y) < threshold, 0, y)

def compress(y, threshold_db=-20, ratio=3.0):
    threshold = 10 ** (threshold_db / 20)
    y_out = y.copy()
    mask = np.abs(y) > threshold
    y_out[mask] = np.sign(y[mask]) * (threshold + (np.abs(y[mask]) - threshold) / ratio)
    return y_out

def saturate(y, drive=1.5):
    return np.tanh(drive * y)

def apply_eq(y, sr, use_genre_eq=False):
    # Placeholder: basic sculpting
    y_eq = y.copy()
    if not use_genre_eq:
        # De-mud ~ cut 300–500 Hz, boost presence 4–6 kHz
        b1, a1 = butter(1, [300 / (sr/2), 500 / (sr/2)], btype='bandstop')
        y_eq = lfilter(b1, a1, y_eq)
        b2, a2 = butter(1, [4000 / (sr/2), 6000 / (sr/2)], btype='bandpass')
        y_eq += 0.15 * lfilter(b2, a2, y_eq)
    else:
        # Genre-specific EQ placeholder
        pass  # to be implemented later
    return y_eq

def limiter(y, ceiling_db=-0.1):
    ceiling = 10 ** (ceiling_db / 20)
    return np.clip(y, -ceiling, ceiling)

# =======================
# Main Enhancement Function
# =======================
def enhance_audio(input_path, output_path, use_genre_eq=False, volume_boost_db=1.5, apply_noise_gate=True):
    y, sr = librosa.load(input_path, sr=None)

    y = high_pass_filter(y, sr)

    if apply_noise_gate:
        y = noise_gate(y)

    y = compress(y)
    y = saturate(y)
    y = apply_eq(y, sr, use_genre_eq=use_genre_eq)

    # Apply volume boost
    boost = 10 ** (volume_boost_db / 20)
    y *= boost

    # Final limiter
    y = limiter(y)

    # Normalize to -1 to 1 to avoid writing clipped files
    y /= max(np.abs(y)) + 1e-9

    sf.write(output_path, y, sr)
    print(f"Enhanced audio saved to: {output_path}")

# =======================
# Example CLI Entry (for dev)
# =======================
if __name__ == '__main__':
    enhance_audio(
        input_path='input.wav',
        output_path='output.wav',
        use_genre_eq=False,
        volume_boost_db=1.5,
        apply_noise_gate=True
    )
