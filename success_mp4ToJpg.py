import cv2
import os
import numpy as np
from PIL import Image

# 한글이름까지 가능하도록 성공
# cv2에서는 한글을 지원하지않아 pil을 사용하여 한번 더 처리하였음
def save_first_frame(video_path, output_path):
    """동영상의 첫 프레임 jpg로 저장"""
    cap = cv2.VideoCapture(video_path)

    filename = os.path.splitext(os.path.basename(video_path))[0] + ".jpg"
    output_file = os.path.join(output_path, filename)


    ret, frame = cap.read()
    if ret:
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image)
        pil_image.save(output_file)

        print(output_file)
        cap.release()
    else:
        print(f"cant not read mov  {video_path}")
        return


def process_videos_in_folder(input_folder, output_folder):
    """폴더 내 모든 동영상 처리"""
    # 출력 폴더 생성
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        video_path = os.path.join(input_folder, filename)

        # 파일이 동영상인지 확인
        if os.path.isfile(video_path) and filename.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
            print(f"Processing video file: {video_path}")
            save_first_frame(video_path, output_folder)
        else:
            print(f"Skipping non-video file: {video_path}")


def process_multiple_folders(base_folder, output_base_folder):
    """여러 폴더 처리"""
    for folder in os.listdir(base_folder):
        input_folder = os.path.join(base_folder, folder)

        # 입력 폴더가 디렉터리인지 확인
        if os.path.isdir(input_folder):
            output_folder = os.path.join(output_base_folder, folder)
            print(f"Processing folder: {input_folder}")
            process_videos_in_folder(input_folder, output_folder)
        else:
            print(f"Skipping non-folder: {input_folder}")


# 사용 예시
base_folder = r"D:\videos"  # 동영상들이 들어 있는 최상위 폴더 경로
output_base_folder = r"C:\Users\subPc\Desktop\241120test"  # 저장할 이미지 폴더
process_multiple_folders(base_folder, output_base_folder)