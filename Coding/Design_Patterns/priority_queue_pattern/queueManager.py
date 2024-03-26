from Design_Patterns.priority_queue_pattern.priorityMessageQueue import (
    PriorityMessageQueue,
)


class QueueManager:
    def __init__(self):
        self.queueManager = PriorityMessageQueue()

    def add(self, message):
        self.queueManager.addMessage(message)

    def remove(self):
        if len(self.queueManager.queue) <= 0:
            return None
        return self.queueManager.removeMessage()
