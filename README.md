# pyconjptv-subtitle

PyCon JP TVの字幕ファイルを生成するスクリプト

## 環境構築

```bash
$ brew install ffmpeg
$ python3.10 -m venv env
$ . env/bin/activate
(env) $ pip install -r requirements.txt
```

## スクリプトを実行

* 引数にエピソードの番号を指定する(`24` 等)
* `python -u` で実行する実行中処理結果が出力される

```bash
(env) $ python -u pyconjptv-subtitle 24
(env) $ ls *.srt
pyconjptv24.srt
```

## 参考

* [yt-dlp/yt-dlp: A youtube-dl fork with additional features and fixes](https://github.com/yt-dlp/yt-dlp)
* [openai/whisper: Robust Speech Recognition via Large-Scale Weak Supervision](https://github.com/openai/whisper)
