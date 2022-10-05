import cv2
import os
from datetime import datetime


def frames_to_video(root_path, save_path):
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    fps = 15
    video_width, video_height = 640, 480
    frames_path = os.listdir(root_path)
    for i, p in enumerate(frames_path):
        s = p + '.mp4'
        real_savepath = os.path.join(save_path, s)
        # print('realsavepath:',real_savepath)
        videoWriter = cv2.VideoWriter(real_savepath, fourcc, fps, (video_width, video_height))
        frames = os.listdir(os.path.join(root_path, p))
        # print('frames:', frames)
        for f, frame in enumerate(frames):
            # print(os.path.join(os.path.join(root_path, p), frame))
            fr = cv2.imread(os.path.join(os.path.join(root_path, p), frame))
            videoWriter.write(fr)
    videoWriter.release()


if __name__ == '__main__':
    frames_to_video('../test_d/frame/S001', "../test_d/video/S001")


