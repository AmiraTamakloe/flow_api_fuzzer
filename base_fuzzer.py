import random
from datetime import datetime, timedelta

class BaseFuzzer:
    @staticmethod
    def random_bool():
        return random.choice([True, False])

    @staticmethod
    def random_int(min_val=0, max_val=1_000_000):
        return random.randint(min_val, max_val)

    @staticmethod
    def random_float(min_val=0.0, max_val=100.0, decimals=2):
        return round(random.uniform(min_val, max_val), decimals)

    @staticmethod
    def random_date(start_year=2018):
        start = datetime(start_year, 1, 1)
        end = datetime.now()
        return start + timedelta(days=random.randint(0, (end - start).days))

    @staticmethod
    def random_time():
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return datetime(2024, 1, 1, hour, minute)
