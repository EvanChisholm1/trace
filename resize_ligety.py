from PIL import Image
import os

file_list = [f for f in os.listdir('./ligety') if f.endswith('.jpg')]

# for file in file_list:
#     img = Image.open(os.path.join('./ligety', file))
#     img = img.resize((1920, 1080))
#     img.save(os.path.join('./ligety', file))


for file in file_list:
    img = Image.open(os.path.join('./ligety', file))
    img.save(os.path.join('./data/raw_images', f"ligety_{file}"))