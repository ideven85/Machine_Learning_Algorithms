import logging
import sys
import time

from Design_Patterns.priority_queue_pattern.queueManager import QueueManager


class Worker:
    """
    Task of Worker Thread is to constantly poll Queue Manager for highest priority messages
    """

    def __init__(self, queueManager: QueueManager):
        self.queueManager = queueManager

    def run(self):
        while True:
            task = self.queueManager.remove()
            if not task:
                logging.error("No messages left in Queue")
                print("No messages left in queue")
                time.sleep(2)
                sys.exit("No messages left in queue")
            else:
                print(task)
