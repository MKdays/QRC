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
path_out_1 = str(Path(app_path).parent) + "/ExcelTool/qt_resource"
path_out_2 = str(Path(app_path).parent) + "/PyCooler/qt_resource"
path_out_3 = str(Path(app_path).parent) + "/RuleMaker/qt_resource"

# print(path_out)
# as_is = ""
# to_be = ""
# -----------------------------------------------------------

# work_list =[]
# for i in os.listdir(path_search):
#     if i.endswith(".ui") or i.endswith(".qrc"):
#         work_list.append(i)

work_list = glob("*.qrc")

# def ui_convert(i):
#   os.system("pyside2-uic " + i + " -o " + path_out + "/" + Path(i).stem + ".py")

def qrc_convert(i):
  print(path_out_1)
  os.system("pyside2-rcc " + i + " -o " + path_out_1 + "/" + Path(i).stem + ".py")
  print(path_out_2)
  os.system("pyside2-rcc " + i + " -o " + path_out_2 + "/" + Path(i).stem + ".py")
  print(path_out_3)
  os.system("pyside2-rcc " + i + " -o " + path_out_3 + "/" + Path(i).stem + ".py")

# def replace_text(i):
#   with open(path_out + "/" + Path(i).stem + ".py", 'r', encoding="utf-8") as file :
#     filedata = file.read()
#   filedata = filedata.replace(as_is, to_be)
#   with open(path_out + "/" + Path(i).stem + ".py", 'w', encoding="utf-8") as file:
#     file.write(filedata)

for i in work_list:
  # print(i + " 완료")
  # if i.endswith(".ui"):ui_convert(i)
  # elif i.endswith(".qrc"):qrc_convert(i)
  qrc_convert(i)
#   replace_text(i)

try:shutil.rmtree("__pycache__") #폴더삭제
except:pass

print("OK")
sleep(0.5)