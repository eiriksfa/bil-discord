"""Bot CLI module."""
import os

import click

from bil_discord.bot import BilBot


class CLI:
    """CLI Application."""

    @staticmethod
    @click.command("start")
    @click.option("--key_env_var", type=str, default="DISCORD_KEY")
    @click.option("--key", type=str, default=None)
    def cli(key_env_var: str, key: str = None) -> None:
        """Bot CLI entrypoint.

        Args:
            key_env_var: environment variable name for discord bot key.
            key: discord bot key, will take priority over env var if provided.

        """
        disc_key = os.getenv(key_env_var) if key is None else key
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
