"""Buat ikon launcher Android dari scripts/icon-source.png."""
from pathlib import Path
from PIL import Image, ImageDraw

SRC = Image.open(Path(__file__).parent / "icon-source.png").convert("RGBA")
RES = Path("android/app/src/main/res")

LEGACY = {"mdpi": 48, "hdpi": 72, "xhdpi": 96, "xxhdpi": 144, "xxxhdpi": 192}
FOREGROUND = {"mdpi": 108, "hdpi": 162, "xhdpi": 216, "xxhdpi": 324, "xxxhdpi": 432}

for dens, size in LEGACY.items():
    folder = RES / f"mipmap-{dens}"
    folder.mkdir(parents=True, exist_ok=True)
    icon = SRC.resize((size, size), Image.LANCZOS)
    icon.save(folder / "ic_launcher.png")
    mask = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)
    round_icon = icon.copy()
    round_icon.putalpha(mask)
    round_icon.save(folder / "ic_launcher_round.png")

for dens, size in FOREGROUND.items():
    folder = RES / f"mipmap-{dens}"
    folder.mkdir(parents=True, exist_ok=True)
    SRC.resize((size, size), Image.LANCZOS).save(folder / "ic_launcher_foreground.png")

print("Ikon selesai dibuat")
