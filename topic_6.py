class ServiceNode:
    def __init__(self, node_id, name, node_type):
        self.node_id = node_id
        self.name = name
        self.node_type = node_type  
        self.children = []
        self.parent = None
        self.attributes = {}  

class ServiceHierarchyTree:
    def __init__(self):
        
        self.root = ServiceNode(0, "Service Hierarchy", "root")
        self.node_count = 1

    def add_node(self, parent_id, name, node_type, attributes=None):
        
        if attributes is None:
            attributes = {}
            
        
        parent = self._find_node(self.root, parent_id)
        if not parent:
            return None

       
        self.node_count += 1
        new_node = ServiceNode(self.node_count, name, node_type)
        new_node.parent = parent
        new_node.attributes = attributes
        parent.children.append(new_node)
        return new_node

    def _find_node(self, current_node, node_id):
        
        if current_node.node_id == node_id:
            return current_node
            
        for child in current_node.children:
            result = self._find_node(child, node_id)
            if result:
                return result
        return None

    def get_path_to_node(self, node_id):
       
        node = self._find_node(self.root, node_id)
        if not node:
            return []
            
        path = []
        current = node
        while current:
            path.append(current)
            current = current.parent
        return list(reversed(path))

    def get_nodes_by_type(self, node_type):
        
        nodes = []
        self._collect_nodes_by_type(self.root, node_type, nodes)
        return nodes

    def _collect_nodes_by_type(self, node, node_type, nodes):
        
        if node.node_type == node_type:
            nodes.append(node)
            
        for child in node.children:
            self._collect_nodes_by_type(child, node_type, nodes)

    def get_hierarchy_stats(self):
        
        stats = {
            'total_nodes': 0,
            'node_types': {},
            'max_depth': 0,
            'leaf_nodes': 0
        }
        self._calculate_stats(self.root, 0, stats)
        return stats

    def _calculate_stats(self, node, depth, stats):
        
        stats['total_nodes'] += 1
        stats['max_depth'] = max(stats['max_depth'], depth)
        
        if node.node_type not in stats['node_types']:
            stats['node_types'][node.node_type] = 0
        stats['node_types'][node.node_type] += 1
        
        if not node.children:
            stats['leaf_nodes'] += 1
            
        for child in node.children:
            self._calculate_stats(child, depth + 1, stats)

    def get_providers_in_area(self, area_node_id):
       
        area_node = self._find_node(self.root, area_node_id)
        if not area_node or area_node.node_type != "area":
            return []
            
        providers = []
        self._collect_providers(area_node, providers)
        return providers

    def _collect_providers(self, node, providers):
        
        if node.node_type == "provider":
            providers.append(node)
            
        for child in node.children:
            self._collect_providers(child, providers)

    def print_hierarchy(self, node=None, level=0):
        
        if node is None:
            node = self.root
            
        print("  " * level + f"└─ {node.name} ({node.node_type})")
        for child in node.children:
            self.print_hierarchy(child, level + 1)

    def get_bookings_for_provider(self, provider_id):
       
        provider_node = self._find_node(self.root, provider_id)
        if not provider_node or provider_node.node_type != "provider":
            return []
            
        bookings = []
        for child in provider_node.children:
            if child.node_type == "booking":
                bookings.append(child)
        return bookings


def test_service_hierarchy():
    
    hierarchy = ServiceHierarchyTree()
    
    
    north = hierarchy.add_node(0, "North Region", "area")
    south = hierarchy.add_node(0, "South Region", "area")
    
    
    plumbing_north = hierarchy.add_node(north.node_id, "Plumbing Services", "service_type", 
                                      {"description": "All plumbing services"})
    electrical_north = hierarchy.add_node(north.node_id, "Electrical Services", "service_type",
                                        {"description": "All electrical services"})
    
   
    provider1 = hierarchy.add_node(plumbing_north.node_id, "John's Plumbing", "provider",
                                 {"rating": 4.5, "years_experience": 10})
    provider2 = hierarchy.add_node(electrical_north.node_id, "Elite Electricians", "provider",
                                 {"rating": 4.8, "years_experience": 15})
    
    
    booking1 = hierarchy.add_node(provider1.node_id, "Emergency Pipe Repair", "booking",
                                {"customer": "Alice Smith", "time": "2025-01-04 10:00"})
    booking2 = hierarchy.add_node(provider2.node_id, "Wiring Installation", "booking",
                                {"customer": "Bob Johnson", "time": "2025-01-04 14:00"})
    
    
    print("Service Hierarchy Structure:")
    hierarchy.print_hierarchy()
    
    
    print("\nHierarchy Statistics:")
    stats = hierarchy.get_hierarchy_stats()
    print(f"Total Nodes: {stats['total_nodes']}")
    print(f"Max Depth: {stats['max_depth']}")
    print("Node Types:", stats['node_types'])
    
    
    print("\nProviders in North Region:")
    providers = hierarchy.get_providers_in_area(north.node_id)
    for provider in providers:
        print(f"- {provider.name} ({provider.attributes.get('rating', 'N/A')} stars)")
    
    
    print("\nPath to booking:")
    path = hierarchy.get_path_to_node(booking1.node_id)
    path_names = [node.name for node in path]
    print(" -> ".join(path_names))

if __name__ == "__main__":
    test_service_hierarchy()