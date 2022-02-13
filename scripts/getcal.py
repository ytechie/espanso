from time import strftime
import icalendar
import recurring_ical_events
from datetime import datetime, date, time, timedelta
from urllib import request
import os

if 'ical' not in os.environ:
    print("Missing ical environment variable")
    exit()

ical_url = os.environ['ical']

#ical_string = request.urlopen(ical_url).read()
ical_string = open('cal.ics','rb').read()

calendar = icalendar.Calendar.from_ical(ical_string)
events = recurring_ical_events.of(calendar).at(date.today() - timedelta(days=2))

def eventSort(e):
    print(type(e))
    return 4
    s = e["DTSTART"].dt
    if(s is datetime):
        o = s
    elif(s is date):
        o = datetime.combine(s, datetime.min.time())
    else:
        o = datetime.max
    return o.strftime("%Y-%m-d %H:%M")

for event in events:#.sort(key=eventSort):
    print(type(event))
    start = event["DTSTART"].dt
    end = event["DTEND"].dt
    duration = event["DTEND"].dt - event["DTSTART"].dt
    print("{}-{} {}".format(start.strftime("%I:%M"), end.strftime("%I:%M"), event["summary"]))