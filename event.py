class Event:
    def __init__(self, title, location, start_time, duration, owner, participants):
        self.participants = participants
        self.owner = owner
        self.duration = duration
        self.start_time = start_time
        self.location = location
        self.title = title