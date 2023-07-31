# ./ /run.py
from vTranslate import VTranslator
import config as settings
import os


def main(input_file_path):
    openaiKey = settings.Token1
    xi_api_key = settings.Token2
    out_dir = "downloads/testing"

    # Ensure output directory exists
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    processor = VTranslator(
        out_dir,
        input_file_path,
        openaiKey,
        xi_api_key,
    )

    # Process the video
    output_file_path = processor.process_video()

    return output_file_path


if __name__ == "__main__":
    main("path_to_your_test_video_file")
