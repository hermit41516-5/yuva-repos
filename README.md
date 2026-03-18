# YUVA - Your User Authenticated Virtual Assistant

Developed by **Shubhangi Chakraverty**

A research-backed voice authentication and desktop virtual assistant system built using Python, MFCC feature extraction, and Gaussian Mixture Models.
# YUVA - Your User Authenticated Virtual Assistant

YUVA is a voice-authenticated desktop virtual assistant built using Python.
It uses MFCC feature extraction and Gaussian Mixture Models (GMM) for speaker authentication.

## Features

- Voice-based user authentication
- Desktop command execution
- Text-to-speech responses
- Offline authentication
- Web search support

## Technologies Used

- Python
- SpeechRecognition
- PyAudio
- Librosa (MFCC extraction)
- Scikit-learn (GMM model)
- Pyttsx3

## Installation

1. Clone the repository
git clone https://github.com/yourusername/YUVA-Voice-Assistant.git

cd YUVA-Voice-Assistant

2. Install dependencies

pip install -r requirements.txt


## Usage

### Step 1: Enroll User
## First Time Setup

Before using YUVA, you must enroll your voice:
python enroll.py

### Step 2: Run Assistant
python yuva.py

## Project Architecture

1. User Enrollment
2. Voice Authentication
3. Command Execution

## Research Paper

This project is based on the research:
"YUVA: Your User-authenticated Virtual Assistant"
