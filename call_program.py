import subprocess

process=subprocess.run("convert Source\\47c8937f8ae4966e356219a9015b1c67.jpg -resize 200 Result\\image1.jpg")
process=subprocess.run("convert Source\\26694fe81544dcf4c14217d6ace7e4f6.jpg -resize 200 Result\\image2.jpg")
process=subprocess.run("convert Source\\face-04.jpg -resize 200 Result\\image3.jpg")
process=subprocess.run("convert Source\\men-beard-styles-for-round-face.jpg -resize 200 Result\\image4.jpg")
process=subprocess.run("convert Source\\trump_mug.jpg -resize 200 Result\\image5.jpg")


