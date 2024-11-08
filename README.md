## Overview
youtube-mp3-downloader is a Python script that downloads YouTube videos and converts them to MP3 format. It uses multiple download methods (pytube, youtube-dl, and yt-dlp) to ensure reliable downloading, and automatically converts the downloaded video to MP3 using ffmpeg.

## Installation
1. Clone the repository
```bash
git clone https://github.com/daishir0/youtube-mp3-downloader.git
```

2. Change to the project directory
```bash
cd youtube-mp3-downloader
```

3. Install the required dependencies
```bash
pip install -r requirements.txt
```

4. Install ffmpeg
- For Ubuntu/Debian:
```bash
sudo apt-get install ffmpeg
```
- For macOS (using Homebrew):
```bash
brew install ffmpeg
```
- For Windows:
  - Download ffmpeg from https://ffmpeg.org/download.html
  - Add ffmpeg to your system PATH

## Usage
Run the script with a YouTube URL as an argument:
```bash
python youtube_to_mp3.py <youtube url>
```

Example:
```bash
python youtube_to_mp3.py https://www.youtube.com/watch?v=example
```

## Notes
- The script requires a stable internet connection
- Downloaded MP3 files will be saved in the same directory as the script
- The script automatically removes the intermediate MP4 file after conversion
- If one download method fails, the script will automatically try the next method

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 概要
youtube-mp3-downloaderは、YouTubeの動画をダウンロードしてMP3形式に変換するPythonスクリプトです。複数のダウンロード方式（pytube、youtube-dl、yt-dlp）を使用して信頼性の高いダウンロードを実現し、ダウンロードした動画を自動的にffmpegを使用してMP3に変換します。

## インストール方法
1. レポジトリをクローンする
```bash
git clone https://github.com/daishir0/youtube-mp3-downloader.git
```

2. プロジェクトディレクトリに移動
```bash
cd youtube-mp3-downloader
```

3. 必要な依存パッケージをインストール
```bash
pip install -r requirements.txt
```

4. ffmpegのインストール
- Ubuntu/Debian の場合:
```bash
sudo apt-get install ffmpeg
```
- macOS の場合（Homebrewを使用）:
```bash
brew install ffmpeg
```
- Windows の場合:
  - ffmpegを https://ffmpeg.org/download.html からダウンロード
  - ffmpegをシステムPATHに追加

## 使い方
YouTubeのURLを引数として指定してスクリプトを実行します：
```bash
python youtube_to_mp3.py <youtube url>
```

例：
```bash
python youtube_to_mp3.py https://www.youtube.com/watch?v=example
```

## 注意点
- 安定したインターネット接続が必要です
- ダウンロードしたMP3ファイルは、スクリプトと同じディレクトリに保存されます
- 変換後、中間ファイル（MP4）は自動的に削除されます
- 一つのダウンロード方式が失敗した場合、自動的に次の方式を試行します

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
