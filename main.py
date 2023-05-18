from PIL import Image, ImageFont, ImageDraw
import csv

large_font = ImageFont.truetype("Gilroy-ExtraBold.ttf", 40)
small_font = ImageFont.truetype("Gilroy-ExtraBold.ttf", 28)

# only the names
with open("data.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    for row in reader:
        img = Image.open("template.png")

        I1 = ImageDraw.Draw(img)

        I1.text((734, 440), row[0], fill=(0, 0, 0), font=large_font, anchor="mm")
        I1.text((910, 540), "Quiz Time", fill=(0, 0, 0), font=small_font)
        I1.text((360, 540), "for participating", fill=(0, 0, 0), font=small_font)

        img.save("certificate/quiz_time/" + row[0] + ".png")

        img.close()
