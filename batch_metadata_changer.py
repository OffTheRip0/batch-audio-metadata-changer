import os
import sounddevice as sd
from pydub import AudioSegment


def play_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    samples = audio.get_array_of_samples()
    sample_rate = 48000*1.83

    sd.play(samples, sample_rate)


def rename_audio_files(folder_path):
    audio_files = [file for file in os.listdir(folder_path) if file.endswith((".mp3", ".wav"))]

    for file_name in audio_files:
        file_path = os.path.join(folder_path, file_name)
        print(f"\nCurrently playing: {file_name}")
        play_audio(file_path)

        new_title = input("Enter song name: ")
        new_artist = input("Enter artist name: ")

        audio = AudioSegment.from_file(file_path)
        audio.export(file_path, format="mp3", bitrate="320k", tags={'title': new_title, 'artist': new_artist})
        print("Metadata updated successfully!")
        play_audio(file_path)


folder_path = r"C:\\path\\to\folder\\here"

rename_audio_files(folder_path)
