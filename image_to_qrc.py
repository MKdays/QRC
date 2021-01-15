import glob
from pathlib import Path
from time import sleep

image_list = glob.glob("image/*.png")

text = "<RCC>"
text = text + "\n" + "  <qresource prefix=\"__resource__\">"
for i in image_list:
    text = text + "\n" + f"    <file>image/{Path(i).name}</file>"
text = text + "\n" + "  </qresource>"
text = text + "\n" + "</RCC>"

file_path = "resource.qrc"
with open(file_path, 'w', encoding="utf-8") as file:
    file.write(text)

print("OK")
sleep(1)