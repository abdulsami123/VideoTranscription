import yt_dlp
import whisper

def download_audio(youtube_url, output_path='audio.mp3'):
    if not youtube_url:
        raise ValueError("You must provide a valid YouTube URL.")
    
    # Use yt-dlp to download the audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_path,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    return output_path

def transcribe_audio(audio_path, output_text_path='transcription1.txt'):
    # Load the Whisper model
    model = whisper.load_model('base')  # You can use 'base', 'small', 'medium', 'large' based on your needs.
    
    # Transcribe the audio
    result = model.transcribe(audio_path)
    
    # Write the transcription to a text file
    with open(output_text_path, 'w', encoding='utf-8') as f:
        f.write(result['text'])
    
    print(f'Transcription saved to {output_text_path}')

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ").strip()
    if youtube_url:
        try:
            #audio_path = download_audio(youtube_url)
            transcribe_audio("audio.mp3")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Error: No URL provided.")
