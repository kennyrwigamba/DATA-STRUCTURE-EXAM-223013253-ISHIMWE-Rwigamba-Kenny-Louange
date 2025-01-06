class ServiceOrder:
    def __init__(self, order_id, customer_name, service_type, urgency_level, timestamp):
        self.order_id = order_id
        self.customer_name = customer_name
        self.service_type = service_type  
        self.urgency_level = urgency_level  
        self.timestamp = timestamp
        self.status = "pending"  

class BinaryTreeNode:
    def __init__(self, order):
        self.order = order
        self.left = None
        self.right = None
        self.parent = None

class ServiceOrderTree:
    def __init__(self, max_orders):
        self.root = None
        self.max_orders = max_orders
        self.current_orders = 0
        self.last_inserted_level = 0
        self.last_inserted_position = 0

    def is_full(self):
        
        return self.current_orders >= self.max_orders

    def insert_order(self, order):
        
        if self.is_full():
            return False

        new_node = BinaryTreeNode(order)

        if not self.root:
            self.root = new_node
            self.current_orders += 1
            return True

        
        parent_node = self._find_next_parent()
        if not parent_node.left:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
        
        new_node.parent = parent_node
        self.current_orders += 1
        return True

    def _find_next_parent(self):
        
        if not self.root:
            return None

        queue = [self.root]
        while queue:
            node = queue[0]
            if not node.left or not node.right:
                return node
            queue.append(node.left)
            queue.append(node.right)
            queue.pop(0)
        return None

    def find_order(self, order_id):
        
        return self._find_order_recursive(self.root, order_id)

    def _find_order_recursive(self, node, order_id):
        
        if not node:
            return None
        if node.order.order_id == order_id:
            return node
        
        left_result = self._find_order_recursive(node.left, order_id)
        if left_result:
            return left_result
            
        return self._find_order_recursive(node.right, order_id)

    def update_order_status(self, order_id, new_status):
        
        node = self.find_order(order_id)
        if node:
            node.order.status = new_status
            return True
        return False

    def get_orders_by_service(self, service_type):
        
        orders = []
        self._collect_orders_by_service(self.root, service_type, orders)
        return orders

    def _collect_orders_by_service(self, node, service_type, orders):
        
        if not node:
            return
        
        if node.order.service_type == service_type:
            orders.append(node.order)
        
        self._collect_orders_by_service(node.left, service_type, orders)
        self._collect_orders_by_service(node.right, service_type, orders)

    def get_urgent_orders(self, urgency_threshold):
        
        urgent_orders = []
        self._collect_urgent_orders(self.root, urgency_threshold, urgent_orders)
        return urgent_orders

    def _collect_urgent_orders(self, node, urgency_threshold, urgent_orders):
        
        if not node:
            return
        
        if node.order.urgency_level <= urgency_threshold:
            urgent_orders.append(node.order)
        
        self._collect_urgent_orders(node.left, urgency_threshold, urgent_orders)
        self._collect_urgent_orders(node.right, urgency_threshold, urgent_orders)

    def print_orders_by_level(self):
        
        if not self.root:
            return

        queue = [self.root]
        level = 1
        nodes_in_current_level = 1
        nodes_in_next_level = 0

        print(f"\nLevel {level}:")
        while queue:
            node = queue.pop(0)
            nodes_in_current_level -= 1

            print(f"Order ID: {node.order.order_id}, "
                  f"Customer: {node.order.customer_name}, "
                  f"Service: {node.order.service_type}, "
                  f"Urgency: {node.order.urgency_level}, "
                  f"Status: {node.order.status}")

            if node.left:
                queue.append(node.left)
                nodes_in_next_level += 1
            if node.right:
                queue.append(node.right)
                nodes_in_next_level += 1

            if nodes_in_current_level == 0:
                if nodes_in_next_level > 0:
                    level += 1
                    print(f"\nLevel {level}:")
                nodes_in_current_level = nodes_in_next_level
                nodes_in_next_level = 0


def test_service_order_tree():
    import time
    
    
    tree = ServiceOrderTree(8)
    
    
    orders = [
        ServiceOrder(1, "Muhire Smith", "plumber", 2, time.time()),
        ServiceOrder(2, "Rukundo Johnson", "electrician", 1, time.time()),
        ServiceOrder(3, "Rukara Wilson", "plumber", 3, time.time()),
        ServiceOrder(4, "Mutesi Sarah", "electrician", 2, time.time()),
        ServiceOrder(5, "Kalisa Davis", "plumber", 1, time.time())
    ]
    
    
    print("Adding orders to tree:")
    for order in orders:
        if tree.insert_order(order):
            print(f"Added order {order.order_id} for {order.customer_name}")
    
    
    print("\nTree structure by level:")
    tree.print_orders_by_level()
    
    
    print("\nFinding order ID 3:")
    node = tree.find_order(3)
    if node:
        print(f"Found order for {node.order.customer_name}")
    
    
    print("\nUpdating order 2 status to 'assigned':")
    tree.update_order_status(2, "assigned")
    
    
    print("\nPlumber orders:")
    plumber_orders = tree.get_orders_by_service("plumber")
    for order in plumber_orders:
        print(f"Order {order.order_id}: {order.customer_name}")
    
    
    print("\nUrgent orders (urgency <= 2):")
    urgent_orders = tree.get_urgent_orders(2)
    for order in urgent_orders:
        print(f"Order {order.order_id}: {order.customer_name} (Urgency: {order.urgency_level})")

if __name__ == "__main__":
    test_service_order_tree()