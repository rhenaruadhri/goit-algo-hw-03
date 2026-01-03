from datetime import datetime, date

def get_days_from_today(date_str):
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = date.today()
        return (today - given_date).days
    except ValueError:
        raise ValueError("Дата повинна бути у форматі 'YYYY-MM-DD'")

print(get_days_from_today("2021-10-09"))