# YouTube Video Clipper

## Overview

YouTube Video Clipper is a Python-based application that allows users to download and clip specific segments from YouTube videos. The application provides both GUI and CSV file processing capabilities, making it easy to handle multiple video URLs and timestamps. This project uses `yt-dlp` for downloading YouTube videos and `moviepy` for video processing.

## Features

- Download videos from YouTube.
- Clip specific segments from downloaded videos.
- Process multiple video URLs and timestamps from a CSV file.
- Simple and user-friendly GUI with Tkinter.
- Generate unique filenames for clipped videos based on the current timestamp.

## Installation

### Using the Installer

1. **Download the Installer**: Go to the [GitHub Releases page](https://github.com/Awesome-Ace22/YouTube-Video-Clipper/releases) and download the latest `YouTubeVideoClipperInstaller.msi` (on Windows) or `YouTubeVideoClipperInstaller.dmg`(on macOS). The installer will guide you through the installation process.

2. **Launch the Application**: Once the installation is complete, you can launch the YouTube Video Clipper from the Start Menu (on Windows) or the Applications folder (on macOS).

### Manual Installation

1. Clone the repository or download the source code.

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv clipper_env
    source clipper_env/Scripts/activate  # On Windows
    source clipper_env/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

#### Using the Installed Version

1. **Launch the Application**: Open YouTube Video Clipper from the Start Menu (on Windows) or the Applications folder (on macOS).

2. **Using the GUI**:
    - Process a CSV file containing video URLs and timestamps.
    - Enter a single video URL and timestamps directly into the GUI.

#### Running from Source

1. Save your Python script as `youtube_video_clipper.py`.

2. Run the script:
    ```bash
    python youtube_video_clipper.py
    ```

3. The Tkinter GUI will open. You can either:
    - Process a CSV file containing video URLs and timestamps.
    - Enter a single video URL and timestamps directly into the GUI.

### CSV File Format

The CSV file should have the following columns:
- `url`: The URL of the YouTube video.
- `start_timestamp`: The start timestamp of the clip (format: `HH:MM:SS`).
- `end_timestamp`: The end timestamp of the clip (format: `HH:MM:SS`).

Example:
```csv
url,start_timestamp,end_timestamp
https://www.youtube.com/watch?v=example1,00:01:00,00:02:00
https://www.youtube.com/watch?v=example2,00:03:00,00:04:30
