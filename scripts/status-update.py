from datetime import datetime

now = datetime.now()

weekAndYear = now.strftime("%W %Y")


status_string = "Status Update Week #{weekAndYear}"
status_string = status_string.format(weekAndYear = weekAndYear)
print(status_string)