from pprint import pprint as pp

from custom_calendar import Calendar
from data.utils import EventGenerator
from event import Event

data = EventGenerator()
#data.save('./data.json')
events_data = data.load('./data.json')

events = [Event(**event) for event in events_data]
c = Calendar(events)
result = c.get_events_by_date("01-01-2023 00:00")
print(result, len(result))
#
# result = c.get_events_by_date("17-05-2022 8:00")
#
# # print(result)
#
# c.remove_event('17-05-2022 9:00')
# print(c)