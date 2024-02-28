import cv2
import pygame
from PIL import Image
import torch
from resnet import ResNet

m = ResNet()
m.load_state_dict(torch.load('best_model.pt'))
m.eval()

video_path = './ski-video.mp4'


points = []
pygame_frames = []

cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(frame)

    pygame_image = pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode)
    pygame_frames.append(pygame_image)

    pil_image = pil_image.resize((round(16/9 * 128), 128))
    img_tensor = torch.tensor(list(pil_image.getdata()), dtype=torch.float32).view(3, 128, round(16/9 * 128))

    x1, y1, x2, y2 = m(img_tensor.unsqueeze(0))[0].tolist()
    points.append({
            'x': x1,
            'y': y1,
            'side': 'l'
        })
    points.append({
            'x': x2,
            'y': y2,
            'side': 'r'
        })
    
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Image Display Example")

i = 0
FPS = 24
clock = pygame.time.Clock()

while True:
    i = i % (len(pygame_frames))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    current_points = points[2*i:2*i+2]
    frame = pygame_frames[i]
    screen.blit(frame, (0, 0))
    print(current_points)
    for point in current_points:
        pygame.draw.circle(screen, (255, 0, 0) if point['side'] == 'l' else (0, 0, 255), (point['x'], point['y']), 10)

    pygame.display.flip()
    clock.tick(FPS)
    i +=1