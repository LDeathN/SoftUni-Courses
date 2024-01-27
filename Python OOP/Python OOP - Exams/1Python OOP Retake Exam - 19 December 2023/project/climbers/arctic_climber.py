from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak

class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, strength=200)

    def can_climb(self):
        if self.strength >= 100:
            return True
        else:
            return False

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        elif peak.difficulty_level == "Advanced":
            self.strength -= 20 * 1.5
        self.conquered_peaks.append(peak.name)
