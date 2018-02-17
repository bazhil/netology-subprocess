import subprocess
import os

folder = os.listdir('Source')
if not os.path.exists("Result"):
    os.mkdir("Result")
for file in folder:
    if file.endswith(".jpg"):
        subprocess.run("convert Source\\{0} -resize 200 Result\\new_{0}".format(file))



