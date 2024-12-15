import os
import pandas as pd
from moviepy import *
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import yt_dlp
from datetime import datetime
import sys

class RedirectText(object):
    def __init__(self, widget):
        self.widget = widget

    def write(self, message):
        self.widget.insert(tk.END, message)
        self.widget.see(tk.END)

    def flush(self):
        pass

def download_and_clip_video(url, start_timestamp, end_timestamp, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    # Generate a unique clip file name based on the current timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    clip_filename = os.path.join(output_dir, f"cliped_video_{timestamp}.mp4")

    # Define the output path for the downloaded video
    downloaded_path = os.path.join(output_dir, f"downloaded_video_{timestamp}.mp4")


    # Download the video using yt-dlp
    ydl_opts = {
        'format': 'best',
        'outtmpl': downloaded_path,
        'noplaylist': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return

    # Clip the video
    try:
        with VideoFileClip(downloaded_path) as video:
            print(f"Clipping video from {start_timestamp} to {end_timestamp}")
            # Ensure start_timestamp and end_timestamp are in seconds
            start_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start_timestamp.split(":"))))
            end_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(end_timestamp.split(":"))))
            #clipped_video = video.subclipped(start_seconds, end_seconds)
            clipped_video = video.subclipped(start_timestamp, end_timestamp)
            clipped_video.write_videofile(clip_filename, codec='libx264', audio_codec='aac')
    except AttributeError as e:
        print(f"Failed to clip video: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while clipping the video: {e}")
    finally:
        # Clean up the downloaded video
        if os.path.exists(downloaded_path):
            pass # os.remove(downloaded_path)


def download_and_clip_videos(csv_file, output_dir):
    # Read the CSV file
    data = pd.read_csv(csv_file)

    # Ensure the output directory exists
    output_sub_dir = os.path.join(output_dir, f"video_clips")
    os.makedirs(output_sub_dir, exist_ok=True)

    # Process each row in the CSV
    for index, row in data.iterrows():
        url = row['url']
        start_timestamp = row['start_timestamp']
        end_timestamp = row['end_timestamp']

        print(f"Processing video {index + 1} from {url}")
        download_and_clip_video(url, start_timestamp, end_timestamp, output_sub_dir)

def process_csv_file():
    csv_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if not csv_file:
        return
    output_dir = filedialog.askdirectory()
    if not output_dir:
        return
    try:
        download_and_clip_videos(csv_file, output_dir)
        messagebox.showinfo("Success", "Videos processed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process videos: {e}")


def process_single_url():
    url = url_entry.get()
    start_timestamp = start_entry.get()
    end_timestamp = end_entry.get()
    if not (url and start_timestamp and end_timestamp):
        messagebox.showerror("Error", "Please fill in all fields!")
        return

    output_dir = filedialog.askdirectory()
    if not output_dir:
        return

    print(f"Processing video from {url}")
    download_and_clip_video(url, start_timestamp, end_timestamp, output_dir)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("YouTube Video Clipper")

    frame = tk.Frame(root)
    frame.pack(pady=10, padx=10)

    tk.Label(frame, text="Enter a Single URL:").grid(row=1, column=0, columnspan=2)

    url_entry = tk.Entry(frame, width=50)
    url_entry.grid(row=2, column=0, columnspan=2, pady=5)

    tk.Label(frame, text="Start Timestamp (hh:mm:ss):").grid(row=3, column=0)
    start_entry = tk.Entry(frame)
    start_entry.grid(row=3, column=1)

    tk.Label(frame, text="End Timestamp (hh:mm:ss):").grid(row=4, column=0)
    end_entry = tk.Entry(frame)
    end_entry.grid(row=4, column=1)

    single_url_button = tk.Button(frame, text="Process Single URL", command=process_single_url)
    single_url_button.grid(row=5, column=0, columnspan=2, pady=5)

    tk.Label(frame, text="Or Enter CSV file:").grid(row=6, column=0, columnspan=2)

    csv_button = tk.Button(frame, text="Process CSV File", command=process_csv_file)
    csv_button.grid(row=7, column=1, columnspan=2, pady=5)

    tk.Label(frame,text="CSV file must have columns titled: url, start_timestamp, end_timestamp").grid(row=8, column=0, columnspan=2)
    # Add a ScrolledText widget to display log messages
    log_widget = scrolledtext.ScrolledText(frame, width=80, height=20, state='disabled')
    log_widget.grid(row=9, column=0, columnspan=2, pady=5)

    # Redirect stdout and stderr to the log widget
    sys.stdout = RedirectText(log_widget)
    sys.stderr = RedirectText(log_widget)

    root.mainloop()
