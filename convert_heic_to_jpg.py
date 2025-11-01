#!/usr/bin/env python3
"""Convert HEIC images in a target directory to JPEG files.

By default, operates on the current working directory. An optional directory
argument can be provided to convert files in a specific folder.
"""

from __future__ import annotations

import sys
import argparse
from pathlib import Path

from PIL import Image
from pillow_heif import register_heif_opener


def convert_images(directory: Path) -> None:
    """Convert all HEIC files in *directory* to JPEG with the same stem."""
    register_heif_opener()

    heic_files = sorted(
        path
        for path in directory.iterdir()
        if path.is_file() and path.suffix.lower() == ".heic"
    )

    if not heic_files:
        print("No HEIC files found.")
        return

    for heic_path in heic_files:
        jpg_path = heic_path.with_suffix(".jpg")

        try:
            with Image.open(heic_path) as image:
                rgb_image = image.convert("RGB")
                rgb_image.save(jpg_path, format="JPEG", quality=95)
        except Exception as exc:  # pylint: disable=broad-exception-caught
            print(f"Failed to convert {heic_path.name}: {exc}", file=sys.stderr)
        else:
            print(f"Converted {heic_path.name} -> {jpg_path.name}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert .heic/.HEIC files in a directory to .jpg"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=Path.cwd(),
        help="Target directory (default: current working directory)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_dir = Path(args.directory).resolve()
    convert_images(target_dir)


if __name__ == "__main__":
    main()
