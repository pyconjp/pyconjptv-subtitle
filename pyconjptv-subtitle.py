"""
PyCon JP TVのエピソード番号を指定すると、音声をダウンロードして
whisperでsrtファイルを生成するスクリプト

usage: python -u pyconjptv-subtitle.py 24
"""

import re
import sys
from urllib.error import HTTPError
from urllib.request import urlopen

import yt_dlp
from whisper import load_model
from whisper.utils import get_writer


AUDIO_DIR = "audio"
SUBTITLE_DIR = "subtitle"


def download_webm(url: str, webm: str) -> int:
    """yt_dlpでYouTubeの音声をwebm形式でダウンロード"""
    print("--- download youtube audio file ---")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": {"default": webm},
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)

    return error_code


def generate_srt(audio_file: str) -> None:
    """whisperで音声ファイルから字幕生成"""
    print("--- transcribe audio file ---")
    model = load_model("large-v2")
    result = model.transcribe(audio_file, verbose=True, language="japanese")

    # 結果をsrtファイルに出力
    writer = get_writer("srt", SUBTITLE_DIR)
    options = {"max_line_width": None, "max_line_count": None, "highlight_words": None}
    writer(result, audio_file, options)


def main(num: str) -> None:
    # PyCon JP TVのWebページからyoutubeのURLを取得
    url = f"https://tv.pycon.jp/episode/{num}.html"
    try:
        with urlopen(url) as f:
            html = f.read().decode("utf-8")
    except HTTPError:
        print("指定されたPyCon JP TVのページが存在しません")
        return

    if m := re.search(r'src="https://www.youtube.com/embed/([^"]+)"', html):
        youtube_url = f"https://www.youtube.com/watch?v={m[1]}"
    else:
        print("Youtube linkが見つかりませんでした")
        return

    basename = f"pyconjptv{num}"
    webm = f"{AUDIO_DIR}/{basename}.webm"
    error_code = download_webm(youtube_url, webm)

    # whisperで字幕をsrtファイルに生成
    generate_srt(webm)


if __name__ == "__main__":
    # 最初の引数を渡す
    if len(sys.argv) >= 2:
        main(sys.argv[1])
    else:
        pass
