"""Tests for bil-bot."""
import random

from bil_discord.bot import BilBot


def test_pull_simple() -> None:
    # Setup
    bil = BilBot()
    players = ["Test1", "Test2"]
    nations = ["Nation1", "Nation2", "Nation3"]
    random.seed("fs43241")
    expected = [("Test1", "Nation2"), ("Test2", "Nation3")]

    # Act
    result = bil.get_nations(players, nations)

    # Assert
    assert result == expected
