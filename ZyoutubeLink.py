import os
import subprocess
from pytube import YouTube
import shutil


def download_youtube_video(youtube_url, output_dir):
    youtubeObject = YouTube(youtube_url)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        # Download the video to the output directory
        video_path = youtubeObject.download(output_path=output_dir)
        print("Download is completed successfully")
        return video_path
    except Exception as e:
        print(f"An error has occurred: {e}")


def reset_folder(folder_path):
    # Delete the folder if it exists
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)

    # Create the folder
    os.makedirs(folder_path)
