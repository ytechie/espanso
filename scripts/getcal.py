import icalendar
import recurring_ical_events
from datetime import datetime, date, timedelta
from urllib import request
import os

ical_url = os.environ['ical']
if(ical_url == ""):
    print("Missing ical environment variable")
    exit()

ical_string = request.urlopen(ical_url).read()
#ical_string = open('cal.ics','rb').read()

calendar = icalendar.Calendar.from_ical(ical_string)
events = recurring_ical_events.of(calendar).at(date.today() - timedelta(days=2))

for event in events:
    start = event["DTSTART"].dt
    end = event["DTEND"].dt
    duration = event["DTEND"].dt - event["DTSTART"].dt
    print("{}-{} {}".format(start.strftime("%-I:%M"), end.strftime("%-I:%M"), event["summary"]))