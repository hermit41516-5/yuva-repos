import numpy as np
import librosa
import pickle
import sounddevice as sd
from scipy.io.wavfile import write
import joblib

SAMPLE_RATE = 16000
DURATION = 4

def record_test_audio():
    print("Speak for authentication...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1)
    sd.wait()
    write("audio_samples/test.wav", SAMPLE_RATE, audio)

def extract_features(file):
    audio, sr = librosa.load(file, sr=16000)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    return mfcc.T

def authenticate():
    with open("models/user_model.pkl", "rb") as f:
        gmm = pickle.load(f)

    record_test_audio()
    # Load scaler
    scaler = joblib.load("models/scaler.pkl")

    features = extract_features("audio_samples/test.wav")
    features = scaler.transform(features.astype(np.float64))

    score = gmm.score(features)

    print("Authentication score:", score)

    if score > -50:   # threshold tuning needed
        print("Access Granted")
        return True
    else:
        print("Access Denied")
        return False
