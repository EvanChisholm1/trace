import cv2

def extract_frames(video_path, output_path):
    video_capture = cv2.VideoCapture(video_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if ret:
            out.write(frame)
        else:
            break
    
    video_capture.release()
    out.release()
    print('Extracted frames from video: {}'.format(video_path))

if __name__ == "__main__":
    video_path = "./ligety-test.mp4"
    output_path = "./ligety/frame_%04d.jpg"
    extract_frames(video_path, output_path)
    print("Done!")
