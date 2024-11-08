import sys
import subprocess
import os
import re
from pytube import YouTube
import youtube_dl
import yt_dlp as youtube_dl_2

# ファイル名に使えない文字を削除する関数
def sanitize_filename(filename):
    return re.sub(r'[\\/*?:"<>|]', "", filename)

# MP4をMP3に変換する関数
def convert_mp4_to_mp3(mp4_file_path, mp3_file_name):
    mp3_file_path = mp3_file_name + '.mp3'
    command = ['ffmpeg', '-i', mp4_file_path, '-vn', '-ab', '128k', '-ar', '44100', '-y', mp3_file_path]
    subprocess.run(command)
    print(f"Converted {mp4_file_path} to {mp3_file_path}")
    # 中間ファイル（MP4）を削除
    os.remove(mp4_file_path)
    print(f"Deleted intermediate file {mp4_file_path}")

# YouTube動画をpytubeでダウンロードする関数
def download_with_pytube(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        title = sanitize_filename(yt.title)
        stream.download(filename='movie.mp4')
        print("Downloaded with pytube")
        return 'movie.mp4', title
    except Exception as e:
        print(f"pytube failed: {e}")
        return None, None

# YouTube動画をyoutube_dlでダウンロードする関数
def download_with_youtube_dl(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'movie.mp4',
        'noplaylist': True,
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print("Downloaded with youtube_dl")
            return 'movie.mp4', sanitize_filename(info_dict['title'])
    except Exception as e:
        print(f"youtube_dl failed: {e}")
        return None, None

# YouTube動画をyt_dlpでダウンロードする関数
def download_with_yt_dlp(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'movie.mp4',
        'noplaylist': True,
    }
    try:
        with youtube_dl_2.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print("Downloaded with yt_dlp")
            return 'movie.mp4', sanitize_filename(info_dict['title'])
    except Exception as e:
        print(f"yt_dlp failed: {e}")
        return None, None

# メイン処理
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python youtube_to_mp3.py <youtube url>")
        sys.exit(1)

    url = sys.argv[1]
    
    # ダウンロードを試行
    mp4_file_path, title = download_with_pytube(url)
    if not mp4_file_path:
        mp4_file_path, title = download_with_youtube_dl(url)
    if not mp4_file_path:
        mp4_file_path, title = download_with_yt_dlp(url)
    
    if mp4_file_path and title:
        # MP4からMP3へ変換
        convert_mp4_to_mp3(mp4_file_path, title)
    else:
        print("Failed to download the video.")
