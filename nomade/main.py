import click

from nomade import __version__
from nomade.constants import level
from nomade.nomad import Nomad


@click.group()
def cli():
    pass


@cli.command()
def version():
    """Show Nomade version.

    Example:\n
        nomade version
    """
    click.secho(f'Nomade ({__version__})', fg=level.INFO)


@cli.command()
def init():
    """Init a Nomade project.

    Example:\n
        nomade init
    """
    Nomad.init()


@cli.command()
@click.argument('name', required=True)
def migrate(name):
    """Create a new migration.

    Example:\n
        nomade migrate "Create X table"
    """
    Nomad().migrate(name)


@cli.command()
@click.argument('steps', required=True)
def upgrade(steps):
    """Upgrade migrations.

    Example:\n
        nomade upgrade 1\n
        nomade upgrade head
    """
    Nomad().upgrade(steps)


@cli.command()
@click.argument('steps', required=True)
def downgrade(steps):
    """Downgrade migrations.

    Example:\n
        nomade downgrade 1\n
        nomade downgrade tail
    """
    Nomad().downgrade(steps)


@cli.command()
def history():
    """Show migrations history.

    Example:\n
        nomade history
    """
    Nomad().history()


@cli.command()
def current():
    """Show the current migration.

    Example:\n
        nomade current
    """
    Nomad().current()


@cli.command()
@click.argument('migration_id', required=True)
def stamp(migration_id):
    """Stamp a specific migration to the database.

    Example:\n
        nomade stamp 19ma82h1
    """
    Nomad().stamp(migration_id)


if __name__ == '__main__':
    cli()
