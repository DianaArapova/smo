class StateOfQueue:
    def __init__(self):
        self.waiting = []

    def add_people(self, start_time_in_queue, route, people_id):
        if self.__contains_people_with_id__(people_id):
            return False
        self.waiting.append((start_time_in_queue, route, people_id))
        return True

    def get_first_people_from_queue(self, route_number, max_people_count, max_time):
        print(f"!!! {self.waiting}")
        waiters = []
        sorted(self.waiting, key=lambda w: w[0])
        i = 0
        while i < len(self.waiting):
            waiter = self.waiting[i]
            if waiter[0] > max_time:
                return []
            if waiter[1] == route_number:
                waiters.append(waiter[2])
                del(self.waiting[i])
            else:
                i += 1
            if len(waiters) == max_people_count:
                return waiters
        print(f"!!! {self.waiting}")
        return waiters

    def __contains_people_with_id__(self, people_id):
        for waiter in self.waiting:
            if waiter[2] == people_id:
                return True
        return False

    def get_count_of_people_in_queue(self):
        return len(self.waiting)

