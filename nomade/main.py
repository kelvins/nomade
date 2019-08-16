import click


@click.group()
def cli():
    pass


@cli.command(help='Create a new migration')
def migrate():
    pass


@cli.command(help='Upgrade migrations')
def upgrade():
    pass


@cli.command(help='Downgrade migrations')
def downgrade():
    pass


@cli.command(help='Show migrations history')
def history():
    pass


@cli.command(help='Show the current migration')
def current():
    pass


if __name__ == '__main__':
    cli()
