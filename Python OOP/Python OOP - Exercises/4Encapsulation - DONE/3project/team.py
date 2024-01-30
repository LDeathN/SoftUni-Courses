from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self._Team__name = name
        self._Team__rating = rating
        self._Team__players = []

    def add_player(self, player: Player):
        if player in self._Team__players:
            return f"Player {player.name} has already joined"
        else:
            self._Team__players.append(player)
            return f"Player {player.name} joined team {self._Team__name}"

    def remove_player(self, player_name: str):
        for player in self._Team__players:
            if player.name == player_name:
                self._Team__players.remove(player)
                return player
        return f"Player {player_name} not found"
