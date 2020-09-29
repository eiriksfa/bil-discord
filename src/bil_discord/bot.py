"""Bil-bot module."""
import random
from typing import List, Tuple

import discord

a_nations = [
    "Saladin",
    "Amanitore",
    "Hojo Tokimune",
    "Robert the Bruce",
    "Montezuma",
    "Gorgo",
    "Pericles",
    "Shaka",
    "Suleiman",
    "John Curtin",
    "Matthias",
    "Teddy Roosevelt  ( base game)",
    "Pachacuti",
    "Menelik II",
    "Rough Rider Teddy",
    "Trajan",
    "Wilhelmina",
    "Genghis Khan",
    "Gitarja",
    "Poundmaker",
    "Gilgamesh",
    "Jadwiga",
    "Pedro",
    "Tomyris",
    "Kristina",
    "Mansa Musa",
    "Qin Shi Quang",
    "Alexander",
    "Wilfrid Laurier",
    "Lady Six Sky",
    "Catherine",
    "Lautaro",
    "Cleopatra",
    "Mvemba ",
    "Victoria",
    "Dido",
    "Eleanor (France)",
    "Gaul",
    "Byzantium",
]


class BilBot(discord.Client):
    """Bil-Bot class."""

    @staticmethod
    def get_nations(players: List[str], nations: List[str]) -> List[Tuple[str, str]]:
        """Get nations bot command.

        Creates a list of randomized player-nation tuples based on a list of players
            and a list of nations.

        Args:
            players: players to give a nation
            nations: list of nations to assign from

        Returns:
            List of players with their assigned nation

        """
        result = []
        players = random.sample(players, len(players))
        for player in players:
            nation = random.choice(nations)
            nations.remove(nation)
            result.append((player, nation))
        return result

    async def on_ready(self) -> None:
        """On-ready listener."""
        print("Logged on as", self.user)

    async def on_message(self, message: discord.message.Message) -> None:
        """On message listener.

        Listener function for discord messages.

        Args:
            message: discord message object

        """
        # don't respond to ourselves
        if message.author == self.user:
            return

        msg_split = message.content.split(" ")

        if msg_split[0] != "!bil" or msg_split[1] != "civstart":
            return

        players = msg_split[2:]
        say = self.get_nations(players, a_nations)
        for msg in say:
            await message.channel.send(f"{msg[0]} - {msg[1]}")
