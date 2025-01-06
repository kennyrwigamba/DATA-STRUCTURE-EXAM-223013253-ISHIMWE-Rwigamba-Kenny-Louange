class ServiceBooking:
    def __init__(self, booking_id, customer_name, service_type, scheduled_time, price):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.service_type = service_type  
        self.scheduled_time = scheduled_time
        self.price = price
        self.status = "scheduled"  

class AVLNode:
    def __init__(self, booking):
        self.booking = booking
        self.left = None
        self.right = None
        self.height = 1
        self.subtree_size = 1  

class ServiceTrackingAVL:
    def __init__(self):
        self.root = None
        self.total_revenue = 0
        self.service_counts = {"plumber": 0, "electrician": 0}

    def height(self, node):
        
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
       
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height_and_size(self, node):
        
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        node.subtree_size = (self.get_size(node.left) + 
                           self.get_size(node.right) + 1)

    def get_size(self, node):
        
        if not node:
            return 0
        return node.subtree_size

    def right_rotate(self, y):
        
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height_and_size(y)
        self.update_height_and_size(x)

        return x

    def left_rotate(self, x):
       
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height_and_size(x)
        self.update_height_and_size(y)

        return y

    def insert(self, booking):
        
        self.root = self._insert_recursive(self.root, booking)
        self.service_counts[booking.service_type] += 1
        if booking.status == "completed":
            self.total_revenue += booking.price

    def _insert_recursive(self, node, booking):
        
        if not node:
            return AVLNode(booking)

        if booking.booking_id < node.booking.booking_id:
            node.left = self._insert_recursive(node.left, booking)
        else:
            node.right = self._insert_recursive(node.right, booking)

        self.update_height_and_size(node)
        balance = self.balance_factor(node)

        
        if balance > 1 and booking.booking_id < node.left.booking.booking_id:
            return self.right_rotate(node)

       
        if balance < -1 and booking.booking_id > node.right.booking.booking_id:
            return self.left_rotate(node)

        
        if balance > 1 and booking.booking_id > node.left.booking.booking_id:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        
        if balance < -1 and booking.booking_id < node.right.booking.booking_id:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def find_booking(self, booking_id):
        
        return self._find_recursive(self.root, booking_id)

    def _find_recursive(self, node, booking_id):
        
        if not node:
            return None
        if booking_id == node.booking.booking_id:
            return node
        if booking_id < node.booking.booking_id:
            return self._find_recursive(node.left, booking_id)
        return self._find_recursive(node.right, booking_id)

    def update_booking_status(self, booking_id, new_status):
        
        node = self.find_booking(booking_id)
        if node:
            old_status = node.booking.status
            node.booking.status = new_status
            
           
            if new_status == "completed" and old_status != "completed":
                self.total_revenue += node.booking.price
            elif old_status == "completed" and new_status != "completed":
                self.total_revenue -= node.booking.price
            
            return True
        return False

    def get_bookings_in_range(self, start_id, end_id):
        
        bookings = []
        self._range_search_recursive(self.root, start_id, end_id, bookings)
        return bookings

    def _range_search_recursive(self, node, start_id, end_id, bookings):
        
        if not node:
            return

        if start_id < node.booking.booking_id:
            self._range_search_recursive(node.left, start_id, end_id, bookings)

        if start_id <= node.booking.booking_id <= end_id:
            bookings.append(node.booking)

        if end_id > node.booking.booking_id:
            self._range_search_recursive(node.right, start_id, end_id, bookings)

    def get_service_metrics(self):
        
        return {
            "total_revenue": self.total_revenue,
            "service_counts": self.service_counts,
            "total_bookings": sum(self.service_counts.values())
        }

    def print_tree_structure(self):
       
        self._print_recursive(self.root, 0)

    def _print_recursive(self, node, level):
       
        if node:
            self._print_recursive(node.right, level + 1)
            print("    " * level + f"ID: {node.booking.booking_id} " +
                  f"(BF: {self.balance_factor(node)}, " +
                  f"Size: {node.subtree_size})")
            self._print_recursive(node.left, level + 1)


def test_service_tracking_avl():

    avl = ServiceTrackingAVL()
    
   
    bookings = [
        ServiceBooking(50, "Rukundo Smith", "plumber", "2025-01-04 10:00", 150),
        ServiceBooking(30, "Muhire Johnson", "electrician", "2025-01-04 11:00", 200),
        ServiceBooking(70, "Rukara Wilson", "plumber", "2025-01-04 13:00", 175),
        ServiceBooking(20, "Mutesi Sarah", "electrician", "2025-01-04 14:00", 225),
        ServiceBooking(60, "Kalisa Davis", "plumber", "2025-01-04 15:00", 160)
    ]
    
    
    print("Adding bookings to AVL tree:")
    for booking in bookings:
        avl.insert(booking)
        print(f"Added booking {booking.booking_id} for {booking.customer_name}")
    
    
    print("\nAVL Tree structure:")
    avl.print_tree_structure()
    
    
    print("\nUpdating bookings to completed:")
    avl.update_booking_status(30, "completed")
    avl.update_booking_status(50, "completed")
    

    metrics = avl.get_service_metrics()
    print("\nService Metrics:")
    print(f"Total Revenue: ${metrics['total_revenue']}")
    print("Service Counts:", metrics['service_counts'])
    print(f"Total Bookings: {metrics['total_bookings']}")
    
  
    print("\nBookings between ID 30 and 60:")
    range_bookings = avl.get_bookings_in_range(30, 60)
    for booking in range_bookings:
        print(f"ID: {booking.booking_id}, Customer: {booking.customer_name}")

if __name__ == "__main__":
    test_service_tracking_avl()