import random

class OrganizationFuzzer:
    PREFIXES = ["North", "South", "East", "West", "Central", "New", "Saint", "United", "Royal", "Grand"]
    NAMES = ["Valley", "Mountain", "River", "Forest", "Harbor", "Coast", "Lake", "Hill", "Field", "Bay"]
    TYPES = ["University", "Institute of Technology", "College", "Polytechnic", "Academy", "School of Science"]
    COLOUR_THEMES = ["Red", "Blue", "Green"]
    PLACEHOLDER_LOGO = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg=="
    )

    @staticmethod
    def random_university_name():
        return f"{random.choice(OrganizationFuzzer.PREFIXES)} " \
               f"{random.choice(OrganizationFuzzer.NAMES)} " \
               f"{random.choice(OrganizationFuzzer.TYPES)}"

    @staticmethod
    def random_colour_theme():
        return random.choice(OrganizationFuzzer.COLOUR_THEMES)

    @staticmethod
    def random_base64_logo():
        return OrganizationFuzzer.PLACEHOLDER_LOGO

    def generate(self):
        return {
            "name": self.random_university_name(),
            "colour_theme": self.random_colour_theme(),
            "logo_base64": self.random_base64_logo()
        }
