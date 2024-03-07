# from Design_Patterns.priority_queue_pattern.backgroundWorker import Worker
# from Design_Patterns.priority_queue_pattern.message import Message
# from Design_Patterns.priority_queue_pattern.queueManager import QueueManager
#from .priorityMessageQueue import PriorityMessageQueue
from queueManager import QueueManager
from message import Message
from backgroundWorker import Worker

if __name__ == '__main__':
    queueManager = QueueManager()
    queueManager.add(Message("First",20))
    queueManager.add(Message("Second",1))
    queueManager.add(Message("Third",5))
    queueManager.add(Message("Fourth",5))
    worker = Worker(queueManager)
    worker.run()