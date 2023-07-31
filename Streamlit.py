import streamlit as st
import run
from ZyoutubeLink import download_youtube_video, reset_folder
import os
import shutil


def clear_directory(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


MEDIA_FOLDER = "Media"
YOUTUBE_FOLDER = "YoutubeDownloads"
out_dir = "downloads/testing"

# Making sure all directories exist
if not os.path.exists(MEDIA_FOLDER):
    os.makedirs(MEDIA_FOLDER)
if not os.path.exists(YOUTUBE_FOLDER):
    os.makedirs(YOUTUBE_FOLDER)
if not os.path.exists(out_dir):
    os.makedirs(out_dir)


def main():
    clear_directory(MEDIA_FOLDER)
    clear_directory(YOUTUBE_FOLDER)
    clear_directory(out_dir)

    st.title("Video Processing App")

    st.sidebar.header("Video Input")
    video_input_option = st.sidebar.selectbox(
        "Choose video input source", ["Upload a video", "Youtube link"]
    )

    st.header("Video Output")
    if video_input_option == "Upload a video":
        video_file = st.sidebar.file_uploader("Upload Video", type=["mp4"])
        if video_file is not None:
            video_path = os.path.join(MEDIA_FOLDER, video_file.name)
            with open(video_path, "wb") as f:
                f.write(video_file.getbuffer())
            st.sidebar.video(video_file)
            run.main(video_path)  # Processing video
    else:
        youtube_link = st.sidebar.text_input("Enter Youtube link")
        if youtube_link:
            reset_folder(YOUTUBE_FOLDER)
            video_path = download_youtube_video(youtube_link, YOUTUBE_FOLDER)
            st.sidebar.video(video_path)
            run.main(video_path)  # Processing video

    # Path to the processed video file
    PROCESSED_VIDEO_PATH = "downloads/testing/Translated.mp4"

    # Check if the processed video file exists and display it
    if os.path.isfile(PROCESSED_VIDEO_PATH):
        st.video(PROCESSED_VIDEO_PATH)
    else:
        st.write("Processed video not found")


if __name__ == "__main__":
    main()
