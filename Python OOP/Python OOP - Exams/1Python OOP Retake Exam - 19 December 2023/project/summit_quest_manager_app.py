from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers = []
        self.peaks = []
        self.climbed_peaks = []

    def register_climber(self, climber_type, climber_name: str):
        if climber_type not in ["ArcticClimber", "SummitClimber"]:
            return f"{climber_type} doesn't exist in our register."
        climber = [c for c in self.climbers if c.name == climber_name]
        if climber:
            return f"{climber_name} has been already registered."
        if climber_type == "ArcticClimber":
            new_climber = ArcticClimber(climber_name)
        elif climber_type == "SummitClimber":
            new_climber = SummitClimber(climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in ["ArcticPeak", "SummitPeak"]:
            return f"{peak_type} is an unknown type of peak."
        if peak_type == "ArcticPeak":
            new_peak = ArcticPeak(peak_name, peak_elevation)
        elif peak_type == "SummitPeak":
            new_peak = SummitPeak(peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list):
        climber = [c for c in self.climbers if c.name == climber_name][0]
        peak = [p for p in self.peaks if p.name == peak_name][0]
        recommended_gear = peak.get_recommended_gear()
        missing_gear = []
        for item in recommended_gear:
            if item not in gear:
                climber.is_prepared = False
                missing_gear.append(item)
        if climber.is_prepared:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = [c for c in self.climbers if c.name == climber_name]
        if not climber:
            return f"Climber {climber_name} is not registered yet."
        climber = climber[0]
        peak = [p for p in self.peaks if p.name == peak_name]
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        peak = peak[0]
        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            if peak not in self.climbed_peaks:
                self.climbed_peaks.append(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers = [c for c in self.climbers if c.conquered_peaks]
        ordered_climbers = sorted(climbers, key=lambda c: (-len(c.conquered_peaks), c.name))
        result = [f"Total climbed peaks: {len(self.climbed_peaks)}"]
        result.append(f"**Climber's statistics:**")
        for climber in ordered_climbers:
            climber.conquered_peaks = sorted(climber.conquered_peaks)
            result.append(climber.__str__())
        return "\n".join(result)


