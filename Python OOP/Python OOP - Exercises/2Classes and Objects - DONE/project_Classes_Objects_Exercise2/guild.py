from project.player import Player

class Guild:
    def __init__(self, name,):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated" and player.name not in self.players:
            self.players.append(player)
            player.guild = f"{self.name}"
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player in self.players:
            return f"Player {player.name} is already in the guild."

        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        for player1 in self.players:
            if player1.name == player_name:
                self.players.remove(player1)
                player1.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = []
        result.append(f"Guild: {self.name}")
        for player1 in self.players:
            result.append(player1.player_info())

        return "\n".join(result)

























