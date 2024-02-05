from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type == FreeDiver.type_ or diver_type == ScubaDiver.type_:
            diver = self._get_diver(diver_name)
            if diver is not None:
                return f"{diver_name} is already a participant."
            if diver_type == ScubaDiver.type_:
                new_diver = ScubaDiver(diver_name)
            else:
                new_diver = FreeDiver(diver_name)
            self.divers.append(new_diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."
        else:
            return f"{diver_type} is not allowed in our competition."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type == DeepSeaFish.type_ or fish_type == PredatoryFish.type_:
            fish = self._get_fish(fish_name)
            if fish is not None:
                return f"{fish_name} is already permitted."
            if fish_type == PredatoryFish.type_:
                new_fish = PredatoryFish(fish_name, points)
            else:
                new_fish = DeepSeaFish(fish_name, points)
            self.fish_list.append(new_fish)
            return f"{fish_name} is allowed for chasing as a {fish_type}."
        else:
            return f"{fish_type} is forbidden for chasing in our competition."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = [d for d in self.divers if d.name == diver_name]
        if not diver:
            return f"{diver_name} is not registered for the competition."
        diver = diver[0]
        fish = [f for f in self.fish_list if f.name == fish_name]
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."
        fish = fish[0]
        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_for_recovery = [d for d in self.divers if d.has_health_issue]
        for diver in divers_for_recovery:
            diver.has_health_issue = False
            diver.renew_oxy()
        return f"Divers recovered: {len(divers_for_recovery)}"

    def diver_catch_report(self, diver_name: str):
        diver = [d for d in self.divers if d.name == diver_name][0]
        result = []
        result.append(f"**{diver_name} Catch Report**")
        for fish in diver.catch:
            result.append(fish.fish_details())
        return "\n".join(result)

    def competition_statistics(self):
        divers_with_good_health = [d for d in self.divers if not d.has_health_issue]
        ordered = sorted(divers_with_good_health, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = []
        result.append(f"**Nautical Catch Challenge Statistics**")
        for diver in ordered:
            result.append(str(diver))
        return "\n".join(result)

    def _get_diver(self, diver_name: str):
        diver = [d for d in self.divers if d.name == diver_name]
        return diver[0] if diver else None

    def _get_fish(self, fish_name: str):
        fish = [f for f in self.fish_list if f.name == fish_name]
        return fish[0] if fish else None