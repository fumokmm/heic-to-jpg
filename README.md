# heic-to-jpg

HEIC画像をJPG画像に問答無用で変換

## 必要なパッケージ

- [Pillow](https://python-pillow.org/)
- [pillow-heif](https://github.com/strukturag/libheif)

```bash
pip install pillow pillow-heif
```

## 使い方

以下のいずれかの方法で実行します。

- 現在のフォルダ内のHEICを変換する:

```bash
python convert_heic_to_jpg.py
```

- 対象フォルダを指定して変換する:

```bash
python convert_heic_to_jpg.py /path/to/dir
```

`.heic` / `.HEIC` の拡張子を持つファイルを、同名の `.jpg` に変換します。
