import click

from nomade import __version__, nomade
from nomade.constants import level


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
    nomade.Nomade.init()


@cli.command()
@click.argument('name', required=True)
def migrate(name):
    """Create a new migration.

    Example:\n
        nomade migrate "Create X table"
    """
    nomade.Nomade().migrate(name)


@cli.command()
@click.argument('steps', required=True)
def upgrade(steps):
    """Upgrade migrations.

    Example:\n
        nomade upgrade 1\n
        nomade upgrade head
    """
    nomade.Nomade().upgrade(steps)


@cli.command()
@click.argument('steps', required=True)
def downgrade(steps):
    """Downgrade migrations.

    Example:\n
        nomade downgrade 1\n
        nomade downgrade tail
    """
    nomade.Nomade().downgrade(steps)


@cli.command()
def history():
    """Show migrations history.

    Example:\n
        nomade history
    """
    nomade.Nomade().history()


@cli.command()
def current():
    """Show the current migration.

    Example:\n
        nomade current
    """
    nomade.Nomade().current()


if __name__ == '__main__':
    cli()
