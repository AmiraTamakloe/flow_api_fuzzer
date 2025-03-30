import random
from base_fuzzer import BaseFuzzer
from datetime import datetime, timedelta


class ExcursionFuzzer:
    EXPEDITION_NAMES = [ "BAHAMAS BEACH", "IPANEMA", "COPACABANA", "SUNSET BEACH", "SUNNY BEACH", "SUNNY ISLAND", "SUNNY COAST", "SUNNY COVE", "SUNNY BAY", "SUNNY HAVEN"]

    def __init__(self, user_ids=None):
        self.user_ids = user_ids or []
        self.creator_id = None

    def random_name(self):
        return random.choice(self.EXPEDITION_NAMES)


    def generate(self):
        start_date = BaseFuzzer.random_date().strftime("%Y-%m-%dT%H:%M:%SZ")
        end_date = (BaseFuzzer.random_date() + timedelta(minutes=random.randint(0, 59))).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.creator_id = random.choice(self.user_ids) if self.user_ids else None
        return {
            "creator_id": self.creator_id,
            "name": self.random_name(),
            "created_at": start_date,
            "is_active": BaseFuzzer.random_bool(),
            "finished_at": end_date
        }

    def generate_user_excursion(self, excursion_id=None):
        user_id = random.choice(self.user_ids)
        if excursion_id == None:
            return 
        while True:
            user_id = random.choice(self.user_ids)
            if user_id != self.creator_id:
                break

        print("user_id", user_id)
        return {
            "user_id": user_id,
            "excursion_id": excursion_id
        }