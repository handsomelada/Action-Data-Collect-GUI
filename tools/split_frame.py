import os
import cv2
import global_flag

def start_collect_view_1(path, scene, person, action):
    total_path = '{root}/{s}C001{p}{a}'.format(root=path, s=scene, p=person, a=action)
    print(total_path)
    if not os.path.exists(total_path):
        os.mkdir(total_path)
    if os.path.exists(total_path):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        cnt = 0
        fr = 30
        while cap.isOpened() and global_flag.get_value('collect_flag'):
            ret, frame = cap.read()
            if cnt % fr == 0:
                img_name = '{s}C001{p}{a}{f}'.format(root=path, s=scene, p=person, a=action, f=f'F{cnt:03d}.jpg')
                cv2.imwrite(os.path.join(total_path, img_name), frame)
            cnt += 1
        cap.release()

def start_collect_view_2(path, scene, person, action):
    total_path = '{root}/{s}C002{p}{a}'.format(root=path, s=scene, p=person, a=action)
    print(total_path)
    if not os.path.exists(total_path):
        os.mkdir(total_path)
    if os.path.exists(total_path):
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        cnt = 0
        fr = 30
        while cap.isOpened() and global_flag.get_value('collect_flag'):
            ret, frame = cap.read()
            if cnt % fr == 0:
                img_name = '{s}C002{p}{a}{f}'.format(root=path, s=scene, p=person, a=action, f=f'F{cnt:03d}.jpg')
                cv2.imwrite(os.path.join(total_path, img_name), frame)
            cnt += 1
        cap.release()

def start_collect_view_3(path, scene, person, action):
    total_path = '{root}/{s}C003{p}{a}'.format(root=path, s=scene, p=person, a=action)
    print(total_path)
    if not os.path.exists(total_path):
        os.mkdir(total_path)
    if os.path.exists(total_path):
        cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
        cnt = 0
        fr = 30
        while cap.isOpened() and global_flag.get_value('collect_flag'):
            ret, frame = cap.read()
            if cnt % fr == 0:
                img_name = '{s}C003{p}{a}{f}'.format(root=path, s=scene, p=person, a=action, f=f'F{cnt:03d}.jpg')
                cv2.imwrite(os.path.join(total_path, img_name), frame)
            cnt += 1
        cap.release()
