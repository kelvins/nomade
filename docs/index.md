# About

Nomade is a simple migration manager tool that aims to be easy to integrate with any ORM (e.g. [SQLAlchemy](https://www.sqlalchemy.org/), [Peewee](http://docs.peewee-orm.com/en/latest/), [Pony](https://ponyorm.org/)) and database (e.g. [SQLite](https://www.sqlite.org/index.html), [MySQL](https://www.mysql.com/), [PostgreSQL](https://www.postgresql.org/)). It is basically a command-line interface (CLI) tool that manages migrations (Python files) by applying changes to the database schema and storing the current migration ID.

This tool was inspired by [alembic](https://alembic.sqlalchemy.org/en/latest/) (if you are using SQLAlchemy as ORM you should consider using alembic).

> **Note**: this project is still under development so you may find bugs. If you find any bug, feel free to contribute by creating an issue and/or submitting a PR to fix it.

## Installation

Use [pip](https://pip.pypa.io/en/stable/installing/) to install Nomade:

```bash
$ pip install nomade
```

## Quick Start

Initialize a **Nomade** project:

```bash
$ nomade init
```

It will create the following project structure:

```
.
├── nomade
│   ├── template.py.j2
│   └── migrations
└── pyproject.toml
```

Define **Nomade** settings in the `pyproject.toml` file, for example:

```toml
[tool.nomade]
migrations = "nomade/migrations"
template = "nomade/template.py.j2"
connection-string = "sqlite:///nomade.db"
date-format = "%d/%m/%Y"
name-format = "{date}_{time}_{id}_{slug}"
```

**Note**: check out all **Nomade** settings in the [settings](./settings.md) documentation.

Then, create your first migration:

```bash
$ nomade migrate "Create first table"
```

Implement the `upgrade` and `downgrade` functions in the migration file.

Then apply the migration to the database:

```bash
$ nomade upgrade head
```

To discover more **Nomade** features please read [commands](./commands.md) documentation or call for help:

```
$ nomade --help

Usage: nomade [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  current    Show the current migration.
  downgrade  Downgrade migrations.
  history    Show migrations history.
  init       Init a Nomade project.
  migrate    Create a new migration.
  stamp      Stamp a specific migration to the database.
  upgrade    Upgrade migrations.
  version    Show Nomade version.
```

