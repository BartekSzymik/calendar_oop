from pprint import pprint as pp

from custom_calendar import Calendar
from data.utils import EventGenerator
from event import Event

data = EventGenerator()
data.generate(500)

c = Calendar

result = c.get_events_by_date("17-05-2022 8:00")

# print(result)

c.remove_event('17-05-2022 9:00')
print(c)