from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def format_day(self, day):
        day_number = ''
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {day_number} </ul></td>"
        return '<td></td>'

    def format_week(self, theweek):
        week = ''
        for day_number, weekday in theweek:
            week += self.format_day(day_number)
        return f'<tr> {week} </tr>'

    def format_month(self, withyear=True):
        cal = f'<table border="0" cellpadding="0" cellspacing="0"     class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.format_week(week)}\n'
        cal += "</table>"
        return cal
