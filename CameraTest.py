import numpy as np
import cv2
import threading
import time
from copy import deepcopy

thread_lock = threading.Lock()
thread_exit = False


class myThread(threading.Thread):
    def __init__(self, camera_id, img_height, img_width):
        super(myThread, self).__init__()
        self.camera_id = camera_id
        self.img_height = img_height
        self.img_width = img_width
        self.frame = np.zeros((img_height, img_width, 3), dtype=np.uint8)

    def get_frame(self):
        return deepcopy(self.frame)

    def run(self):
        global thread_exit
        cap = cv2.VideoCapture(self.camera_id)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.img_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.img_height)
        while not thread_exit:
            ret, frame = cap.read()
            if ret:
                # frame = cv2.resize(frame, (self.img_width, self.img_height))
                thread_lock.acquire()
                self.frame = frame
                thread_lock.release()
            else:
                thread_exit = True
        cap.release()


def main():
    global thread_exit
    camera_id = 0
    img_width = 1920
    img_height = 1080
    thread = myThread(camera_id, img_height, img_width)
    thread.start()

    while not thread_exit:
        thread_lock.acquire()
        frame = thread.get_frame()
        thread_lock.release()

        cv2.imshow('Video', frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            thread_exit = True
        elif(key & 0xFF == ord('s')):
            cv2.imwrite(
                f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}.png", frame)
    thread.join()


if __name__ == "__main__":
    main()
