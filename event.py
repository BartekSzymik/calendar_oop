from datetime import timedelta, datetime


class Event:
    def __init__(self, title, location, start_time, duration, owner, participants):
        self.title = title
        self.location = location
        self.start_time = start_time
        self.duration = duration
        self.owner = owner
        self.participants = participants

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if len(str(value)):
            self._title = value
        else:
            self._title = "No title"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not (10 < value < 600):
            raise ValueError(f'Too short or too long: {value}')

        self._duration = timedelta(minutes=value)

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, val):
        if not isinstance(val, str):
            raise TypeError(f'Invalid value: {val}')

        try:
            parsed_date = datetime.strptime(val, '%d-%m-%Y %H:')
        except ValueError:
            raise ValueError(f'Invalid date format, use DD-MM-YYYY HH:MM, {val}')

        if parsed_date < datetime.now() + timedelta(minutes=15):
            raise ValueError(f'Not enought time to organize a meeting : {parsed_date -datetime.now()}')

        self._start_time = val


e = Event('42', '', '14-05-2022 15:10', '11', '', '')
print(e.start_time)
