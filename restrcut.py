import glob
import pathlib
import shutil
from typing import Union

images = glob.glob("Plantes/*/image*")

def get_image_label(path: Union[str, pathlib.Path]) -> str:
  """ """
  path = pathlib.Path(path)
  label = path.parts[1].split('_')[2]
  return label

labels = list(map(get_image_label, images))


for p in labels:
    pp = pathlib.Path("Plantes/train")

for i in images:
    source = i
    target = pathlib.Path(
        f"Plantes/train/{get_image_label(source)}/")
    target.mkdir(
            parents=True, exist_ok=True)
    shutil.copy(source, target)
    print("Copied", source, "==>", target)

