import time
from InfoTrace import Trace
from threading import Thread
from Network import Network


class Rotation:
    n = Network()
    trace = Trace()

    delay = 10

    def __init__(self):
        self.isPatrol = True
        Thread(target=self.patrol).start()

    def patrol(self):
        while True:
            if not self.isPatrol:
                break

            self.trace.print_patrol("Turn left")
            self.__turn_left()
            time.sleep(self.delay)
            self.__stop()

            if not self.isPatrol:
                break

            self.trace.print_patrol("Turn right")
            self.__turn_right()
            time.sleep(self.delay)
            self.__stop()

    def __turn_left(self):
        self.n.send_message(3)

    def __turn_right(self):
        self.n.send_message(4)

    def __stop(self):
        self.n.send_message(0)

    def stop_patrol(self):
        self.isPatrol = False

    def start_patrol(self):
        self.isPatrol = True
