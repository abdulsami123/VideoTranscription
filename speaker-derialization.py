from pyannote.audio import Pipeline
import torch
from dotenv import load_dotenv
import os 

load_dotenv()
api_key_hf: str = os.environ.get("key")

# Load pre-trained pipeline
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1" , use_auth_token= api_key_hf)

# send pipeline to GPU (when available)
pipeline.to(torch.device("cuda"))

# Apply pipeline to an audio file
diarization = pipeline("audio.mp3")

# Format the diarization result into readable text
with open("transcription2.txt", "w") as f:
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        f.write(f"{speaker}: {turn.start:.1f} - {turn.end:.1f}\n")


