"""Build a local Lively wallpaper import package; Python standard library only."""
from pathlib import Path
import zipfile

root = Path(__file__).parent
output = root / "dist" / "colorful-fluid-wallpaper.zip"
output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
    for name in ("index.html", "fluid.js", "LDR_LLL1_0.png", "LivelyInfo.json", "LICENSE"):
        archive.write(root / name, name)
print(output)
