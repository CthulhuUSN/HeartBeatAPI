from threading import Thread
import time

def background_task():
    while not background_task.cancelled:
        self.mqConn.heartbeat_tick()
        time.sleep(30)
background_task.cancelled = False

t = Thread(target=background_task)
t.start()

background_task.cancelled = True