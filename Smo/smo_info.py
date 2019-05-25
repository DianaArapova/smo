import random

from Smo.state_of_queue import StateOfQueue


class NewPeopleInfo:
    def __init__(self, people_id, time_when_arrives):
        self.people_id = people_id
        self.time_when_arrives = time_when_arrives

    def __repr__(self):
        return str(self.people_id)


class SMO:
    def __init__(self, id, init_people, is_terminal, random_seed):
        self.random_seed = random_seed
        self.id = id
        self.people_in_smo = init_people
        self.is_terminal = is_terminal
        self.neighbours = []
        self.queue_in_smo = StateOfQueue()

    def add_info_about_smo_neighbour(self, smo_id):
        self.neighbours.append(smo_id)

    def take_away_people(self, leave_people_ids):
        for people_id in leave_people_ids:
            self.__delete_people_by_id__(people_id)

    def __delete_people_by_id__(self, id):
        for i in range(len(self.people_in_smo)):
            if self.people_in_smo[i].people_id == id:
                del(self.people_in_smo[i])
                return

    def add_new_people(self, new_people_info):
        for people_info in new_people_info:
            self.people_in_smo.append(people_info)

    def generate_peoples_desires(self, t_start, t_end, max_people_count=-1):
        print(f"start time {t_start} finish time {t_end}")
        print(f"smo id {self.id} peoples in it: {self.people_in_smo}")
        count_of_people_not_in_queue = len(self.people_in_smo) - self.queue_in_smo.get_count_of_people_in_queue()
        if max_people_count == -1:
            max_people_count = count_of_people_not_in_queue

        peoples_info = self.people_in_smo.copy()
        random.shuffle(peoples_info)

        count_people_with_desires = min(max_people_count, count_of_people_not_in_queue)

        if len(self.neighbours) == 0:
            return

        for people_info in peoples_info:
            #todo: make generation of time зависимой от часов пик
            if count_people_with_desires == 0:
                break
            if int(people_info.time_when_arrives) + 1 >= t_end:
                continue

            t_generate = random.randint(max(t_start, int(people_info.time_when_arrives) + 1), t_end)
            index_smo_neighbor = random.randint(0, len(self.neighbours) - 1)

            if self.queue_in_smo.add_people(
                    start_time_in_queue=t_generate,
                    route=self.neighbours[index_smo_neighbor],
                    people_id=people_info.people_id):
                count_people_with_desires -= 1

    def add_exclusive_people_to_the_queue(self, t_start, route, id_of_exclusive_people):
        self.queue_in_smo.add_people(start_time_in_queue=t_start, route=route, people_id=id_of_exclusive_people)
