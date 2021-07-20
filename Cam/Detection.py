import cv2
import imutils
import numpy as np
import InfoTrace
from threading import Thread
from datetime import datetime
import time
import os


class Detection:

    def __init__(self, confidence):
        self.CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
                        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                        "sofa", "train", "tvmonitor"]
        self.COLORS = np.random.uniform(0, 255, size=(len(self.CLASSES), 3))

        self.target_confidence = confidence
        self.flag = True

        InfoTrace.print_info("loading model...")
        self.net = cv2.dnn.readNetFromCaffe("Caffe/MobileNetSSD_deploy.prototxt.txt",
                                            "Caffe/MobileNetSSD_deploy.caffemodel")

    def person_detect(self, frame):
        thread = Thread(target=self.person_detect_logic, args=(frame,))
        thread.start()
        thread.join()

    def person_detect_logic(self, frame):
        frame = imutils.resize(frame, width=400)

        # grab the frame dimensions and convert it to a blob
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                     0.007843, (300, 300), 127.5)

        # pass the blob through the network and obtain the detections and
        # predictions
        self.net.setInput(blob)
        detections = self.net.forward()

        # loop over the detections
        for i in np.arange(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with
            # the prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by ensuring the `confidence` is
            # greater than the minimum confidence
            if confidence > self.target_confidence:
                # extract the index of the class label from the
                # `detections`, then compute the (x, y)-coordinates of
                # the bounding box for the object
                idx = int(detections[0, 0, i, 1])
                if self.CLASSES[idx] == "person":
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # draw the prediction on the frame
                    label = "{}: {:.2f}%".format(self.CLASSES[idx],
                                                 confidence * 100)
                    cv2.rectangle(frame, (startX, startY), (endX, endY),
                                  self.COLORS[idx], 2)
                    y = startY - 15 if startY - 15 > 15 else startY + 15
                    cv2.putText(frame, label, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.COLORS[idx], 2)

                    self.detection_commit(frame)

    def return_flag(self):
        time.sleep(5)
        self.flag = True
        InfoTrace.print_info("Detection ready")

    def detection_commit(self, frame):
        if self.flag:
            self.flag = False
            message = datetime.now().strftime("%d.%m.%Y %H:%M:%S") + "\t[Detection]\tPerson detected"
            InfoTrace.print_detection("Person detected")
            file_input = open("Detections/Log.txt", "a")
            file_input.writelines(message + "\n")
            file_input.close()

            if not os.path.isdir("Detections"):
                os.makedirs("Detections")

            cv2.imwrite("Detections/" + datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".jpg", frame)
            Thread(target=self.return_flag).start()
