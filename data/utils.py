from datetime import datetime, timedelta
from random import random, randint
import json

class EventGenerator:
    def __init__(self):
        self.titles = ['Learn python', "Drink beer", "Do something"]
        self.locations = ['Wwa', 'LA', "Krk"]
        self.users = ["Ala", "Ola", "Ela", "Ula", "Roman"]
        self.events =[]

    def generate(self, quantity=100):
        for _ in range(quantity):
            event = Event(
                title=random.choice(self.titles),
                location=random.choice(self.locations),
                start_time=f'{('datetime.now() + timedelta(minutes=random.randint(50,50000)))}'',
                duration=random.randint(16,599),
                owner=random.choice(self.users),
                participants=random.choices(self.users, k=random.randint(0, len(self.users)))
            )

            self.events.append(event)

    def generate_data(self, quantity=100):
        events_data = []

        for _ in range(quantity):
            event = {
                "title": random.choice(self.titles),
                "location": random.choice(self.locations),
                "start_time": f'{(datetime.now() + timedelta(minutes=random.randint(50, 500000))):%d-%m-%Y %H:%M}',
                "duration": random.randint(16, 599),
                "owner": random.choice(self.users),
                "participants": random.choices(self.users, k=random.randint(0,
                                                                            len(self.users)))
            }
            events_data.append(event)

        return events_data

    def save(self, path):
        with open(path, "w") as file:
            data = json.dumps(self.events, indent=4)
            file.write(data)

    @staticmethod
    def load(path):
        with open(path, 'r') as file:
            return json.load(file)
