#!/usr/bin/env python3
"""Convert every HEIC image located alongside this script into a JPEG file."""

from __future__ import annotations

import sys
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


def main() -> None:
    convert_images(Path(__file__).resolve().parent)


if __name__ == "__main__":
    main()
