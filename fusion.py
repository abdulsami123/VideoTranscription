def read_transcription(file_path):
    """
    Reads a transcription file with plain text.
    Returns the entire text as a single string.
    """
    with open(file_path, 'r') as file:
        transcription = file.read().strip()
    return transcription

def read_diarization(file_path):
    """
    Reads the diarization file and returns a list of dictionaries.
    Each dictionary contains the speaker, start time, and end time.
    """
    diarization_data = []
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(": ")
            speaker = parts[0]  # e.g., "Speaker 0"
            times = parts[1].split(" - ")
            start_time = float(times[0])  # Convert start time to float
            end_time = float(times[1])    # Convert end time to float
            diarization_data.append({
                "speaker": speaker,
                "start_time": start_time,
                "end_time": end_time
            })
    return diarization_data

def segment_transcription(transcription, diarization_data, words_per_second=2):
    """
    Segments the transcription based on diarization data.
    Assumes a basic words-per-second rate for rough alignment.
    """
    words = transcription.split()
    total_duration = diarization_data[-1]["end_time"]
    approx_total_words = len(words)
    words_per_second = approx_total_words / total_duration  # Calculate a better words per second rate
    
    segments = []
    word_index = 0
    
    for entry in diarization_data:
        speaker = entry["speaker"]
        start_time = entry["start_time"]
        end_time = entry["end_time"]
        
        # Calculate number of words that fit in the current segment
        num_words = int((end_time - start_time) * words_per_second)
        segment_text = " ".join(words[word_index:word_index + num_words])
        
        segments.append(f"{speaker}: {segment_text}")
        word_index += num_words
    
    return segments

def save_dialogue(segments, output_file):
    """
    Saves the combined dialogue into a text file.
    """
    with open(output_file, 'w') as file:
        for segment in segments:
            file.write(segment + "\n")
    
    print(f"Dialogue manuscript saved to {output_file}")

# Main Functionality
transcription_file = "transcribed_output.txt"
diarization_file = "diarizatrion_output.txt"
output_file = "dialogue_manuscript.txt"

# Read transcription and diarization data
transcription = read_transcription(transcription_file)
diarization_data = read_diarization(diarization_file)

# Segment the transcription according to diarization timestamps
dialogue_segments = segment_transcription(transcription, diarization_data)

# Save the final dialogue manuscript
save_dialogue(dialogue_segments, output_file)
