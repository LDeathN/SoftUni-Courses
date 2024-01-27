from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        gear = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
        return gear

    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            return f"Extreme"
        elif 2000 <= self.elevation <= 3000:
            return "Advanced"

