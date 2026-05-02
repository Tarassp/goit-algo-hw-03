from datetime import datetime

def get_days_from_today(date):
    try:
        dt = datetime.strptime(date, "%Y-%m-%d").date()  #fromisoformat(date)
    except TypeError:
        raise TypeError("Expected a string")
    except ValueError:
        raise ValueError(f"Expected format (YYYY-MM-DD), got: {date!r}")
    return (datetime.today().date() - dt).days
