from __future__ import unicode_literals
from youtube_dl import YoutubeDL

import argparse
import os

def parse_music_from_url(url, output_filename:str = '', output_folder:str = ''):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # By deffault it will use the title of the video
    if output_filename != '':
        ydl_opts['outtmpl'] = output_filename

    create_folder_if_not_exists(output_folder)
    os.chdir(output_folder)

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def initialize_cli_parser():
    # Initialize the command line parser and arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-U",
        "--url",
        type=str,
        required=True,
        help='URL of the youtube video'
    )
    parser.add_argument(
        "-N",
        "--output-filename",
        default='',
        type=str,
        required=False,
        help='Name of the output file; the default value is the video\'s title. For example: test.mp3'
    )
    parser.add_argument(
        "-P",
        "--output-folder",
        default='',
        type=str,
        required=False,
        help='The location where the file is saved; the default destination is the folder "downloads" in the executed folder'
    )
    return parser


cli_parser = initialize_cli_parser()
# Read argument from the command line
input_args = cli_parser.parse_args()

def build_default_downloads_folder():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    download_folder = 'downloads'
    return os.path.join(current_directory, download_folder)

def create_folder_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

download_path = build_default_downloads_folder()
if input_args.output_folder:
    download_path = input_args.output_folder

parse_music_from_url(
    url=input_args.url,
    output_filename=input_args.output_filename,
    output_folder=download_path
)
