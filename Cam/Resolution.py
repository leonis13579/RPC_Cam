import cv2
import imutils

STD_DIMENSIONS =  {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}

def get_dims(res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    return width, height


def change_res(cap, width, height):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def change_res(frame, resolution):
    if frame.shape[0] != resolution[0] or frame.shape[1] != resolution[1]:
        return imutils.resize(frame, resolution[0], resolution[1])
    else:
        return frame
