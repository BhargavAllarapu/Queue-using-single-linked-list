length = 0
class Node:
    def __init__(self, data):
        self.data = data
        self.nextval = None

class Queue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def lengthOfQueue(self):
        global length
        return length

    def enqueue(self, data):
        global length
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            length += 1
            return "Data inserted in the queue."
        else:
            newNode.nextval = self.head
            self.head = newNode
            length += 1
            return "Data inserted in the queue."

    def dequeue(self):
        global length
        queue = self.head
        if queue is None:
            return "Nothing to delete.... Queue is empty."
        else:
            while queue.nextval is not None:
                temp = queue
                queue = queue.nextval
            temp.nextval = None
            del queue
            length -= 1
            return "Deleted"

    def printQueue(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.nextval
        return None

if __name__ == '__main__':
    q = Queue()
    print("Is Queue empty : "+str(q.isEmpty()))
    print(q.dequeue())
    print("Length of Queue : "+str(q.lengthOfQueue()))
    a = input("Enter : ")
    q.enqueue(a)
    b = input("Enter : ")
    q.enqueue(b)
    c = input("Enter : ")
    q.enqueue(c)
    d = input("Enter : ")
    q.enqueue(d)
    q.printQueue()
    print("-----------------")
    print(q.dequeue())
    q.printQueue()
    print("-----------------")
    print(q.dequeue())
    q.printQueue()
    print("-----------------")
    print(q.dequeue())
    q.printQueue()
    print("-----------------")
    print("Length of Queue : " + str(q.lengthOfQueue()))



