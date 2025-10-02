from datetime import datetime

def get_days_from_today(date: str) -> int: #date is back to the function
        try:
                converted_time = datetime.strptime(date, "%Y-%m-%d").date() #converted_time is string in datetime object
        except ValueError:        
                return "Invalid time format, try again, please, use \"YYYY-MM-DD\" format."
         
        today = datetime.today().date() #adding .date() as attribute to get object without hours
        days_ahead = (converted_time - today).days #days_ahead is timedelta object, .days is an attribute
        return days_ahead #function returns calculated days difference. No loopers, no input request.
        
print(get_days_from_today("2026-03-26"))
