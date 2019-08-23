import click
from colorama import Fore

import log
from nomade import Nomade
from __init__ import __version__


@click.group()
def cli():
    pass


@cli.command()
def version():
    """Show Nomade version."""
    log.info(f'Nomade ({__version__})')


@cli.command()
def init():
    """Init a Nomade project."""
    Nomade.init()


@cli.command()
@click.argument('name')
def migrate(name):
    """Create a new migration."""
    nomade = Nomade()
    nomade.migrate(name)


@cli.command()
@click.argument('steps', required=False)
def upgrade(steps):
    """Upgrade migrations."""
    nomade = Nomade()
    nomade.upgrade(steps)


@cli.command()
@click.argument('steps', required=False)
def downgrade(steps):
    """Downgrade migrations."""
    nomade = Nomade()
    nomade.downgrade(steps)


@cli.command()
def history():
    """Show migrations history."""
    nomade = Nomade()
    nomade.history()


@cli.command()
def current():
    """Show the current migration."""
    nomade = Nomade()
    nomade.current()


if __name__ == '__main__':
    cli()
