import random
import base64

class OrganizationFuzzer:
    PREFIXES = ["North", "South", "East", "West", "Central", "New", "Saint", "United", "Royal", "Grand"]
    NAMES = ["Valley", "Mountain", "River", "Forest", "Harbor", "Coast", "Lake", "Hill", "Field", "Bay"]
    TYPES = ["University", "Institute of Technology", "College", "Polytechnic", "Academy", "School of Science"]
    COLOUR_THEMES = ["Red", "Blue", "Green"]

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
        with open("./7FBF7F5C-A282-466F-A232-7A16C92D92C2_1_105_c.jpeg", "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
        return "data:image/jpeg;base64," + base64_string

    def generate(self):
        return {
            "name": self.random_university_name(),
            "colour_theme": self.random_colour_theme(),
            "logo_base64": self.random_base64_logo()
        }
