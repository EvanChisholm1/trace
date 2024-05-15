import cv2
import numpy as np

image_path = './frame_0561.jpg'
img = cv2.imread(image_path)

overlay = img.copy()

grid_size = 150 # Grid cell size
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
color = (255, 255, 255)  # White color in BGR format
thickness = 3
circle_color = (0, 0, 255)
radius = grid_size//5
text_color = (255, 255, 255)

height, width, _ = img.shape

count = 0
for i in range(0, width, grid_size):
    for j in range(0, height, grid_size):
        # Draw rectangle (grid cell)
        cv2.rectangle(overlay, (i, j), (i + grid_size, j + grid_size), (0, 0, 0), 2)

        # Calculate the row and column number
        center_x = i + grid_size // 2
        center_y = j + grid_size // 2

        # Draw circle (overlay the circle in the center of the grid cell)
        cv2.circle(overlay, (center_x, center_y), radius, circle_color, -1)
        row = j // grid_size
        col = i // grid_size

        # Define the position to put the number text (slightly inside the grid)
        position = (i + 5, j + 20)

        # Put row and column numbers as text
        # cv2.putText(overlay, f'{row},{col}', position, font, font_scale, color, thickness)
        # text = f'{row},{col}'
        text = f'{count}'
        count += 1
        (text_width, text_height), baseline = cv2.getTextSize(text, font, font_scale, thickness)
        text_x = center_x - text_width // 2
        text_y = center_y + text_height // 2

        # Put row and column numbers as text inside the circle
        cv2.putText(overlay, text, (text_x, text_y), font, font_scale, text_color, thickness)


combined = cv2.addWeighted(overlay, 0.5, img, 0.2, 1)
cv2.imwrite('image_with_grid_overlay_2.jpg', combined)
