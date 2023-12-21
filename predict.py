import pygame
import os
import sys
import random
import json
import torch
# from model2 import SimpleConvNet
from resnet import ResNet 
from PIL import Image

# file_list = [f for f in os.listdir('./data/raw_images') if f.endswith('.jpg')]
file_list = [f['image'] for f in json.load(open('data/labeled_images.json'))]
file_list = file_list[int(len(file_list) * 0.8):]
print(file_list)

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Image Display Example")

# Load the image
global pointer
pointer = 0
image_path = os.path.join('./data/raw_images', file_list[pointer])
image = pygame.image.load(image_path)

used_images = set()

def get_new_image(pointer):
    while pointer in used_images:
        pointer = random.randint(0, len(file_list))    

    print(pointer)
    used_images.add(pointer)

    image_path = os.path.join('./data/raw_images', file_list[pointer])
    image = pygame.image.load(image_path)

    return image, image_path, pointer


get_new_image(pointer)

points = []

m = ResNet()
m.load_state_dict(torch.load('best_model.pt'))
m.eval()

def predict(image_path):
    img = Image.open(image_path)
    img = img.resize((round(16/9 * 128), 128))
    img_tensor = torch.tensor(list(img.getdata()), dtype=torch.float32).view(3, 128, round(16/9 * 128))
    x1, y1, x2, y2 = m(img_tensor.unsqueeze(0))[0].tolist()
    return [
        {
            'x': x1,
            'y': y1
        },
        {
            'x': x2,
            'y': y2
        }
    ]


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #print x and y coordinates to console
            print(event.pos)
            points.append({'x': event.pos[0], 'y': event.pos[1]})
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            points = []
            image, image_path, pointer = get_new_image(pointer)
            points = predict(image_path)
            print(points)


    # Blit the image onto the screen
    screen.blit(image, (0, 0))
    
    for point in points:
        pygame.draw.circle(screen, (255, 0, 0), (point['x'], point['y']), 5)

    # Update the display
    pygame.display.flip()

# Cleanup
pygame.quit()
