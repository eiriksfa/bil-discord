"""Bot CLI module."""
import os

import click

from bil_discord.bot import BilBot


class CLI:
    """CLI Application."""

    @staticmethod
    @click.command("start")
    @click.argument("key", type=str)
    def cli(key: str) -> None:
        """Bot CLI entrypoint.

        Args:
            key: environment variable name for discord bot key.

        """
        disc_key = os.getenv(key)
        bot = BilBot()
        bot.run(disc_key)

    def run(self) -> None:
        """Run CLI Application."""
        self()

    def __call__(self) -> None:
        """Run CLI Application."""
        self.cli()


def main() -> None:
    """Bot entrypoint."""
    cli = CLI()
    cli()


if __name__ == "__main__":
    main()
