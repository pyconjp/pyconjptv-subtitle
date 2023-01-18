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
--- download youtube audio file ---
[youtube] Extracting URL: https://www.youtube.com/watch?v=6gqyEktNU0Q
[youtube] 6gqyEktNU0Q: Downloading webpage
[youtube] 6gqyEktNU0Q: Downloading android player API JSON
[info] 6gqyEktNU0Q: Downloading 1 format(s): 251
[download] pyconjptv24.webm has already been downloaded
[download] 100% of   44.17MiB
--- transcribe audio file ---
/Users/takanori/Private/pyconjp/pyconjptv-subtitle/env/lib/python3.10/site-packages/whisper/transcribe.py:79: UserWarning: FP16 is not supported on CPU; using FP32 instead
  warnings.warn("FP16 is not supported on CPU; using FP32 instead")
[00:00.000 --> 00:08.000] 字幕があればコメントお願い致しました!
[00:30.000 --> 00:34.260] ますか 誰に対していつもと違うところから配信して
[00:34.260 --> 00:38.500] ます見てわかると思うんですけどはい パイコン gptv の時間です
...
(env) $ ls *.srt
pyconjptv24.srt
```

## 参考

* [yt-dlp/yt-dlp: A youtube-dl fork with additional features and fixes](https://github.com/yt-dlp/yt-dlp)
* [openai/whisper: Robust Speech Recognition via Large-Scale Weak Supervision](https://github.com/openai/whisper)
