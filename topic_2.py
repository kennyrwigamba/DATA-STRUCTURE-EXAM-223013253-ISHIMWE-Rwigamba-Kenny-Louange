class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        self.size = 0

    def is_full(self):
        
        return self.size == self.capacity

    def is_empty(self):
     
        return self.size == 0

    def enqueue(self, service_request):
       
        if self.is_full():
            return False
        
        if self.front == -1: 
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
            
        self.queue[self.rear] = service_request
        self.size += 1
        return True

    def dequeue(self):
        
        if self.is_empty():
            return None
            
        service_request = self.queue[self.front]
        if self.front == self.rear: 
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return service_request

class ServiceRequest:
    def __init__(self, customer_id, service_type, priority, timestamp):
        self.customer_id = customer_id
        self.service_type = service_type  
        self.priority = priority  
        self.timestamp = timestamp

    def __lt__(self, other):
        
        if self.priority != other.priority:
            return self.priority < other.priority
        return self.timestamp < other.timestamp

class ServiceRequestHeap:
    def __init__(self):
        
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, service_request):
        
        self.heap.append(service_request)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def _heapify_down(self, i):
        
        min_idx = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_idx]:
            min_idx = left

        if right < len(self.heap) and self.heap[right] < self.heap[min_idx]:
            min_idx = right

        if min_idx != i:
            self.swap(i, min_idx)
            self._heapify_down(min_idx)

    def get_highest_priority(self):
        
        if not self.heap:
            return None
        return self.heap[0]

    def extract_highest_priority(self):
        
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root


def test_service_structures():
    
    queue = CircularQueue(5)
    heap = ServiceRequestHeap()
    
    
    import time
    requests = [
        ServiceRequest(1, "plumber", 2, time.time()),
        ServiceRequest(2, "electrician", 1, time.time()),
        ServiceRequest(3, "plumber", 3, time.time()),
        ServiceRequest(4, "electrician", 1, time.time()),
        ServiceRequest(5, "plumber", 2, time.time())
    ]
    
   
    print("Testing Circular Queue:")
    for request in requests:
        if queue.enqueue(request):
            print(f"Added request from customer {request.customer_id}")
    
    print("\nProcessing queue:")
    while not queue.is_empty():
        request = queue.dequeue()
        print(f"Processing customer {request.customer_id}'s {request.service_type} request")
    
  
    print("\nTesting Priority Heap:")
    for request in requests:
        heap.insert(request)
        print(f"Added request from customer {request.customer_id} with priority {request.priority}")
    
    print("\nProcessing heap by priority:")
    while heap.heap:
        request = heap.extract_highest_priority()
        print(f"Processing customer {request.customer_id}'s {request.service_type} request (Priority: {request.priority})")

if __name__ == "__main__":
    test_service_structures()