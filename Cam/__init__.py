import cv2
import Resolution
from Detection import Detection
from Recorder import Recorder
from RTSPCam import Camera

cap = Camera("rtsp://192.168.1.99")

resolution = Resolution.get_dims()
recorder = Recorder(resolution, video_length=10)
detection = Detection(0.6)

while True:
    frame = cap.getFrame()
    if frame is not None:
        resized_frame = Resolution.change_res(frame, resolution)
        cv2.imshow('frame', resized_frame)
        detection.person_detect(resized_frame)
        recorder.write_frame(resized_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

recorder.end_recording()
cv2.destroyAllWindows()
