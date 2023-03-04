import os
from pytube import YouTube
from pytube.cli import on_progress
import shutil
import threads

def download_song(video_url, nid):
  global threads
  shutil.rmtree("./tmp")
  os.mkdir("./tmp")
  threads.threads[nid] = 1

  # create a YouTube object
  yt = YouTube(video_url, on_progress_callback=on_progress)
  threads.threads[nid] = 2

  # extract only audio
  video = yt.streams.filter(only_audio=True).first()
  threads.threads[nid] = 3

  # destination directory for the downloaded file
  destination = './tmp'
  threads.threads[nid] = 4

  # download the file
  out_file = video.download(output_path=destination)
  threads.threads[nid] = 5

  # save the file with an MP3 extension
  os.rename(out_file, "./tmp/" + yt.title + ".mp3")
  threads.threads[nid] = 6

  # result of success

  return yt.title
