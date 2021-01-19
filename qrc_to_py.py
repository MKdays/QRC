#경로 설정 : 순서 변경 금지
import sys, os
app_path = os.path.join(os.path.dirname(sys.argv[0])) #현재 위치 확인
os.chdir(app_path) #경로 변경

#라이브러리
from pathlib import Path
from time import sleep
import shutil
from glob import glob

# 옵션 ------------------------------------------------------
path_search = app_path
path_out = [
    str(Path(app_path).parent) +"/ExcelKits/qt_resource",
    str(Path(app_path).parent) + "/PyKooler/qt_resource",
    str(Path(app_path).parent) + "/RuleMaker/qt_resource"
]
# -----------------------------------------------------------

work_list = glob("*.qrc") + glob("*.ui")

def ui_convert(raw):
    for i in path_out:
        os.system(f"pyside2-uic \"{raw}\" -o \"{i}/{Path(raw).stem}.py\"")
        print(f"\"{i}/{Path(raw).stem}.py\"")

def qrc_convert(raw):
    for i in path_out:
        os.system(f"pyside2-rcc \"{raw}\" -o \"{i}/{Path(raw).stem}.py\"")
        print(f"\"{i}/{Path(raw).stem}.py\"")

for raw in work_list:
    if raw.endswith(".ui"):ui_convert(raw)
    elif raw.endswith(".qrc"):qrc_convert(raw)

try:shutil.rmtree("__pycache__") #폴더삭제
except:pass

sleep(0.5)