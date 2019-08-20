import click
from colorama import Fore

from nomade import Nomade
from __init__ import __version__


@click.group()
def cli():
    print(Fore.CYAN + f'Nomade ({__version__})')
    pass


@cli.command(help='Init the migration manager')
def init():
    Nomade.init()


@cli.command(help='Create a new migration')
@click.argument('name')
def migrate(name):
    nomade = Nomade()
    nomade.migrate(name)


@cli.command(help='Upgrade migrations')
def upgrade():
    nomade = Nomade()
    nomade.upgrade()


@cli.command(help='Downgrade migrations')
def downgrade():
    nomade = Nomade()
    nomade.downgrade()


@cli.command(help='Show migrations history')
def history():
    nomade = Nomade()
    nomade.history()


@cli.command(help='Show the current migration')
def current():
    nomade = Nomade()
    nomade.current()


if __name__ == '__main__':
    cli()
