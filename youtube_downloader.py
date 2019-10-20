from __future__ import unicode_literals
from youtube_dl import YoutubeDL

import argparse
import os

def parse_music_from_url(url, name:str = ''):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # By deffault it will use the title of the video
    if name != '':
        ydl_opts['outtmpl'] = name

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

# Initialize the command line parser
parser = argparse.ArgumentParser()
parser.add_argument(
    "-U",
    "--url"
)
parser.add_argument(
    "-N",
    "--output-name"
)
parser.add_argument(
    "-P",
    "--output-path"
)

# Read argument from the command line
args = parser.parse_args()

# Check for --url o -U
if args.url:
    print("URL: {}".format(args.url))


current_directory = os.path.dirname(os.path.abspath(__file__))
download_folder = 'dowloads'
download_path = os.path.join(current_directory, download_folder)
if args.output_folder:
    download_path = args.output_folder


os.chdir(download_path)
url = ['https://www.youtube.com/watch?v=OmH_wUt2o6g']
#urls = ['https://www.youtube.com/watch?v=AjPKCLxG9wY']
#urls = ['https://www.youtube.com/watch?v=BaW_jenozKc']
parse_music_from_url(url, 'test.mp3')