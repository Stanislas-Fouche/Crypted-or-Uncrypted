from random import randint
import numpy as np
from PIL import Image
import numpy as np
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import io
import csv


for x in range(26):
    filename = str(x)+ ".csv"
    rows, columns = 2000, 2000
    random_data = np.random.randint(0, 1000, size=(rows, columns))

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(random_data)

    print(f"CSV file created: {filename}")



for y in range(39):
    filename = str(y)
    width, height = 1024, 1024 

    Image.fromarray(np.random.randint(0, 256, (height, width, 3), dtype=np.uint8), 'RGB').save(filename + '.png')
    print( filename + ".png Image saved")

    Image.fromarray(np.random.randint(0, 256, (height, width, 3), dtype=np.uint8), 'RGB').save( filename + '.jpg')
    print(filename + ".jpg Image saved")


for z in range(39):
    filename = str(z) + ".pdf"
    random_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    image = Image.fromarray(random_data, 'RGB')

    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    c = canvas.Canvas(filename, pagesize=letter)



    page_width, page_height = letter
    x = (page_width - width) / 2
    y = (page_height - height) / 2

    image_reader = ImageReader(img_byte_arr)

    c.drawImage(image_reader, x, y, width=width, height=height)
    c.save()

    print(f"PDF saved as : {filename}")


for zz in range(49):
    if (zz == 0):
        continue
    filename = str(zz) + ".txt"




for x in range(48):
    filename = str(x)+ ".txt"
    rows, columns = 2000, 2000
    random_data = np.random.randint(0, 1000, size=(rows, columns))

    with open(filename, "w") as file:
        file.writelines(f"{randint(1, 100)}\n" for _ in range(100))

    with open(filename, "r") as fin,\
        open("filtered_numbers.txt", "w") as fout:
        numbers = [n for n in map(int, fin) if 20 < n < 80]
        print(f"Found {len(numbers)} numbers between 20 and 80.")
        fout.write(",".join(map(str, numbers)))

    print(f"TXT file created: {filename}")


