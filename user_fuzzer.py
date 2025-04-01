import random
from base_fuzzer import BaseFuzzer
import base64


class UserFuzzer:

    def __init__(self, organization_ids):
        self.organization_ids = organization_ids

    @staticmethod
    def random_username():
        return f"user{random.randint(0, 1_000_000)}"

    @staticmethod
    def random_email():
        return f"user{random.randint(0, 1_000_000)}@gmail.com"

    @staticmethod
    def random_image_url():
        with open("./IMG_4264.jpeg", "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
        return "data:image/jpeg;base64," + base64_string

    @staticmethod
    def random_inscription_date():
        return BaseFuzzer.random_date().strftime("%Y-%m-%dT%H:%M:%SZ")

    def random_organization_id(self):
        return random.choice(self.organization_ids)

    def generate(self):
        return {
            "username": self.random_username(),
            "email": self.random_email(),
            "image_url": self.random_image_url(),
            "association": BaseFuzzer.random_int(),
            "date_inscription": self.random_inscription_date(),
            "notification": BaseFuzzer.random_bool(),
            "localisation": BaseFuzzer.random_bool(),
            "langue": BaseFuzzer.random_int(),
            "macro_tutoriel": BaseFuzzer.random_bool(),
            "micro_tutoriel": BaseFuzzer.random_bool(),
            "materials": BaseFuzzer.random_bool(),
            "organization_id": self.random_organization_id(),
        }
