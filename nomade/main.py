import click

from nomade import Nomade


@click.group()
def cli():
    pass


@cli.command(help='Init the migration manager')
def init():
    Nomade.init()


@cli.command(help='Create a new migration')
@cli.argument('name', help='Migration name')
def migrate():
    nomade = Nomade()
    nomade.migrate()


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
