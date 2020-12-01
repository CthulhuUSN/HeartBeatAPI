from Heartbeat import Requester
from threading import Thread
import time

def main():
    requester = Requester()
    while (True):
        requester.Post_Heartbeat()
        time.sleep(30)

if __name__ == "__main__":
    main()