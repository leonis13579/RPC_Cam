import time
import cv2
import os
from datetime import datetime
from threading import Thread


class Recorder(object):
    def __init__(self, resolution, video_length):
        self.recording = True
        Thread(target=self.subtract_video, args=(resolution, video_length)).start()

    def write_frame(self, frame):
        self.out.write(frame)

    def end_recording(self):
        self.recording = False

    def subtract_video(self, resolution, video_length):
        while self.recording:
            if not os.path.isdir("Videos/" + datetime.now().strftime("%d-%m-%Y")):
                os.makedirs("Videos/" + datetime.now().strftime("%d-%m-%Y"))

            dt_string = datetime.now().strftime("%d-%m-%Y/%H-%M-%S")
            name = "Videos/" + dt_string + '.mp4'
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.out = cv2.VideoWriter(name, fourcc, 10.0, resolution)

            i = 0
            while i < video_length and self.recording:
                i += 1
                time.sleep(1)

            self.out.release()
