class ServiceBooking:
    def __init__(self, booking_id, customer_name, service_type, date, status="pending"):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.service_type = service_type  
        self.date = date
        self.status = status  

class BSTNode:
    def __init__(self, booking):
        self.booking = booking
        self.left = None
        self.right = None

class ServiceBookingBST:
    def __init__(self):
        self.root = None
        self.total_bookings = 0

    def insert(self, booking):
        
        if not self.root:
            self.root = BSTNode(booking)
        else:
            self._insert_recursive(self.root, booking)
        self.total_bookings += 1

    def _insert_recursive(self, node, booking):
        
        if booking.booking_id < node.booking.booking_id:
            if node.left is None:
                node.left = BSTNode(booking)
            else:
                self._insert_recursive(node.left, booking)
        else:
            if node.right is None:
                node.right = BSTNode(booking)
            else:
                self._insert_recursive(node.right, booking)

    def search(self, booking_id):
        
        return self._search_recursive(self.root, booking_id)

    def _search_recursive(self, node, booking_id):
        
        if node is None or node.booking.booking_id == booking_id:
            return node
        
        if booking_id < node.booking.booking_id:
            return self._search_recursive(node.left, booking_id)
        return self._search_recursive(node.right, booking_id)

    def update_booking_status(self, booking_id, new_status):
        
        node = self.search(booking_id)
        if node:
            node.booking.status = new_status
            return True
        return False

    def get_bookings_by_service(self, service_type):
        
        bookings = []
        self._inorder_service_type(self.root, service_type, bookings)
        return bookings

    def _inorder_service_type(self, node, service_type, bookings):
        
        if node:
            self._inorder_service_type(node.left, service_type, bookings)
            if node.booking.service_type == service_type:
                bookings.append(node.booking)
            self._inorder_service_type(node.right, service_type, bookings)

    def get_bookings_by_status(self, status):
        
        bookings = []
        self._inorder_status(self.root, status, bookings)
        return bookings

    def _inorder_status(self, node, status, bookings):
        
        if node:
            self._inorder_status(node.left, status, bookings)
            if node.booking.status == status:
                bookings.append(node.booking)
            self._inorder_status(node.right, status, bookings)

    def delete_booking(self, booking_id):
        
        self.root = self._delete_recursive(self.root, booking_id)

    def _delete_recursive(self, node, booking_id):
        
        if not node:
            return node

        if booking_id < node.booking.booking_id:
            node.left = self._delete_recursive(node.left, booking_id)
        elif booking_id > node.booking.booking_id:
            node.right = self._delete_recursive(node.right, booking_id)
        else:
           
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
              
            temp = self._min_value_node(node.right)
            node.booking = temp.booking
            node.right = self._delete_recursive(node.right, temp.booking.booking_id)
        
        return node

    def _min_value_node(self, node):
        
        current = node
        while current.left:
            current = current.left
        return current

    def print_all_bookings(self):
   
        self._inorder_print(self.root)

    def _inorder_print(self, node):
        
        if node:
            self._inorder_print(node.left)
            print(f"Booking ID: {node.booking.booking_id}, "
                  f"Customer: {node.booking.customer_name}, "
                  f"Service: {node.booking.service_type}, "
                  f"Status: {node.booking.status}")
            self._inorder_print(node.right)


def test_service_booking_bst():
    
    bst = ServiceBookingBST()
    
    
    bookings = [
        ServiceBooking(101, "Muhire John", "plumber", "2025-01-04"),
        ServiceBooking(103, "Kalisa Smith", "electrician", "2025-01-04"),
        ServiceBooking(102, "Rukundo Johnson", "plumber", "2025-01-05"),
        ServiceBooking(105, "Butera Brown", "electrician", "2025-01-05"),
        ServiceBooking(104, "Rukara Wilson", "plumber", "2025-01-06")
    ]
    
    
    print("Adding bookings to BST:")
    for booking in bookings:
        bst.insert(booking)
        print(f"Added booking {booking.booking_id} for {booking.customer_name}")
    
    print("\nAll bookings in order:")
    bst.print_all_bookings()
    
    
    print("\nSearching for booking 103:")
    result = bst.search(103)
    if result:
        print(f"Found booking for {result.booking.customer_name}")
    
    
    print("\nUpdating booking 102 status to 'confirmed':")
    bst.update_booking_status(102, "confirmed")
    
    
    print("\nPlumber bookings:")
    plumber_bookings = bst.get_bookings_by_service("plumber")
    for booking in plumber_bookings:
        print(f"Booking {booking.booking_id}: {booking.customer_name}")
    
    
    print("\nDeleting booking 104:")
    bst.delete_booking(104)
    
    print("\nFinal booking list:")
    bst.print_all_bookings()

if __name__ == "__main__":
    test_service_booking_bst()