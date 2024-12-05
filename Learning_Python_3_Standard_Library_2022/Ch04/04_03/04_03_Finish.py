# Calendar Module
from datetime import datetime, timedelta
import calendar

now = datetime.now()

testDate = now + timedelta(days=2)
myFirstLinkedInCourse = now - timedelta(weeks=3)

print(testDate.date())
print(myFirstLinkedInCourse.date())

if testDate > myFirstLinkedInCourse:
    print("Comparison works")

cal = calendar.month(2024, 12)
print(cal)

cal2 = calendar.weekday(2024, 12, 3)
print(cal2)

print(calendar.isleap(1999))
print(calendar.isleap(2000))