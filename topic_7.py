class ServiceBooking:
    def __init__(self, booking_id, customer_name, service_type, emergency_level, 
                 scheduled_time, estimated_duration, is_premium_customer=False):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.service_type = service_type  
        self.emergency_level = emergency_level  
        self.scheduled_time = scheduled_time
        self.estimated_duration = estimated_duration  
        self.is_premium_customer = is_premium_customer
        self.priority_score = self._calculate_priority_score()

    def _calculate_priority_score(self):
        
        score = 0
        
        score += (6 - self.emergency_level) * 100  
        
        if self.is_premium_customer:
            score += 50
            
        return score

    def __str__(self):
        return (f"Booking {self.booking_id}: {self.customer_name} - "
                f"{self.service_type} (Emergency Level: {self.emergency_level}, "
                f"Priority Score: {self.priority_score})")

class ServiceBookingSorter:
    @staticmethod
    def merge_sort(bookings, sort_key='priority'):
    
        if len(bookings) <= 1:
            return bookings
            
        mid = len(bookings) // 2
        left = bookings[:mid]
        right = bookings[mid:]
        
        # Recursively sort both halves
        left = ServiceBookingSorter.merge_sort(left, sort_key)
        right = ServiceBookingSorter.merge_sort(right, sort_key)
        
        return ServiceBookingSorter._merge(left, right, sort_key)

    @staticmethod
    def _merge(left, right, sort_key):
        
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if ServiceBookingSorter._compare_bookings(left[i], right[j], sort_key):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    @staticmethod
    def _compare_bookings(booking1, booking2, sort_key):
        if sort_key == 'priority':
            return booking1.priority_score > booking2.priority_score
        elif sort_key == 'time':
            return booking1.scheduled_time < booking2.scheduled_time
        elif sort_key == 'duration':
            return booking1.estimated_duration < booking2.estimated_duration
        elif sort_key == 'emergency':
            return booking1.emergency_level < booking2.emergency_level
        else:
            return booking1.booking_id < booking2.booking_id

    @staticmethod
    def sort_by_multiple_criteria(bookings):
        if len(bookings) <= 1:
            return bookings
            
        mid = len(bookings) // 2
        left = bookings[:mid]
        right = bookings[mid:]
        
        left = ServiceBookingSorter.sort_by_multiple_criteria(left)
        right = ServiceBookingSorter.sort_by_multiple_criteria(right)
        
        return ServiceBookingSorter._merge_multiple_criteria(left, right)

    @staticmethod
    def _merge_multiple_criteria(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i].emergency_level < right[j].emergency_level:
                result.append(left[i])
                i += 1
            elif left[i].emergency_level > right[j].emergency_level:
                result.append(right[j])
                j += 1
            else:
                if left[i].is_premium_customer and not right[j].is_premium_customer:
                    result.append(left[i])
                    i += 1
                elif not left[i].is_premium_customer and right[j].is_premium_customer:
                    result.append(right[j])
                    j += 1
                else:
                    if left[i].scheduled_time <= right[j].scheduled_time:
                        result.append(left[i])
                        i += 1
                    else:
                        result.append(right[j])
                        j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

def test_service_booking_sort():
    bookings = [
        ServiceBooking(1, "Muhire Smith", "plumber", 3, "2025-01-04 10:00", 60, False),
        ServiceBooking(2, "Rukundo Johnson", "electrician", 1, "2025-01-04 09:00", 120, True),
        ServiceBooking(3, "Rukara Wilson", "plumber", 2, "2025-01-04 11:00", 45, True),
        ServiceBooking(4, "Mutesi Sarah", "electrician", 4, "2025-01-04 14:00", 90, False),
        ServiceBooking(5, "Kalisa Davis", "plumber", 1, "2025-01-04 13:00", 30, False)
    ]
    
    print("Sorting by priority score:")
    priority_sorted = ServiceBookingSorter.merge_sort(bookings, 'priority')
    for booking in priority_sorted:
        print(booking)
    
    print("\nSorting by emergency level:")
    emergency_sorted = ServiceBookingSorter.merge_sort(bookings, 'emergency')
    for booking in emergency_sorted:
        print(booking)
    
    print("\nSorting by multiple criteria (emergency level, premium status, time):")
    multi_sorted = ServiceBookingSorter.sort_by_multiple_criteria(bookings)
    for booking in multi_sorted:
        print(booking)

    print("\nSorting by estimated duration:")
    duration_sorted = ServiceBookingSorter.merge_sort(bookings, 'duration')
    for booking in duration_sorted:
        print(booking)

if __name__ == "__main__":
    test_service_booking_sort()