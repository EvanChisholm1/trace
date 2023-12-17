import pygame
import os
import sys
import random
import json

file_list = [f for f in os.listdir('./data/raw_images') if f.endswith('.jpg')]
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

labeled_images = []
if os.path.exists('data/labeled_images.json'):
    labeled_images = json.load(open('data/labeled_images.json', 'r'))
    for labeled_image in labeled_images:
        used_images.add(file_list.index(labeled_image['image']))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            json.dump(labeled_images, open('data/labeled_images.json', 'w'))
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #print x and y coordinates to console
            print(event.pos)
            points.append({'x': event.pos[0], 'y': event.pos[1]})
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print(pointer, file_list[pointer])
            if len(points) == 2: labeled_images.append({'image': file_list[pointer], 'points': points})
            points = []
            image, image_path, pointer = get_new_image(pointer)
            print(labeled_images)
            print(len(labeled_images))


    # Blit the image onto the screen
    screen.blit(image, (0, 0))
    
    for point in points:
        pygame.draw.circle(screen, (255, 0, 0), (point['x'], point['y']), 5)

    # Update the display
    pygame.display.flip()

# Cleanup
pygame.quit()
