from time import strftime
import icalendar
import recurring_ical_events
from datetime import datetime, date, time, timedelta, tzinfo
from urllib import request
import os

if 'ical' not in os.environ:
    print("Missing ical environment variable")
    exit()

ical_url = os.environ['ical']

ical_string = request.urlopen(ical_url).read()
#ical_string = open('cal.ics','rb').read()

calendar = icalendar.Calendar.from_ical(ical_string)
events = recurring_ical_events.of(calendar).at(date.today() - timedelta(days=0))

def eventSort(e):
    s = e["DTSTART"].dt
    o = datetime.max
    if(type(s) is datetime):
        o = s
    elif(type(s) is date):
        o = datetime.combine(s, datetime.min.time())
        
    return o.strftime("%Y-%m-%d %H:%M")

#events.sort(key=eventSort)
for event in sorted(events, key=eventSort):
    start = event["DTSTART"].dt
    end = event["DTEND"].dt

    if(type(start) is date):
        start = datetime.combine(start, datetime.min.time())
    if(type(end) is date):
        end = datetime.combine(end, datetime.min.time())

    print("{}-{} {}".format(start.astimezone().strftime("%I:%M"), end.astimezone().strftime("%I:%M"), event["summary"]))