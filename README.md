# Youtube audio downloader

## Setup

YAD is a script that allows to extract and download the music from your favourite youtube videos in mp3 format.

### Upgrade pip and install youtube-dl

```bash
$ python -m pip install --upgrade pip
$ pip install --upgrade youtube-dl
```

### Install ffmpeg (windows)

Go to [ffmpeg](http://ffmpeg.zeranoe.com/builds) downloads page and install the version that suits you the most.

Extract the content of the zip file and add the binaries to the location of the exes inside.

## Run the script

```bash
$ python yad.py --url https://www.youtube.com/watch?v=OmH_wUt2o6g --output-filename test.mp3
```

The script may take several seconds/minutes to finish depending on the length of the video, the quality, etc.

### Parameters

* `-U` or `--url`: **[REQUIRED]**, specifies the youtube link
* `-N` or `--output-name`: **[OPTIONAL]**, specifies the name of the output file, the **default value** is the title of the video
* `-P` or `--output-path`: **[OPTIONAL]**, specifies where will the output file be stored, the **default value** is the folder `downloads` located in the script's execution folder
