import random
from datetime import datetime, timedelta

class SampleFuzzer:
    def __init__(self, user_ids=None, excursion_ids=None):
        self.user_ids = user_ids or []
        self.excursion_ids = excursion_ids or []

    @staticmethod
    def random_date(start_year=2018, end_year=None):
        """Generate a random datetime between start_year and today"""
        end_year = end_year or datetime.now().year
        start = datetime(start_year, 1, 1)
        end = datetime.now()
        delta = end - start
        random_days = random.randint(0, delta.days)
        return start + timedelta(days=random_days)

    @staticmethod
    def random_time():
        """Return a random time as a datetime object (hour & minute)"""
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return datetime(2024, 1, 1, hour, minute)

    @staticmethod
    def random_float(min_val=0.0, max_val=100.0, decimals=2):
        return round(random.uniform(min_val, max_val), decimals)

    @staticmethod
    def random_int(min_val=0, max_val=100):
        return random.randint(min_val, max_val)

    @staticmethod
    def random_bool():
        return random.choice([True, False])

    def generate(self):
        sample_date = self.random_date()
        sample_time = self.random_time()
        high_tide_time = sample_time + timedelta(hours=random.randint(1, 4))

        return {
            "user_id": random.choice(self.user_ids) if self.user_ids else None,
            "excursion_id": random.choice(self.excursion_ids) if self.excursion_ids else None,
            "sample_date": sample_date.isoformat(),
            "sample_time": sample_time.isoformat(),
            "high_tide_time": high_tide_time.isoformat(),
            "tide_coefficient": self.random_float(20, 120),
            "number_of_students": self.random_int(5, 35),
            "collect_duration": self.random_float(0.5, 3.0),
            "sorting_duration": self.random_float(0.5, 2.0),
            "transect_length": self.random_float(5, 200),
            "start_gps_latitude": self.random_float(-90, 90, 6),
            "start_gps_longitude": self.random_float(-180, 180, 6),
            "end_gps_latitude": self.random_float(-90, 90, 6),
            "end_gps_longitude": self.random_float(-180, 180, 6),
            "immediate_infrastructure": self.random_bool(),
            "agglomeration_distance": self.random_float(0, 100),
            "waste_disposal_distance": self.random_float(0, 50),
            "macro_weight": self.random_float(0, 10),
            "macro_volume": self.random_float(0, 50),
            "total_macro_items": self.random_int(0, 300),
        }

