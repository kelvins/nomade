import click
from colorama import Fore

from nomade.constants import level
from nomade import nomade
from nomade import __version__


@click.group()
def cli():
    pass


@cli.command()
def version():
    """Show Nomade version."""
    click.secho(f'Nomade ({__version__})', fg=level.INFO)


@cli.command()
def init():
    """Init a Nomade project."""
    nomade.Nomade.init()


@cli.command()
@click.argument('name')
def migrate(name):
    """Create a new migration."""
    nomade = nomade.Nomade()
    nomade.migrate(name)


@cli.command()
@click.argument('steps', required=False)
def upgrade(steps):
    """Upgrade migrations."""
    nomade = nomade.Nomade()
    nomade.upgrade(steps)


@cli.command()
@click.argument('steps', required=False)
def downgrade(steps):
    """Downgrade migrations."""
    nomade = nomade.Nomade()
    nomade.downgrade(steps)


@cli.command()
def history():
    """Show migrations history."""
    nomade = nomade.Nomade()
    nomade.history()


@cli.command()
def current():
    """Show the current migration."""
    nomade = nomade.Nomade()
    nomade.current()


if __name__ == '__main__':
    cli()
