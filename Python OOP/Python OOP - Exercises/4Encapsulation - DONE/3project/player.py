class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self._name = name
        self._Player__sprint = sprint
        self._Player__dribble = dribble
        self._Player__passing = passing
        self._Player__shooting = shooting

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Player: {self._name}\nSprint: {self._Player__sprint}\nDribble: {self._Player__dribble}\nPassing: {self._Player__passing}\nShooting: {self._Player__shooting}"
