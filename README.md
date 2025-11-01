# heic-to-jpg

HEIC画像をJPG画像に問答無用で変換

## 必要なパッケージ

- [Pillow](https://python-pillow.org/)
- [pillow-heif](https://github.com/strukturag/libheif)

```bash
pip install pillow pillow-heif
```

## 使い方

HEIC画像と同じフォルダにこのスクリプトを配置し、以下のコマンドを実行してください。

```bash
python convert_heic_to_jpg.py
```

同じフォルダ内にある `.heic` 拡張子のファイルをすべて同名の `.jpg` ファイルに変換します。
