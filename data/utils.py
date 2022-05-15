from datetime import datetime, timedelta
<<<<<<< HEAD
from random import random, randint
import json

=======
import random
import json

from event import Event


>>>>>>> 025a398 (final version of project)
class EventGenerator:
    def __init__(self):
        self.titles = ['Learn python', "Drink beer", "Do something"]
        self.locations = ['Wwa', 'LA', "Krk"]
        self.users = ["Ala", "Ola", "Ela", "Ula", "Roman"]
<<<<<<< HEAD
        self.events =[]

    def generate(self, quantity=100):
=======
        self.events = []

    def generate_events(self, quantity=100):
>>>>>>> 025a398 (final version of project)
        for _ in range(quantity):
            event = Event(
                title=random.choice(self.titles),
                location=random.choice(self.locations),
<<<<<<< HEAD
                start_time=f'{('datetime.now() + timedelta(minutes=random.randint(50,50000)))}'',
                duration=random.randint(16,599),
                owner=random.choice(self.users),
                participants=random.choices(self.users, k=random.randint(0, len(self.users)))
            )

=======
                start_time=f'{(datetime.now() + timedelta(minutes=random.randint(50, 50000))):%d-%m-%Y %H:%M}',
                duration=random.randint(16, 599),
                owner=random.choice(self.users),
                participants=random.choices(self.users, k=random.randint(0, len(self.users)))
            )
>>>>>>> 025a398 (final version of project)
            self.events.append(event)

    def generate_data(self, quantity=100):
        events_data = []
<<<<<<< HEAD

=======
>>>>>>> 025a398 (final version of project)
        for _ in range(quantity):
            event = {
                "title": random.choice(self.titles),
                "location": random.choice(self.locations),
                "start_time": f'{(datetime.now() + timedelta(minutes=random.randint(50, 500000))):%d-%m-%Y %H:%M}',
                "duration": random.randint(16, 599),
                "owner": random.choice(self.users),
<<<<<<< HEAD
                "participants": random.choices(self.users, k=random.randint(0,
                                                                            len(self.users)))
=======
                "participants": random.choices(self.users, k=random.randint(0, len(self.users)))
>>>>>>> 025a398 (final version of project)
            }
            events_data.append(event)

        return events_data

    def save(self, path):
        with open(path, "w") as file:
<<<<<<< HEAD
            data = json.dumps(self.events, indent=4)
=======
            data = json.dumps(self.generate_data(500), indent=4)
>>>>>>> 025a398 (final version of project)
            file.write(data)

    @staticmethod
    def load(path):
        with open(path, 'r') as file:
            return json.load(file)
