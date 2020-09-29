"""Bot CLI module."""
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
            key: discord bot key.

        """
        bot = BilBot()
        bot.run(key)

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
